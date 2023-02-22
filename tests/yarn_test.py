# REFERENCE: https://stackoverflow.com/questions/18249949/python-file-object-to-flasks-filestorage

from werkzeug.datastructures import FileStorage
import unittest
import filecmp
from pathlib import Path
from tests.test_data import test_yarn, test_manufacturer
from models.yarn import Yarn


class TestYarn(unittest.TestCase):
    def setUp(self):
        self.yarn = test_yarn
        self.saved_image_location = (
            Path.cwd() / "static" / "images" / "yarns" / "test_image.jpeg"
        )

    def tearDown(self):
        if self.saved_image_location.exists():
            self.saved_image_location.unlink()

    def test_yarn_has_name(self):
        expected = "Caron Cakes"
        actual = self.yarn.name
        self.assertEqual(expected, actual)

    def test_yarn_has_manufacturer(self):
        expected = test_manufacturer
        actual = self.yarn.manufacturer
        self.assertEqual(expected, actual)

    def test_yarn_has_yarn_weight(self):
        expected = "DK"
        actual = self.yarn.yarn_weight
        self.assertEqual(expected, actual)

    def test_yarn_has_ball_weight(self):
        expected = 200
        actual = self.yarn.ball_weight_grams
        self.assertEqual(expected, actual)

    def test_yarn_has_length(self):
        expected = 350
        actual = self.yarn.length_metres
        self.assertEqual(expected, actual)

    def test_yarn_has_needle_size(self):
        expected = 5
        actual = self.yarn.needle_size_mm
        self.assertEqual(expected, actual)

    def test_yarn_has_fibre_type(self):
        expected = "20% wool, 80% acrylic"
        actual = self.yarn.fibre_type
        self.assertEqual(expected, actual)

    def test_yarn_has_buy_cost(self):
        expected = 750
        actual = self.yarn.buy_cost
        self.assertEqual(expected, actual)

    def test_yarn_has_sell_price(self):
        expected = 999
        actual = self.yarn.sell_price
        self.assertEqual(expected, actual)

    def test_yarn_has_profit(self):
        expected = 249
        actual = self.yarn.profit
        self.assertEqual(expected, actual)

    def test_yarn_has_id(self):
        expected = 7
        actual = self.yarn.id
        self.assertEqual(expected, actual)

    def test_yarn_total_cost(self):
        expected = 3750
        actual = self.yarn.total_cost(5)
        self.assertEqual(expected, actual)

    def test_yarn_default_image(self):
        expected = "none.jpeg"
        new_yarn = Yarn(
            "Caron Cakes",
            test_manufacturer,
            "DK",
            200,
            350,
            5,
            "20% wool, 80% acrylic",
            750,
            999,
            id=7,
        )
        actual = new_yarn.image
        self.assertEqual(expected, actual)

    def test_save_image(self):
        test_image_location = Path.cwd() / "tests" / "test_image.jpeg"
        with open(test_image_location, "rb") as f:
            image = FileStorage(f)
            image.filename = "test_image.jpeg"
            self.yarn.save_image(image)
        self.assertTrue(filecmp.cmp(test_image_location, self.saved_image_location))
        self.assertEqual(image.filename, self.yarn.image)

    def test_no_image(self):
        no_image = FileStorage()
        self.yarn.save_image(no_image)
        expected = "none.jpeg"
        actual = self.yarn.image
        self.assertEqual(expected, actual)

    def test_format_currency(self):
        expected = "£7.50"
        actual = self.yarn.format_currency(self.yarn.buy_cost)
        self.assertEqual(expected, actual)
