from fastapi import FastAPI

app = FastAPI()

@app.get("/activities")
def get_activities():
    # return a list of activities
    return [{"id": 1, "name": "Activity 1"}, {"id": 2, "name": "Activity 2"}]

@app.post("/signup")
def signup_for_activity(payload: dict):
    # handle signup
    return {"message": "Signup successful", "payload": payload}

from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_get_activities():
    response = client.get("/activities")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    assert "Chess Club" in data

def test_signup_for_activity():
    activity_name = "Chess Club"
    email = "newstudent@mergington.edu"
    response = client.post(f"/activities/{activity_name}/signup?email={email}")
    assert response.status_code == 200
    result = response.json()
    assert "message" in result
    # Check if the student was added
    get_response = client.get("/activities")
    assert email in get_response.json()[activity_name]["participants"]