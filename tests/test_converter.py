from arabic_currency_to_word import currency_to_arabic_words

def test_simple_case():
    result = currency_to_arabic_words(
        number=3.75,
        original_number="3.75",
        currency_forms={"singular": "دينار", "dual": "ديناران", "plural": "دنانير"},
        fraction_forms={"singular": "فلس", "dual": "فلسان", "plural": "فلوس"}
    )
    assert "دنانير" in result
    assert "خمسة و سبعون" in result or "خمسة وسبعون" in result
