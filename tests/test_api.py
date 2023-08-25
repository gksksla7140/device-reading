import pytest
from fastapi.testclient import TestClient
from main import app
from app.models import DeviceReadings, Reading

class TestAPI:
    client = TestClient(app)

    @pytest.mark.asyncio
    async def test_store_and_fetch_readings(self):
        device_id = "device_id"
        readings_data = {
            "id": device_id,
            "readings": [
                {"timestamp": "2021-09-29T16:08:15+01:00", "count": 2},
                {"timestamp": "2021-09-29T16:09:15+01:00", "count": 15}
            ]
        }
        store_response =  self.client.post("/store_readings/", json=readings_data)
        assert store_response.status_code == 200

        fetch_response =  self.client.get(f"/fetch_readings/{device_id}")
        assert fetch_response.status_code == 200
        assert "readings" in fetch_response.json()

    @pytest.mark.asyncio
    async def test_store_duplicated_readings(self):
        device_id = "duplicated_id"
        readings_data = {
            "id": device_id,
            "readings": [
                {"timestamp": "2021-09-29T16:08:15+01:00", "count": 2},
                {"timestamp": "2021-09-29T16:08:15+01:00", "count": 2}  # Duplicated reading
            ]
        }

        store_response = self.client.post("/store_readings/", json=readings_data)
        assert store_response.status_code == 200

        fetch_response = self.client.get(f"/fetch_readings/{device_id}")
        assert fetch_response.status_code == 200

        assert len(fetch_response.json()["readings"]) == 1

    @pytest.mark.asyncio
    async def test_store_invalid_readings(self):
        invalid_readings_data = {
            "id": "device_id",
            "readings": [
                {"timestamp": "2021-09-29T16:08:15+01:00", "count": "invalid_count"}
            ]
        }

        store_response = self.client.post("/store_readings/", json=invalid_readings_data)
        assert store_response.status_code == 422
