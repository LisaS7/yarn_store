from dataclasses import dataclass
from typing import Optional
from models.yarn import Yarn
from config import stock_low_threshold


@dataclass
class Colour:
    name: str
    hex_code: str
    stock_quantity: int
    yarn: Yarn
    id: Optional[int] = None

    def __post_init__(self):
        self.low_stock = self.stock_quantity < stock_low_threshold

    def increase_stock(self, quantity):
        self.stock_quantity += quantity

    def total_cost(self, quantity):
        return quantity * self.yarn.buy_cost
