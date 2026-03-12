import os
from dotenv import load_dotenv

load_dotenv()

CANVAS_API_TOKEN = os.getenv("CANVAS_API_TOKEN")
CANVAS_BASE_URL = os.getenv("CANVAS_BASE_URL", "https://boisestatecanvas.instructure.com")

if not CANVAS_API_TOKEN:
    raise ValueError("CANVAS_API_TOKEN missing from .env")