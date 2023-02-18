from dataclasses import dataclass
from typing import Optional
from decimal import Decimal
from datetime import datetime


@dataclass
class Manufacturer:
    name: str
    last_payment_date: datetime
    balance_due: Decimal
    id: Optional[int] = None

    def format_currency_balance(self):
        return "£{0:,.2f}".format(self.balance_due)

    def format_date_for_psql(self):
        return self.last_payment_date.strftime("%Y-%m-%d")

    def format_date_for_view(self):
        return self.last_payment_date.strftime("%d %B %Y")
