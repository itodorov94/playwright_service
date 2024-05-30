# app/tasks.py
from .celery_config import celery_app
from .services import crawl_and_capture_screenshots

@celery_app.task()
def crawl_and_screenshot(start_url: str, number_of_links: int, id: str):
    return crawl_and_capture_screenshots(start_url, number_of_links, id)
