from pydantic import BaseModel, Field


class DepositRequest(BaseModel):
    date: str = Field(...,
                      pattern=r"^\d{2}\.\d{2}\.\d{4}$",
                      example="01.01.2021"
                      )
    periods: int = Field(...,
                         ge=1,
                         le=60,
                         example=7
                         )
    amount: int = Field(...,
                        ge=10000,
                        le=3000000,
                        example=10000
                        )
    rate: float = Field(...,
                        ge=1.0,
                        le=8.0,
                        example=6.0
                        )
