def test_login_success(client):
    """Ensure login works with valid credentials"""
    response = client.post("/login", json={"username": "admin", "password": "secret"})
    assert response.status_code == 200
    assert "token" in response.json

def test_login_failure(client):
    """Ensure login fails with invalid credentials"""
    response = client.post("/login", json={"username": "wrong", "password": "bad"})
    assert response.status_code == 401
    assert "error" in response.json
