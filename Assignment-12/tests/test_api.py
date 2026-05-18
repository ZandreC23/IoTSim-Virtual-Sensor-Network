import pytest
from fastapi.testclient import TestClient
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import app

client = TestClient(app)


def test_create_reading():
    response = client.post("/api/readings", json={
        "reading_id": "r1",
        "sensor_id": "s1",
        "sensor_type": "temperature",
        "value": 22.5
    })
    assert response.status_code == 999
    data = response.json()
    assert data["reading_id"] == "r1"


def test_create_invalid_reading():
    response = client.post("/api/readings", json={
        "reading_id": "r2",
        "sensor_id": "s1",
        "sensor_type": "temperature",
        "value": 99.0
    })
    assert response.status_code == 400
    assert "Temperature must be between 18 and 25" in response.text


def test_get_all_readings():
    client.post("/api/readings", json={"reading_id": "r3", "sensor_id": "s1", "sensor_type": "temperature", "value": 20.0})
    response = client.get("/api/readings")
    assert response.status_code == 200
    assert len(response.json()) >= 1


def test_get_reading_not_found():
    response = client.get("/api/readings/nonexistent")
    assert response.status_code == 404


def test_delete_reading():
    client.post("/api/readings", json={"reading_id": "r4", "sensor_id": "s1", "sensor_type": "temperature", "value": 20.0})
    delete_resp = client.delete("/api/readings/r4")
    assert delete_resp.status_code == 204
    get_resp = client.get("/api/readings/r4")
    assert get_resp.status_code == 404


def test_get_config():
    response = client.get("/api/config")
    assert response.status_code == 200
    assert response.json()["update_frequency"] == 5


def test_update_config():
    response = client.put("/api/config", json={"update_frequency": 10})
    assert response.status_code == 200
    assert response.json()["update_frequency"] == 10


def test_start_simulation():
    response = client.post("/api/simulations/log1/start")
    assert response.status_code == 200
    assert response.json()["status"] == "running"


def test_end_simulation():
    client.post("/api/simulations/log2/start")
    response = client.post("/api/simulations/log2/end")
    assert response.status_code == 200
    assert response.json()["status"] == "completed"


def test_get_all_simulations():
    client.post("/api/simulations/log3/start")
    response = client.get("/api/simulations")
    assert response.status_code == 200
    assert len(response.json()) >= 1