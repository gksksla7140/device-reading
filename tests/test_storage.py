import pytest
from app.storage import ReadingsStorage, DeviceNotFound
from app.models import DeviceReadings, Reading

@pytest.fixture
def storage():
    return ReadingsStorage()

def test_readings_storage_singleton():
    storage_instance1 = ReadingsStorage()
    storage_instance2 = ReadingsStorage()

    assert storage_instance1 is storage_instance2

def test_store_and_fetch_readings(storage):
    readings_data = DeviceReadings(
        id="device_id",
        readings=[
            Reading(timestamp="2021-09-29T16:08:15+01:00", count=2),
            Reading(timestamp="2021-09-29T16:09:15+01:00", count=15)
        ]
    )
    storage.store_readings(readings_data)
    
    actual = storage.fetch_readings(readings_data.id)
    expected = readings_data.model_dump()["readings"]
    assert actual == expected

def test_fetch_readings_device_not_found(storage):
    with pytest.raises(DeviceNotFound):
        storage.fetch_readings("non_existent_device_id")


