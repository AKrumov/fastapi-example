from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config.settings_cfg import Settings

config = Settings().app


def configure(app: FastAPI):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
