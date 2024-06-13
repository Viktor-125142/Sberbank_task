import pytest
from pydantic import ValidationError

from app.operations.schemas import DepositRequest


def test_valid_deposit_request():
    request_data = {
        "date": "31.01.2021",
        "periods": 7,
        "amount": 10000,
        "rate": 6.0
    }

    request = DepositRequest(**request_data)
    assert request.date == "31.01.2021"
    assert request.periods == 7
    assert request.amount == 10000
    assert request.rate == 6.0


def test_invalid_date_format():
    request_data = {
        "date": "31-01-2021",
        "periods": 7,
        "amount": 10000,
        "rate": 6.0
    }

    with pytest.raises(ValidationError):
        DepositRequest(**request_data)


def test_invalid_periods():
    request_data = {
        "date": "31.01.2021",
        "periods": 0,
        "amount": 10000,
        "rate": 6.0
    }

    with pytest.raises(ValidationError):
        DepositRequest(**request_data)


def test_invalid_amount():
    request_data = {
        "date": "31.01.2021",
        "periods": 7,
        "amount": 5000,
        "rate": 6.0
    }

    with pytest.raises(ValidationError):
        DepositRequest(**request_data)


def test_invalid_rate():
    request_data = {
        "date": "31.01.2021",
        "periods": 7,
        "amount": 10000,
        "rate": 0
    }

    with pytest.raises(ValidationError):
        DepositRequest(**request_data)
