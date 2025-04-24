import logging

from fastapi import status as status_code
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from app.schemas.response_sch import BaseResponse

LOGGER = logging.getLogger(__name__)


def ok(status="success", message="", data=None):
    """HTTP Response 200 OK"""
    return custom_response(
        BaseResponse(
            status=status,
            message=message,
            data=data,
        ), status_code.HTTP_200_OK)


def error(status="error", message="", data=None):
    """HTTP Response 500 Internal Server Error"""
    return custom_response(
        BaseResponse(
            status=status,
            message=message,
            data=data,
        ), status_code.HTTP_500_INTERNAL_SERVER_ERROR)


def custom_response(resp: BaseResponse, code: int):
    return JSONResponse(status_code=code, content=jsonable_encoder(resp))
