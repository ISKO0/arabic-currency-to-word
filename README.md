# arabic-currency-to-word
Convert numbers and currency amounts into accurate Arabic words with full linguistic support.
A Python library to convert numeric values and currency amounts into fully accurate Arabic words.

Requirements: Python 3.6+


✅ Features:
- Converts both integer and decimal numbers to Arabic words.
- Full support for Arabic currency forms: singular, dual, and plural.
- Supports Arabic currencies like: ريال (Riyal), دينار (Dinar), درهم (Dirham), جنيه (Pound), دولار (Dollar), and more.
- Handles currency fractions like: هللة (Halala), فلس (Fils), قرش (Qirsh), سنت (Cent).
- Supports negative numbers and produces grammatically correct Arabic.
- Accurate handling of decimals using the original number string to avoid floating point issues.
- Fully customizable for any new currency or fraction format.

📦 Installation:
pip install arabic-currency-to-word

🚀 Example Usage:
from arabic_currency_to_word import currency_to_arabic_words

result = currency_to_arabic_words(
    number=2.75,
    original_number="2.75",
    currency_forms={
        "singular": "دينار",
        "dual": "ديناران",
        "plural": "دنانير"
    },
    fraction_forms={
        "singular": "فلس",
        "dual": "فلسان",
        "plural": "فلوس"
    }
)

print(result)
# Output: ديناران و خمسة و سبعون فلس
