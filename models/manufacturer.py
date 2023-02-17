from dataclasses import dataclass
from typing import Optional
from datetime import datetime


@dataclass
class Manufacturer:
    name: str
    last_payment_date: datetime
    balance_due: int
    logo: str

    def format_currency_balance(self):
        pass

    def save_logo(self):
        pass