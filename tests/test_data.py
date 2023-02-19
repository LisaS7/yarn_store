from models.yarn import Yarn
from models.colour import Colour
from models.manufacturer import Manufacturer
from datetime import datetime as dt
from decimal import Decimal

test_manufacturer = Manufacturer("Caron", dt(2023, 1, 12), Decimal(100.50), 2)

test_yarn = Yarn(
    "Caron Cakes",
    test_manufacturer,
    "DK",
    200,
    350,
    5,
    "20% wool, 80% acrylic",
    Decimal(7.50),
    Decimal(9.99),
    "test_image.jpeg",
    7,
)

test_colour = Colour("Caron Cakes", "#111217", 12, test_yarn, 3)
