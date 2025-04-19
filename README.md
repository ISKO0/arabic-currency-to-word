# 🧮 arabic-currency-to-word

A powerful Python library for converting numbers and currency values into accurate Arabic (and English) words with full grammatical correctness.

## ✅ Features

- Convert numbers into **Arabic or English words**
- Support for **singular, dual, plural** currency forms
- Full Arabic grammar: مذكر/مؤنث، مفرد/جمع، الأرقام فوق المليون والمليار
- Multi-currency support (SAR, AED, SYP, USD, etc.)
- Intelligent handling of **fractions and decimal parts**
- Ready to be used in financial documents, invoices, or Odoo systems

## 📦 Installation

```bash
pip install git+https://github.com/ISKO0/arabic-currency-to-word.git
```

## 🚀 Example Usage

```python
from arabic_currency_to_word import to_word

result = to_word(1234.56, currency_code='SAR', language='Arabic')
print(result)
# → فقط ألف و مائتان و أربعة و ثلاثون ريال سعودي و ستة و خمسون هللة لا غير.
```

## 🔤 Supported Languages

- Arabic 🇸🇦
- English 🇬🇧

## ⚠️ Limitations

- Only Arabic and English are supported.
- Currency definitions must be preconfigured (but you can add more).
- No TTS support (you can integrate reshaping & bidi manually for display).


## 🚀 Example Usage

```python
from arabic_currency_to_word import to_word

# Basic Arabic usage with default settings (SAR)
print(to_word(123.45))
# → فقط مائة و ثلاثة و عشرون ريال سعودي و خمسة و أربعون هللة لا غير.

# Arabic with manual currency definitions (دينار + فلس)
print(to_word(
    number=2.75,
    currency_code='JOD',  # Jordanian Dinar
    language='Arabic'
))
# → فقط ديناران و خمسة و سبعون فلساً لا غير.

# English usage with currency
print(to_word(
    number=99.99,
    currency_code='USD',
    language='English'
))
# → Ninety-nine US Dollars and ninety-nine cents only.

# Full customization with user-defined currency (fictional)
custom_currency = {
    "code": "XYZ",
    "singular": "نقطة",
    "dual": "نقطتان",
    "plural": "نقاط",
    "fraction_singular": "جزء",
    "fraction_dual": "جزءان",
    "fraction_plural": "أجزاء"
}

# Using a custom Currency object (optional if supported in wrapper)
from arabic_currency_to_word.converter import Currency, NumberToWord
currency_obj = Currency(
    code="XYZ",
    singular="نقطة",
    dual="نقطتان",
    plural="نقاط",
    fraction_singular="جزء",
    fraction_dual="جزءان",
    fraction_plural="أجزاء"
)

print(NumberToWord.to_word(10.50, currency_code='XYZ', language='Arabic'))
# → عشر نقاط و خمسون جزءاً لا غير.
```
