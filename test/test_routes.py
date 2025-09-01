def test_ping_returns_pong(client):
    """Check /ping endpoint returns pong"""
    response = client.get("/ping")
    assert response.status_code == 200
    assert response.json == {"message": "pong"}

def test_echo_returns_message(client):
    """Check /echo returns same message"""
    response = client.post("/echo", json={"msg": "Hello"})
    assert response.status_code == 201
    assert response.json["echo"] == "Hello"

def test_echo_missing_msg(client):
    """Check /echo handles missing JSON field"""
    response = client.post("/echo", json={})
    assert response.status_code == 400
    assert "error" in response.json
