from datetime import datetime
from typing import List, Dict
import calendar

from app.operations.schemas import DepositRequest


def calculate_deposit(
        request: DepositRequest
) -> List[Dict[str, float]]:

    start_date = datetime.strptime(request.date, '%d.%m.%Y')
    results = []
    rate_per_month = request.rate / 12 / 100

    current_amount = request.amount
    current_date = start_date

    for _ in range(request.periods):
        interest = current_amount * rate_per_month
        current_amount += interest

        last_day_of_month = calendar.monthrange(current_date.year,
                                                current_date.month
                                                )[1]
        result_date = current_date.replace(day=last_day_of_month
                                           ).strftime('%d.%m.%Y')

        results.append({result_date: round(current_amount, 2)})

        next_month = current_date.month + 1 if current_date.month < 12 else 1
        next_year = current_date.year if current_date.month < 12 else current_date.year + 1
        current_date = current_date.replace(year=next_year,
                                            month=next_month,
                                            day=1
                                            )

    return results
