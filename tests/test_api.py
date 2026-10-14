from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    result = client.get("/health")
    assert result.status_code == 200
    assert result.json() == {"status": "ok"}
