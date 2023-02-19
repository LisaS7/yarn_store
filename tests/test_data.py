from models.yarn import Yarn
from models.colour import Colour
from models.manufacturer import Manufacturer
from datetime import datetime as dt

test_manufacturer = Manufacturer("Caron", dt(2023, 1, 12), 10050, 2)

test_yarn = Yarn(
    "Caron Cakes",
    test_manufacturer,
    "DK",
    200,
    350,
    5,
    "20% wool, 80% acrylic",
    750,
    999,
    "test_image.jpeg",
    7,
)

test_colour = Colour("Caron Cakes", "#111217", 12, test_yarn, 3)
