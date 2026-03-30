import pytest

def test_unregistered_access(client):
    """Test that unregistered users cannot access protected endpoints."""
    response = client.get("/protected")
    assert response.status_code == 401
    assert response.json() == {"error": "Unauthorized access."}