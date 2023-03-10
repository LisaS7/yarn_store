from dataclasses import dataclass
from typing import Optional
from datetime import datetime


@dataclass
class Manufacturer:
    name: str
    last_payment_date: datetime
    balance_due: int
    id: Optional[int] = None

    def add_to_balance(self, amount):
        self.balance_due += amount

    def format_currency_balance(self):
        return "£{0:,.2f}".format(self.balance_due / 100)

    def format_date_for_psql(self):
        return self.last_payment_date.strftime("%Y-%m-%d")

    def format_date_for_view(self):
        return self.last_payment_date.strftime("%d %B %Y")

    @staticmethod
    def form_date_to_datetime(form_date):
        year, month, day = map(int, form_date.split("-"))
        return datetime(year, month, day)
