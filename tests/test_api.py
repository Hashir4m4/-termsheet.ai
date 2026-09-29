import pytest
from fastapi.testclient import TestClient
from src.main import app
from src.data_generator import seed_data

client = TestClient(app)

def test_health():
    res = client.get("/health")
    assert res.status_code == 200
    assert res.json() == {"status": "ok"}

def test_get_vendors():
    res = client.get("/api/vendors")
    assert res.status_code == 200
    assert "CloudForge" in res.json()["vendors"]

def test_vendor_profile():
    with TestClient(app) as c:
        res = c.get("/api/vendor/CloudForge/profile")
        assert res.status_code == 200
        data = res.json()
        assert data["vendor"] == "CloudForge"
        assert len(data["observations"]) > 0
        assert "15%" in data["observations"][0]

def test_strategy_memory():
    with TestClient(app) as c:
        res = c.post("/api/strategy", json={
            "vendor": "CloudForge",
            "current_offer": "$120k",
            "use_memory": True
        })
        assert res.status_code == 200
        data = res.json()
        assert data["mode"] == "Memory"
        assert "15%" in data["recommendation"]
        assert len(data["evidence"]) > 0

def test_strategy_control():
    res = client.post("/api/strategy", json={
        "vendor": "CloudForge",
        "current_offer": "$120k",
        "use_memory": False
    })
    assert res.status_code == 200
    data = res.json()
    assert data["mode"] == "Control"
    assert "5-10%" in data["recommendation"]
    assert len(data["evidence"]) == 0
