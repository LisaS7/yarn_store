from dataclasses import dataclass
from models.manufacturer import Manufacturer
from typing import Optional
from decimal import Decimal


@dataclass
class Yarn:
    name: str
    manufacturer: Manufacturer
    yarn_weight: str
    ball_weight_grams: int
    length_metres: int
    needle_size_mm: float
    fibre_type: str
    buy_cost: Decimal
    sell_price: Decimal
    image: Optional[str] = None
    id: Optional[int] = None

    def __post_init__(self):
        self.buy_cost = Decimal(self.buy_cost)
        self.sell_price = Decimal(self.sell_price)

    @staticmethod
    def save_image(image):
        if not image:
            image = "none.jpeg"
        else:
            image.save("./static/images/yarns/" + image.filename)

    @staticmethod
    def format_currency(value):
        return "£{0:,.2f}".format(value)
