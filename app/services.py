# app/services.py
import os
from sqlalchemy.future import select
from sqlalchemy.orm import Session

from .models import Screenshot
from .config import SCREENSHOTS_DIR, SessionLocal
from playwright.sync_api import sync_playwright


def get_screenshot_urls(id: str):
    with SessionLocal() as session:
        try:
            result = session.execute(select(Screenshot).where(Screenshot.id == id))
            screenshot = result.scalars().first()
            if screenshot:
                return screenshot.urls.split(",")
        finally:
            session.close()

def save_screenshots(id: str, urls: list):
    with SessionLocal() as session:
        try:
            static_urls = [f"/static/screenshots/{os.path.basename(url)}" for url in urls]
            new_screenshot = Screenshot(id=id, urls=",".join(static_urls))
            session.add(new_screenshot)
            session.commit()
        except:
            session.rollback()

def crawl_and_capture_screenshots(start_url: str, number_of_links: int, id: str) -> list:
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        page.goto(start_url)
        screenshot_path = os.path.join(SCREENSHOTS_DIR, f"{id}_0.png")
        page.screenshot(path=screenshot_path)

        urls = [screenshot_path]
        links = page.eval_on_selector_all('a', 'elements => elements.map(el => el.href)')
        links = links[:number_of_links]

        for index, link in enumerate(links):
            page.goto(link)

            screenshot_path = os.path.join(SCREENSHOTS_DIR, f"{id}_{index + 1}.png")

            page.screenshot(path=screenshot_path)
            urls.append(screenshot_path)

        browser.close()

        save_screenshots(id, urls)

    return urls