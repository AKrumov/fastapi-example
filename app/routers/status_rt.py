from fastapi import APIRouter, Request

from app.schemas.response_sch import BaseResponse
from app.utils.response_uts import ok
from app.config.logger_cfg import logger

router = APIRouter()


@router.get("/status", response_model=BaseResponse)
async def status():
    """
    Check If application is healthy
    """
    logger.info(f"Application is Healthy")
    return ok(message="Service is healthy!")
