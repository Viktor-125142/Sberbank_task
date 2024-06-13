from fastapi import APIRouter, HTTPException
from typing import List, Dict


from app.operations.schemas import DepositRequest
from app.operations.services import calculate_deposit

router_calculate = APIRouter(
    prefix="/calculate",
    tags=["calculate_deposit"]
)


@router_calculate.post("",
                       response_model=List[Dict[str, float]],
                       status_code=200
                       )
def calculate_endpoint(
        request: DepositRequest
) -> List[Dict[str, float]]:
    try:
        result = calculate_deposit(request)
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
