import json
from app.auth.schemas import UserResponse, user_request_schema
from app.tests.conftest import RANDOM_STR


def test_helloworld_page(client):
    resp = client.get("/auth/")  # Make sure to use the correct URL path
    assert resp.status_code == 200  # Check if the status code is 200 (OK)
    assert resp.content_type == "application/json"  # Check if the content type is JSON
    json_data = json.loads(resp.data)  # Parse the JSON content
    assert "Hello" in json_data  # Check if the "Hello" key is present in the JSON data
    assert (
        json_data["Hello"] == "Hello"
    )  # Check if the value of the "Hello" key is "Hello"


def test_register_user(client):
    user_request = {"email": f"{RANDOM_STR}", "password": "123"}
    user_request_schema.load(user_request)
    resp = client.post("/auth/register", json=user_request)

    assert resp.status_code == 200
    assert resp.content_type == "application/json"

    # Parse the JSON response content
    json_data = json.loads(resp.data)
    schema = UserResponse()
    validation_errors = schema.validate(json_data)

    # Check if the validation was successful
    assert not validation_errors

    # Check if the email and token fields are present in the JSON response
    assert "email" in json_data
    assert "token" in json_data

    # Check if the email matches the user request email
    assert json_data["email"] == user_request["email"]


def test_register_user_wrong_params(client):
    user_request = {"emai": f"{RANDOM_STR}@example.com", "passwor": "password123"}
    resp = client.post("/auth/register", json=user_request)

    assert resp.status_code == 400
    assert resp.content_type == "application/json"

    # Parse the JSON response content
    json_data = json.loads(resp.data)
    schema = UserResponse()
    validation_errors = schema.validate(json_data)

    # Check if the validation wasn't successful
    assert validation_errors["error"] == ["Unknown field."]

    assert "error" in json_data


def test_register_user_wrong_values(client):
    user_request = {"email": "notemail", "password": "password123"}
    resp = client.post("/auth/register", json=user_request)

    assert resp.status_code == 400
    assert resp.content_type == "application/json"

    # Parse the JSON response content
    json_data = json.loads(resp.data)
    schema = UserResponse()
    validation_errors = schema.validate(json_data)

    # Check if the validation wasn't successful
    assert validation_errors["error"] == ["Unknown field."]

    assert "error" in json_data
    assert (
        json_data["error"]
        == "Validation error: {'email': ['Not a valid email address.']}"
    )
