from app.devices.camera import camera
from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates

from app.services.logger import logger

router = APIRouter(
    prefix="/camera",
    tags=["IP Camera"]
)

templates = Jinja2Templates(directory="app/templates")


@router.get("/login")
async def login_page(request: Request):

    device = camera.get_device_info()

    return templates.TemplateResponse(
        request=request,
        name="camera/login.html",
        context={
            "error": None,
            "camera": device
        }
    )


@router.post("/login")
async def login_attempt(
    request: Request,
    username: str = Form(...),
    password: str = Form(...)
):

    device = camera.get_device_info()

    logger.info(
        f"LOGIN ATTEMPT | "
        f"IP={request.client.host} | "
        f"USERNAME={username} | "
        f"PASSWORD={password}"
    )

    return templates.TemplateResponse(
        request=request,
        name="camera/login.html",
        context={
            "error": "Invalid username or password",
            "camera": device
        }
    )
@router.get("/dashboard")
async def dashboard(request: Request):

    device = camera.get_device_info()

    status = camera.get_status()

    return templates.TemplateResponse(
        request=request,
        name="camera/dashboard.html",
        context={
            "camera": device,
            "status": status
        }
    )
@router.get("/deviceinfo")
async def device_information(request: Request):

    device = camera.get_device_info()

    return templates.TemplateResponse(
        request=request,
        name="camera/deviceinfo.html",
        context={
            "camera": device
        }
    )