from dataclasses import dataclass
from models.manufacturer import Manufacturer
from typing import Optional


@dataclass
class Yarn:
    name: str
    manufacturer: Manufacturer
    yarn_weight: str
    ball_weight_grams: int
    length_metres: int
    needle_size_mm: float
    fibre_type: str
    buy_cost: int
    sell_price: int
    image: Optional[str] = "none.jpeg"
    id: Optional[int] = None

    def __post_init__(self):
        profit = (self.sell_price - self.buy_cost) / self.buy_cost
        self.margin = "{0:.0%}".format(profit)

    def save_image(self, image):
        if not image.filename:
            self.image = "none.jpeg"
        else:
            image.save("./static/images/yarns/" + image.filename)
            self.image = image.filename

    @staticmethod
    def format_currency(value):
        return "£{0:,.2f}".format(value / 100)
