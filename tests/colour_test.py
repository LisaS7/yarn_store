import unittest

from models.colour import Colour
from models.yarn import Yarn


class TestColour(unittest.TestCase):
    def setUp(self):
        self.yarn = Yarn()
        self.colour = Colour("Caron Cakes", "#111217", 12, self.yarn, 3)

    def test_colour_has_name(self):
        self.assertEqual(self.colour.name, "Caron Cakes")