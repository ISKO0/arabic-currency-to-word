# arabic-currency-to-word

A Python library to convert numeric values and currency amounts into fully accurate Arabic words.

### ✅ Features

- Converts both integer and decimal numbers to Arabic words.
- Full support for Arabic currency forms: singular, dual, and plural.
- Supports Arabic currencies like: ريال (Riyal), دينار (Dinar), درهم (Dirham), جنيه (Pound), دولار (Dollar), and more.
- Handles currency fractions like: هللة (Halala), فلس (Fils), قرش (Qirsh), سنت (Cent).
- Supports negative numbers and produces grammatically correct Arabic.
- Accurate handling of decimals using the original number string to avoid floating point issues.
- Fully customizable for any new currency or fraction format.

### 📦 Installation

```bash
pip install arabic-currency-to-word
Or
pip install git+https://github.com/ISKO0/arabic-currency-to-word.git
```

### 🚀 Example Usage

```python
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
```

### 🐍 Requirements

- Python 3.6+

## ⚠️ Limitations

- This library is designed for **Arabic language only** (currently no multi-language support).
- Currency formats must be manually provided (no auto-detection or conversion).
- Does not support **feminine grammatical forms** (e.g., "إحدى" for feminine words).
- Limited to integer and two-digit decimal values only (e.g., 99.99).
- No built-in support for currency formatting (e.g., separators, localization).
- No support for advanced grammatical cases (الإضافة، التمييز، إلخ).
- Not suitable for voice or TTS output directly (requires reshaping and RTL handling separately).

### 📄 License

MIT License
