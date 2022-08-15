from fastapi.testclient import TestClient
from main import app


client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert {"Coding Challenge Bankaya"} == {"Coding Challenge Bankaya"}


def test_invalid_number_record1():
    response = client.get("/cat-facts")
    assert response.status_code == 404
    assert response.json() == {'detail':'Not Found'}


def test_invalid_number_record2():
    response = client.get("/cat-facts/501")
    assert response.status_code == 200
    assert {"Number_records must be between 1 and 500"} == {"Number_records must be between 1 and 500"}


def test_invalid_number_record3():
    response = client.get("/cat-facts/abc")
    assert response.status_code == 422
    assert response.json()["detail"][0]["msg"] == "value is not a valid integer"


def test_valid_number_record():
    response = client.get("/cat-facts/10")
    assert response.status_code == 200


def test_api_response_json_exists():
    response = client.get("/cat-facts/10")
    assert response.status_code == 200
    data = response.json()
    assert data != []


def test_updatedAt_item_exists():
    response = client.get("/cat-facts/10")
    assert response.status_code == 200
    data = response.json()
    assert data[0]["updatedAt"] != ""
