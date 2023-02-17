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
    image: Optional[str] = None
    id: Optional[int] = None

    def save_image(self, image):
        if not image:
            image = "none.jpeg"
        else:
            image.save("./static/images/yarns/" + image.filename)
