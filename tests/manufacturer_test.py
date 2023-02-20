import unittest
from datetime import datetime as dt
from tests.test_data import test_manufacturer


class TestManufacturer(unittest.TestCase):
    def setUp(self):
        self.manufacturer = test_manufacturer

    def test_mfr_has_name(self):
        expected = "Caron"
        actual = self.manufacturer.name
        self.assertEqual(expected, actual)

    def test_mfr_has_last_payment_date(self):
        expected = dt(2023, 1, 12)
        actual = self.manufacturer.last_payment_date
        self.assertEqual(expected, actual)

    def test_mfr_has_balance_due(self):
        expected = 10050
        actual = self.manufacturer.balance_due
        self.assertEqual(expected, actual)

    def test_mfr_has_id(self):
        expected = 2
        actual = self.manufacturer.id
        self.assertEqual(expected, actual)

    def test_mfr_format_currency(self):
        expected = "£100.50"
        actual = self.manufacturer.format_currency_balance()
        self.assertEqual(expected, actual)

    def test_mfr_format_date_for_psql(self):
        expected = "2023-01-12"
        actual = self.manufacturer.format_date_for_psql()
        self.assertEqual(expected, actual)

    def test_mfr_format_date_for_view(self):
        expected = "12 January 2023"
        actual = self.manufacturer.format_date_for_view()
        self.assertEqual(expected, actual)

    def test_mfr_form_date_to_datetime(self):
        expected = dt(2023, 1, 12)
        actual = self.manufacturer.form_date_to_datetime("2023-01-12")
        self.assertEqual(expected, actual)
