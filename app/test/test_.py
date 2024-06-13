from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_calculate_deposit_route():
    request_data = {
        "date": "31.01.2021",
        "periods": 7,
        "amount": 10000,
        "rate": 6.0
    }

    response = client.post("/calculate", json=request_data)
    print(response.status_code)
    print(response.json())
    assert response.status_code == 200
    expected_results = [
        {"31.01.2021": 10050.00},
        {"28.02.2021": 10100.25},
        {"31.03.2021": 10150.75},
        {"30.04.2021": 10201.51},
        {"31.05.2021": 10252.51},
        {"30.06.2021": 10303.78},
        {"31.07.2021": 10355.29},
    ]
    assert response.json() == expected_results


def test_calculate_deposit_route_invalid_date():
    request_data = {
        "date": "31-01-2021",
        "periods": 7,
        "amount": 10000,
        "rate": 6.0
    }

    response = client.post("/calculate/", json=request_data)
    assert response.status_code == 400


def test_calculate_deposit_route_invalid_periods():
    request_data = {
        "date": "31.01.2021",
        "periods": 0,
        "amount": 10000,
        "rate": 6.0
    }

    response = client.post("/calculate/", json=request_data)
    assert response.status_code == 400


def test_calculate_deposit_route_invalid_amount():
    request_data = {
        "date": "31.01.2021",
        "periods": 7,
        "amount": 5000,
        "rate": 6.0
    }

    response = client.post("/calculate/", json=request_data)
    assert response.status_code == 400


def test_calculate_deposit_route_invalid_rate():
    request_data = {
        "date": "31.01.2021",
        "periods": 7,
        "amount": 10000,
        "rate": 0
    }

    response = client.post("/calculate", json=request_data)
    assert response.status_code == 400
