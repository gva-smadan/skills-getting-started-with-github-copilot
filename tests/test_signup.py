import pytest

def test_signup_success(client):
    """Test successful signup."""
    payload = {"username": "testuser", "password": "securepassword"}
    response = client.post("/signup", json=payload)
    assert response.status_code == 201
    assert response.json() == {"message": "User created successfully."}

def test_signup_missing_fields(client):
    """Test signup with missing fields."""
    payload = {"username": "testuser"}
    response = client.post("/signup", json=payload)
    assert response.status_code == 400
    assert "error" in response.json()