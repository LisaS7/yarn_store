import unittest

from models.colour import Colour
from models.yarn import Yarn


class TestColour(unittest.TestCase):
    def setUp(self):
        self.yarn = Yarn()
        self.colour = Colour("Caron Cakes", "#111217", 12, self.yarn, 3)

    def test_colour_has_name(self):
        self.assertEqual(self.colour.name, "Caron Cakes")

    def test_colour_has_hex_code(self):
        self.assertEqual(self.colour.hex_code, "#111217")

    def test_colour_has_stock_quantity(self):
        self.assertEqual(self.colour.stock_quantity, 12)

    def test_colour_has_yarn(self):
        self.assertEqual(self.colour.yarn, self.yarn)

    def test_colour_has_id(self):
        self.assertEqual(self.colour.id, 3)

    def test_increase_stock(self):
        self.colour.increase_stock(5)
        self.assertEqual(self.colour.stock_quantity, 17)