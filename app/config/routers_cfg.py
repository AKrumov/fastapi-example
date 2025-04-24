from fastapi import FastAPI

from app.config.settings_cfg import Settings
from app.routers import status_rt

config = Settings().app


def configure(app: FastAPI):
    app.include_router(status_rt.router, prefix=config['root_path'], tags=["Health Check"])
