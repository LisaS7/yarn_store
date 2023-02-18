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

    @staticmethod
    def save_image(image):
        if not image:
            image = "none.jpeg"
        else:
            image.save("./static/images/yarns/" + image.filename)
