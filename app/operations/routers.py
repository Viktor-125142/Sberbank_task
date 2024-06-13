from fastapi import APIRouter, HTTPException
from typing import List, Dict

from app.operations.schemas import DepositRequest
from app.operations.services import calculate_deposit

router_calculate = APIRouter(
    prefix="/deposit/calculate",
    tags=["calculate_deposit"]
)


@router_calculate.post("",
                       response_model=List[Dict[str, float]],
                       status_code=200,
                       summary="Calculate deposit",
                       description="Calculate deposit based on input parameters"
                       )
def calculate_endpoint(
        request: DepositRequest
) -> List[Dict[str, float]]:
    result = calculate_deposit(request)
    return result
