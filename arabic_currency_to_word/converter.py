from .currencies import currencies

def number_to_arabic_words(number):
    if number == 0:
        return "صفر"
    ones = ["", "واحد", "اثنان", "ثلاثة", "أربعة", "خمسة", "ستة", "سبعة", "ثمانية", "تسعة"]
    tens = ["", "عشرة", "عشرون", "ثلاثون", "أربعون", "خمسون", "ستون", "سبعون", "ثمانون", "تسعون"]
    words = []
    if number < 10:
        words.append(ones[number])
    elif number < 100:
        words.append(ones[number % 10])
        if number % 10 != 0:
            words.append("و")
        words.append(tens[number // 10])
    else:
        words.append(str(number))  # fallback
    return " ".join([w for w in words if w])

class Currency:
    def __init__(self, code, singular, dual, plural, fraction_singular, fraction_dual, fraction_plural, part_precision=2):
        self.code = code
        self.singular = singular
        self.dual = dual
        self.plural = plural
        self.fraction_singular = fraction_singular
        self.fraction_dual = fraction_dual
        self.fraction_plural = fraction_plural
        self.part_precision = part_precision

class NumberToWord:
    @staticmethod
    def to_word(number, currency_code='SAR', language='Arabic'):
        currency = currencies.get(currency_code)
        if not currency:
            currency = Currency(currency_code, f"عملة {currency_code}", f"عملتان {currency_code}",
                                f"عملات {currency_code}", "جزء", "جزءان", "أجزاء")

        integer_part = int(number)
        decimal_part = int(round((float(number) - integer_part) * (10 ** currency.part_precision)))

        result = ""

        if language == "Arabic":
            # الجزء الصحيح
            if integer_part == 1:
                result += currency.singular
            elif integer_part == 2:
                result += currency.dual
            elif 3 <= integer_part <= 10:
                result += f"{number_to_arabic_words(integer_part)} {currency.plural}"
            else:
                result += f"{number_to_arabic_words(integer_part)} {currency.singular}"

            # الجزء العشري
            if decimal_part > 0:
                result += " و "
                if decimal_part == 1:
                    result += currency.fraction_singular
                elif decimal_part == 2:
                    result += currency.fraction_dual
                elif 3 <= decimal_part <= 10:
                    result += f"{number_to_arabic_words(decimal_part)} {currency.fraction_plural}"
                else:
                    result += f"{number_to_arabic_words(decimal_part)} {currency.fraction_singular}"

            result += " لا غير."
            return result
        else:
            return f"{integer_part} {currency_code} and {decimal_part} subunits"

def to_word(number, currency_code='SAR', language='Arabic'):
    return NumberToWord.to_word(number, currency_code, language)
