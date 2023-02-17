import unittest

from tests.test_data import test_colour, test_yarn


class TestColour(unittest.TestCase):
    def setUp(self):
        self.colour = test_colour

    def test_colour_has_name(self):
        self.assertEqual(self.colour.name, "Caron Cakes")

    def test_colour_has_hex_code(self):
        self.assertEqual(self.colour.hex_code, "#111217")

    def test_colour_has_stock_quantity(self):
        self.assertEqual(self.colour.stock_quantity, 12)

    def test_colour_has_yarn(self):
        self.assertEqual(self.colour.yarn, test_yarn)

    def test_colour_has_id(self):
        self.assertEqual(self.colour.id, 3)

    def test_increase_stock(self):
        self.colour.increase_stock(5)
        self.assertEqual(self.colour.stock_quantity, 17)