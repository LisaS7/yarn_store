import unittest
from models.manufacturer import Manufacturer
from datetime import datetime as dt

from werkzeug.datastructures import FileStorage

class TestManufacturer(unittest.TestCase):
    def setUp(self):
        self.manufacturer = Manufacturer("Caron", dt(2023, 1, 12), 10050, "caron.jpeg")

    def test_mfr_has_name(self):
        self.assertEqual(self.manufacturer.name, "Caron")

    def test_mfr_has_last_payment_date(self):
        self.assertEqual(self.manufacturer.last_payment_date, dt(2023, 1, 12))
    
    def test_mfr_has_balance_due(self):
        self.assertEqual(self.manufacturer.balance_due, 10050)

    def test_mfr_has_logo(self):
        self.assertEqual(self.manufacturer.logo, "caron.jpeg")

    def test_mfr_format_currency(self):
        self.assertEqual(self.manufacturer.format_currency_balance(), "£100.50")