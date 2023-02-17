from dataclasses import dataclass
from typing import Optional
from models.yarn import Yarn

@dataclass
class Colour:
    name: str
    hex_code: str
    stock_quantity: int
    yarn: Yarn
    id: Optional[int] = None

    def increase_stock(self, quantity):
        self.stock += quantity
