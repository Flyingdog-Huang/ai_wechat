from fastapi import FastAPI
from dotenv import load_dotenv
import os
from . import settings
from tortoise.contrib.fastapi import register_tortoise
from .apps.common.views import app as common_app
from .apps.users.views import app as users_app
from .utils import middleware, exceptions

def create_app() -> FastAPI:
    load_dotenv()
    app = FastAPI(
        title=os.environ.get("APP_NAME"),
        summary=os.environ.get("APP_SUMMARY"),
        description=os.environ.get("APP_DESCRIPTION"),
        version=os.environ.get("APP_VERSION"),
        exception_handlers={
            exceptions.HTTPException: exceptions.global_http_exception_handler,
            exceptions.RequestValidationError: exceptions.global_request_exception_handler,
        },
    )
    # load_dotenv()
    # print(os.environ.get("APP_TIMEZONE"))
    register_tortoise(
        app,
        config=settings.TORTOISE_ORM,
        generate_schemas=False,
        add_exception_handlers=True
    )
    app.include_router(common_app)
    app.include_router(users_app, prefix="/users")

    http_middleware = app.middleware("http")
    http_middleware(middleware.log_requests)

    return app