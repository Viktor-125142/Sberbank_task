import pytest
from pydantic import ValidationError

from app.operations.services import calculate_deposit
from app.operations.schemas import DepositRequest


def test_calculate_deposit():
    request = DepositRequest(date="31.01.2021",
                             periods=7,
                             amount=10000,
                             rate=6.0
                             )

    expected_results = {
        "31.01.2021": 10050,
        "28.02.2021": 10100.25,
        "31.03.2021": 10150.75,
        "30.04.2021": 10201.51,
        "31.05.2021": 10252.51,
        "30.06.2021": 10303.78,
        "31.07.2021": 10355.29
    }

    results = calculate_deposit(request)
    assert results == expected_results


def test_calculate_deposit_invalid_date():
    with pytest.raises(ValidationError):
        DepositRequest(date="111.13.2021",
                       periods=7,
                       amount=10000,
                       rate=6.0
                       )


def test_calculate_deposit_negative_periods():
    with pytest.raises(ValidationError):
        DepositRequest(date="31.01.2021",
                       periods=-1,
                       amount=10000,
                       rate=6.0
                       )


def test_calculate_deposit_negative_amount():
    with pytest.raises(ValidationError):
        DepositRequest(date="31.01.2021",
                       periods=7,
                       amount=-10000,
                       rate=6.0
                       )


def test_calculate_deposit_invalid_rate():
    with pytest.raises(ValidationError):
        DepositRequest(date="31.01.2021",
                       periods=7,
                       amount=10000,
                       rate=-6.0
                       )
