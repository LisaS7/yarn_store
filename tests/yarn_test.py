# REFERENCE: https://stackoverflow.com/questions/18249949/python-file-object-to-flasks-filestorage

from werkzeug.datastructures import FileStorage
import unittest
import filecmp
from pathlib import Path
from tests.test_data import test_yarn, test_manufacturer


class TestYarn(unittest.TestCase):
    def setUp(self):
        self.yarn = test_yarn
        self.test_image_location = Path.cwd() / "tests" / "test_image.jpeg"
        self.saved_image_location = (
            Path.cwd() / "static" / "images" / "yarns" / "test_image.jpeg"
        )

    def tearDown(self):
        if self.saved_image_location.exists():
            self.saved_image_location.unlink()

    def test_yarn_has_name(self):
        self.assertEqual(self.yarn.name, "Caron Cakes")

    def test_yarn_has_manufacturer(self):
        self.assertEqual(self.yarn.manufacturer, test_manufacturer)

    def test_yarn_has_yarn_weight(self):
        self.assertEqual(self.yarn.yarn_weight, "DK")

    def test_yarn_has_ball_weight(self):
        self.assertEqual(self.yarn.ball_weight_grams, 200)

    def test_yarn_has_length(self):
        self.assertEqual(self.yarn.length_metres, 350)

    def test_yarn_has_needle_size(self):
        self.assertEqual(self.yarn.needle_size_mm, 5)

    def test_yarn_has_fibre_type(self):
        self.assertEqual(self.yarn.fibre_type, "20% wool, 80% acrylic")

    def test_yarn_has_buy_cost(self):
        self.assertEqual(self.yarn.buy_cost, 750)

    def test_yarn_has_sell_price(self):
        self.assertEqual(self.yarn.sell_price, 999)

    def test_yarn_has_image(self):
        self.assertEqual(self.yarn.image, "test_image.jpeg")

    def test_yarn_has_id(self):
        self.assertEqual(self.yarn.id, 7)

    def test_save_image(self):
        with open(self.test_image_location, "rb") as f:
            image = FileStorage(f)
            image.filename = "test_image.jpeg"
            self.yarn.save_image(image)
        self.assertTrue(
            filecmp.cmp(self.test_image_location, self.saved_image_location)
        )
