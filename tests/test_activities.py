import pytest

class TestGetActivities:
    """Tests for GET /activities endpoint"""
    
    def test_get_all_activities_returns_dict(self, client):
        """Test that GET /activities returns a dictionary of activities"""
        # Arrange
        expected_activities = ["Chess Club", "Programming Class", "Gym Class", 
                              "Basketball Team", "Tennis Club", "Art Studio", 
                              "Drama Club", "Debate Team", "Science Olympiad"]
        
        # Act
        response = client.get("/activities")
        
        # Assert
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, dict)
        assert len(data) == 9
        assert set(data.keys()) == set(expected_activities)
    
    def test_get_activities_response_structure(self, client):
        """Test that each activity has correct structure"""
        # Arrange
        required_fields = {"description", "schedule", "max_participants", "participants"}
        
        # Act
        response = client.get("/activities")
        activities = response.json()
        
        # Assert
        assert len(activities) > 0
        for activity_name, activity_data in activities.items():
            assert required_fields.issubset(set(activity_data.keys()))
            assert isinstance(activity_name, str)
            assert isinstance(activity_data["description"], str)
            assert isinstance(activity_data["schedule"], str)
            assert isinstance(activity_data["max_participants"], int)
            assert isinstance(activity_data["participants"], list)
    
    def test_get_activities_chess_club_details(self, client):
        """Test specific details of Chess Club activity"""
        # Arrange
        club_name = "Chess Club"
        
        # Act
        response = client.get("/activities")
        activities = response.json()
        chess_club = activities.get(club_name)
        
        # Assert
        assert chess_club is not None
        assert chess_club["description"] == "Learn strategies and compete in chess tournaments"
        assert chess_club["schedule"] == "Fridays, 3:30 PM - 5:00 PM"
        assert chess_club["max_participants"] == 12
        assert len(chess_club["participants"]) == 2
        assert "michael@mergington.edu" in chess_club["participants"]
        assert "daniel@mergington.edu" in chess_club["participants"]
