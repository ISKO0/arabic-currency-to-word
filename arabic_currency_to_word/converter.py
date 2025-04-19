from .currencies import currencies
from .models import Currency

# تبسيط تحويل الرقم إلى كلمات عربية (مستوى أساسي للتجربة)
def number_to_arabic_words(number):
    ones = ["", "واحد", "اثنان", "ثلاثة", "أربعة", "خمسة", "ستة", "سبعة", "ثمانية", "تسعة"]
    teens = ["", "أحد عشر", "اثنا عشر", "ثلاثة عشر", "أربعة عشر", "خمسة عشر",
             "ستة عشر", "سبعة عشر", "ثمانية عشر", "تسعة عشر"]
    tens = ["", "عشرة", "عشرون", "ثلاثون", "أربعون", "خمسون",
            "ستون", "سبعون", "ثمانون", "تسعون"]
    hundreds = ["", "مائة", "مائتان", "ثلاثمائة", "أربعمائة", "خمسمائة",
                "ستمائة", "سبعمائة", "ثمانمائة", "تسعمائة"]

    if number == 0:
        return "صفر"

    def _below_100(n):
        if n < 10:
            return ones[n]
        elif 10 < n < 20:
            return teens[n - 10]
        elif n == 10:
            return "عشرة"
        else:
            u = n % 10
            t = n // 10
            if u == 0:
                return tens[t]
            return f"{ones[u]} و {tens[t]}"

    def _below_1000(n):
        h = n // 100
        r = n % 100
        parts = []
        if h:
            parts.append(hundreds[h])
        if r:
            parts.append(_below_100(r))
        return " و ".join(parts)

    parts = []

    millions = number // 1_000_000
    if millions:
        if millions == 1:
            parts.append("مليون")
        elif millions == 2:
            parts.append("مليونان")
        elif 3 <= millions <= 10:
            parts.append(f"{_below_1000(millions)} ملايين")
        else:
            parts.append(f"{number_to_arabic_words(millions)} مليون")
        number %= 1_000_000

    thousands = number // 1_000
    if thousands:
        if thousands == 1:
            parts.append("ألف")
        elif thousands == 2:
            parts.append("ألفان")
        elif 3 <= thousands <= 10:
            parts.append(f"{_below_1000(thousands)} آلاف")
        else:
            parts.append(f"{number_to_arabic_words(thousands)} ألف")
        number %= 1_000

    if number:
        parts.append(_below_1000(number))

    return " و ".join(parts)


def number_to_english_words(number):
    import inflect
    p = inflect.engine()
    return p.number_to_words(number).replace("-", " ")

class NumberToWord:
    @staticmethod
    def to_word(number, currency_code='SAR', language='Arabic'):
        currency: Currency = currencies.get(currency_code)
        if not currency:
            currency = Currency(
                code=currency_code,
                singular=f"عملة {currency_code}",
                dual=f"عملتان {currency_code}",
                plural=f"عملات {currency_code}",
                fraction_singular="جزء",
                fraction_dual="جزءان",
                fraction_plural="أجزاء",
                part_precision=2,
                en_name=f"{currency_code} Currency",
                en_fraction_name="subunit"
            )

        integer_part = int(number)
        decimal_part = int(round((float(number) - integer_part) * (10 ** currency.part_precision)))

        if language.lower() == "arabic":
            result = ""
            if integer_part == 1:
                result += currency.singular
            elif integer_part == 2:
                result += currency.dual
            elif 3 <= integer_part <= 10:
                result += f"{number_to_arabic_words(integer_part)} {currency.plural}"
            else:
                result += f"{number_to_arabic_words(integer_part)} {currency.singular}"

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

        elif language.lower() == "english":
            result = ""
            int_words = number_to_english_words(integer_part).capitalize()
            dec_words = number_to_english_words(decimal_part)
            result += f"{int_words} {currency.en_name}"
            if decimal_part > 0:
                result += f" and {dec_words} {currency.en_fraction_name}"
            result += " only."
            return result

        else:
            return str(number)

def to_word(number, currency_code='SAR', language='Arabic'):
    return NumberToWord.to_word(number, currency_code, language)
