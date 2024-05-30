# app/routes.py
import uuid
from fastapi import APIRouter, HTTPException

from .tasks import crawl_and_screenshot
from .celery_config import celery_app
from .schemas import ScreenshotRequest
from .services import get_screenshot_urls

router = APIRouter()

@router.get("/isalive")
async def is_alive():
    return {"status": "alive"}

@router.post("/screenshots")
def post_screenshot_request(request: ScreenshotRequest):
    id = str(uuid.uuid4())
    task = crawl_and_screenshot.delay(request.start_url, request.number_of_links, id)
    return {"id": id, "task_id": task.id}

@router.get("/screenshots/{id}")
def get_screenshots(id: str):
    urls = get_screenshot_urls(id)
    if urls:
        return {"id": id, "screenshots": urls}
    else:
        raise HTTPException(status_code=404, detail="Screenshots not found")
    
# Endpoint to check task status
@router.get("/tasks/{task_id}")
async def get_task_status(task_id: str):
    task_result = celery_app.AsyncResult(task_id)
    return {"task_id": task_id, "status": task_result.status}
