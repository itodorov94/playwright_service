# app/main.py
import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from .config import init_db, SCREENSHOTS_DIR
from .models import Base
from .routes import router as screenshots_router

def create_app():
    app = FastAPI()
    app.include_router(screenshots_router)
    
    @app.on_event("startup")
    def on_startup():
        init_db(Base)
        os.makedirs(SCREENSHOTS_DIR, exist_ok=True)
    
    app.mount("/static/screenshots", StaticFiles(directory=SCREENSHOTS_DIR), name="screenshots")
    return app



app = create_app()

