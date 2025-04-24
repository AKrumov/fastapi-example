from typing import Any, Optional

from pydantic import BaseModel


class BaseResponse(BaseModel):
    status: str
    message: str
    data: Optional[Any] = None

    class Config:
        json_schema_extra = {
            "example": {
                "status": "success",
                "message": "Service is healthy!",
                "data": None,
            }
        }
