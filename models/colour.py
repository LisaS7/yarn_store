from dataclasses import dataclass
from typing import Optional
from models.yarn import Yarn
from config.config import config


@dataclass
class Colour:
    name: str
    hex_code: str
    stock_quantity: int
    yarn: Yarn
    id: Optional[int] = None

    def low_stock(self):
        config.get_stock_threshold()
        return self.stock_quantity < config.low_stock_threshold

    def increase_stock(self, quantity):
        self.stock_quantity += quantity

    def total_cost(self, quantity):
        return quantity * self.yarn.buy_cost
