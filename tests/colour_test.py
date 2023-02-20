import unittest

from tests.test_data import test_colour, test_yarn


class TestColour(unittest.TestCase):
    def setUp(self):
        self.colour = test_colour

    def test_colour_has_name(self):
        expected = "Caron Cakes"
        actual = self.colour.name
        self.assertEqual(expected, actual)

    def test_colour_has_hex_code(self):
        expected = "#111217"
        actual = self.colour.hex_code
        self.assertEqual(expected, actual)

    def test_colour_has_stock_quantity(self):
        expected = 12
        actual = self.colour.stock_quantity
        self.assertEqual(expected, actual)

    def test_colour_has_yarn(self):
        expected = test_yarn
        actual = self.colour.yarn
        self.assertEqual(expected, actual)

    def test_colour_has_id(self):
        expected = 3
        actual = self.colour.id
        self.assertEqual(expected, actual)

    def test_increase_stock(self):
        expected = 17
        self.colour.increase_stock(5)
        actual = self.colour.stock_quantity
        self.assertEqual(expected, actual)
