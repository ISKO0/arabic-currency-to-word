import unittest
from arabic_currency_to_word import to_word

class TestArabicCurrencyToWord(unittest.TestCase):

    def test_basic_numbers_ar(self):
        self.assertEqual(
            to_word(1, currency_code="SAR", language="Arabic"),
            "ريال لا غير."
        )
        self.assertEqual(
            to_word(2, currency_code="SAR", language="Arabic"),
            "ريالان لا غير."
        )
        self.assertEqual(
            to_word(5, currency_code="SAR", language="Arabic"),
            "خمسة ريالات لا غير."
        )

    def test_teens_ar(self):
        self.assertEqual(
            to_word(11, currency_code="SAR", language="Arabic"),
            "أحد عشر ريال لا غير."
        )
        self.assertEqual(
            to_word(19, currency_code="SAR", language="Arabic"),
            "تسعة عشر ريال لا غير."
        )

    def test_thousands_ar(self):
        self.assertEqual(
            to_word(1000, currency_code="SAR", language="Arabic"),
            "ألف ريال لا غير."
        )
        self.assertEqual(
            to_word(2500, currency_code="SAR", language="Arabic"),
            "ألفان و خمسمائة ريال لا غير."
        )

    def test_mixed_decimal_ar(self):
        self.assertEqual(
            to_word(1234.56, currency_code="SAR", language="Arabic"),
            "ألف و مائتان و أربعة و ثلاثون ريال و ستة و خمسون هللة لا غير."
        )

    def test_unknown_currency(self):
        self.assertIn("عملة ZZZ", to_word(2.50, currency_code="ZZZ", language="Arabic"))

    def test_english_output(self):
        self.assertEqual(
            to_word(5.25, currency_code="USD", language="English"),
            "Five US Dollar and twenty five cent only."
        )

if __name__ == "__main__":
    unittest.main()
