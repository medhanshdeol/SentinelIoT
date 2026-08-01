from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
import time

from app.routers.camera import router as camera_router
from app.services.logger import logger

app = FastAPI(
    title="SentinelIoT",
    description="AI Enhanced IoT Honeypot",
    version="0.1.0"
)

app.mount(
    "/static",
    StaticFiles(directory="app/static"),
    name="static"
)

app.include_router(camera_router)


@app.middleware("http")
async def log_requests(request: Request, call_next):

    start_time = time.perf_counter()

    response = await call_next(request)

    duration = time.perf_counter() - start_time

    logger.info(
        f"IP={request.client.host} | "
        f"METHOD={request.method} | "
        f"PATH={request.url.path} | "
        f"STATUS={response.status_code} | "
        f"TIME={duration:.4f}s"
    )

    return response


@app.get("/")
async def root():

    return JSONResponse(
        {
            "status": "running",
            "project": "SentinelIoT",
            "version": "0.1.0"
        }
    )


@app.get("/health")
async def health():

    return {
        "status": "healthy"
    }
