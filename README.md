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
- English (United States 🇺🇸)

## ⚠️ Limitations

- Only Arabic and English are supported.
- Currency definitions must be preconfigured (but you can add more).
- No TTS support (you can integrate reshaping & bidi manually for display).
