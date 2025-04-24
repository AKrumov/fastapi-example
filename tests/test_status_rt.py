import pytest
from fastapi import status
from fastapi.testclient import TestClient
from main import app


@pytest.mark.asyncio
async def test_lifespan():
    with TestClient(app) as client:
        response = client.get("/api/v1/status")
        assert response.status_code == status.HTTP_200_OK
        assert response.json() == {"data": None, "message": "Service is healthy!", "status": "success"}
