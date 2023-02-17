from dataclasses import dataclass
from typing import Optional
from datetime import datetime


@dataclass
class Manufacturer:
    name: str
    last_payment_date: datetime
    balance_due: int
    id: Optional[int] = None

    def format_currency_balance(self):
        balance_in_pounds = self.balance_due / 100
        return "£{0:,.2f}".format(balance_in_pounds)

    def format_date_for_psql(self):
        return self.last_payment_date.strftime("%Y-%m-%d")
