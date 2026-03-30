import pytest
from fastapi.testclient import TestClient
import sys
from pathlib import Path

# Add src directory to path so we can import app
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from app import app

@pytest.fixture
def client():
    """Create a test client for the FastAPI app"""
    return TestClient(app)

@pytest.fixture
def reset_activities():
    """Reset activities to initial state before each test"""
    from app import activities
    
    # Store original state
    original_activities = {}
    for name, data in activities.items():
        original_activities[name] = {
            "description": data["description"],
            "schedule": data["schedule"],
            "max_participants": data["max_participants"],
            "participants": data["participants"].copy()
        }
    
    yield
    
    # Restore original state
    activities.clear()
    activities.update(original_activities)
