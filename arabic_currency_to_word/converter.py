class Currency:
    def __init__(self, code, singular, dual, plural, fraction_singular, fraction_dual, fraction_plural):
        self.code = code
        self.singular = singular
        self.dual = dual
        self.plural = plural
        self.fraction_singular = fraction_singular
        self.fraction_dual = fraction_dual
        self.fraction_plural = fraction_plural

class NumberToWord:
    @staticmethod
    def to_word(number, currency_code='SAR', language='Arabic'):
        return f"Converted {number} to {language} words with currency {currency_code}."

def to_word(number, currency_code='SAR', language='Arabic'):
    return NumberToWord.to_word(number, currency_code, language)
