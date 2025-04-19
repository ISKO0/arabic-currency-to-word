from .currencies import currencies
from .models import Currency

# تبسيط تحويل الرقم إلى كلمات عربية (مستوى أساسي للتجربة)
def number_to_arabic_words(number):
    ones = ["", "واحد", "اثنان", "ثلاثة", "أربعة", "خمسة", "ستة", "سبعة", "ثمانية", "تسعة"]
    tens = ["", "عشرة", "عشرون", "ثلاثون", "أربعون", "خمسون", "ستون", "سبعون", "ثمانون", "تسعون"]

    if number == 0:
        return "صفر"
    if number < 10:
        return ones[number]
    if number < 100:
        u = number % 10
        t = number // 10
        if u == 0:
            return tens[t]
        return f"{ones[u]} و {tens[t]}"
    if number < 1000:
        h = number // 100
        r = number % 100
        h_word = ones[h] + " مائة" if h > 1 else "مائة"
        return f"{h_word}" + (f" و {number_to_arabic_words(r)}" if r else "")
    if number < 1000000:
        th = number // 1000
        r = number % 1000
        if th == 1:
            th_word = "ألف"
        elif th == 2:
            th_word = "ألفان"
        elif 3 <= th <= 10:
            th_word = f"{number_to_arabic_words(th)} آلاف"
        else:
            th_word = f"{number_to_arabic_words(th)} ألف"
        return f"{th_word}" + (f" و {number_to_arabic_words(r)}" if r else "")
    else:
        m = number // 1000000
        r = number % 1000000
        m_word = f"{number_to_arabic_words(m)} مليون"
        return f"{m_word}" + (f" و {number_to_arabic_words(r)}" if r else "")

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
