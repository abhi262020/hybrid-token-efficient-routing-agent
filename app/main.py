from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import router
from app.config import settings

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
)

origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    "https://hybrid-token-efficient-routing-agen-six.vercel.app",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)


@app.get("/")
def root():
    return {
        "application": settings.APP_NAME,
        "status": "running",
        "docs": "/docs",
    }