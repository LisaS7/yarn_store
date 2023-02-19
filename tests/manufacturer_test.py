import unittest
from datetime import datetime as dt
from tests.test_data import test_manufacturer


class TestManufacturer(unittest.TestCase):
    def setUp(self):
        self.manufacturer = test_manufacturer

    def test_mfr_has_name(self):
        self.assertEqual(self.manufacturer.name, "Caron")

    def test_mfr_has_last_payment_date(self):
        self.assertEqual(self.manufacturer.last_payment_date, dt(2023, 1, 12))

    def test_mfr_has_balance_due(self):
        self.assertEqual(self.manufacturer.balance_due, 10050)

    def test_mfr_has_id(self):
        self.assertEqual(self.manufacturer.id, 2)

    def test_mfr_format_currency(self):
        self.assertEqual(self.manufacturer.format_currency_balance(), "£100.50")

    def test_mfr_format_date_for_psql(self):
        self.assertEqual(self.manufacturer.format_date_for_psql(), "2023-01-12")

    def test_mfr_format_date_for_view(self):
        self.assertEqual(self.manufacturer.format_date_for_view(), "12 January 2023")

    def test_mfr_form_date_to_datetime(self):
        dt_date = self.manufacturer.form_date_to_datetime("2023-01-12")
        self.assertEqual(dt_date, dt(2023, 1, 12))
