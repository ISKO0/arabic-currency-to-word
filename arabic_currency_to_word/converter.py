def number_to_arabic_words(number):
    if number == 0:
        return 'صفر'
    if number < 0:
        return 'سالب ' + number_to_arabic_words(abs(number))

    ones = {
        1: 'واحد', 2: 'اثنان', 3: 'ثلاثة', 4: 'أربعة', 5: 'خمسة',
        6: 'ستة', 7: 'سبعة', 8: 'ثمانية', 9: 'تسعة', 10: 'عشرة',
        11: 'أحد عشر', 12: 'اثنا عشر', 13: 'ثلاثة عشر', 14: 'أربعة عشر',
        15: 'خمسة عشر', 16: 'ستة عشر', 17: 'سبعة عشر', 18: 'ثمانية عشر', 19: 'تسعة عشر',
    }

    tens = {
        2: 'عشرون', 3: 'ثلاثون', 4: 'أربعون', 5: 'خمسون',
        6: 'ستون', 7: 'سبعون', 8: 'ثمانون', 9: 'تسعون',
    }

    hundreds = {
        1: 'مائة', 2: 'مائتان', 3: 'ثلاثمائة', 4: 'أربعمائة',
        5: 'خمسمائة', 6: 'ستمائة', 7: 'سبعمائة', 8: 'ثمانمائة', 9: 'تسعمائة',
    }

    def two_digit_number(n):
        if n <= 19:
            return ones[n]
        ten = n // 10
        one = n % 10
        if one == 0:
            return tens[ten]
        return f"{ones[one]} و {tens[ten]}"

    def three_digit_number(n):
        h = n // 100
        r = n % 100
        parts = []
        if h > 0:
            parts.append(hundreds[h])
        if r > 0:
            parts.append(two_digit_number(r))
        return ' و '.join(parts)

    def group_name(n, singular, dual, plural):
        if n == 1:
            return singular
        elif n == 2:
            return dual
        elif 3 <= n <= 10:
            return f"{ones[n]} {plural}"
        else:
            return f"{number_to_arabic_words(n)} {singular}"

    parts = []
    billions = number // 1_000_000_000
    if billions:
        parts.append(group_name(billions, 'مليار', 'ملياران', 'مليارات'))
        number %= 1_000_000_000

    millions = number // 1_000_000
    if millions:
        parts.append(group_name(millions, 'مليون', 'مليونان', 'ملايين'))
        number %= 1_000_000

    thousands = number // 1000
    if thousands:
        parts.append(group_name(thousands, 'ألف', 'ألفان', 'آلاف'))
        number %= 1000

    if number:
        parts.append(three_digit_number(number))

    return ' و '.join(parts)


def currency_to_arabic_words(number, original_number=None, currency_forms=None, fraction_forms=None, debug=False):
    if currency_forms is None:
        currency_forms = {"singular": "ريال", "dual": "ريالان", "plural": "ريالات"}
    if fraction_forms is None:
        fraction_forms = {"singular": "هللة", "dual": "هللتان", "plural": "هللات"}

    is_negative = False
    if float(number) < 0:
        is_negative = True
        if original_number and original_number.startswith('-'):
            original_number = original_number[1:]
        number = abs(float(number))

    num_float = float(number)
    int_part = int(num_float)

    if original_number and '.' in original_number:
        decimal_str = original_number.split('.')[1]
        if len(decimal_str) == 1:
            decimal_str += '0'
        decimal_part = int(decimal_str)
    else:
        decimal_part = int(round((num_float - int_part) * 100))

    if decimal_part == 0:
        if int_part == 1:
            result = currency_forms["singular"]
        elif int_part == 2:
            result = currency_forms["dual"]
        else:
            words = number_to_arabic_words(int_part)
            currency_text = currency_forms["plural"] if 3 <= int_part <= 10 else currency_forms["singular"]
            result = f"{words} {currency_text}"
        return f"سالب {result}" if is_negative else result

    if int_part == 0:
        integer_text = ""
    elif int_part == 1:
        integer_text = currency_forms["singular"]
    elif int_part == 2:
        integer_text = currency_forms["dual"]
    elif 3 <= int_part <= 10:
        integer_text = f"{number_to_arabic_words(int_part)} {currency_forms['plural']}"
    else:
        integer_text = f"{number_to_arabic_words(int_part)} {currency_forms['singular']}"

    if decimal_part == 1:
        decimal_text = fraction_forms["singular"]
    elif decimal_part == 2:
        decimal_text = fraction_forms["dual"]
    elif 3 <= decimal_part <= 10:
        decimal_text = fraction_forms["plural"]
    else:
        decimal_text = fraction_forms["singular"]

    if int_part == 0:
        result = decimal_text if decimal_part == 2 else f"{number_to_arabic_words(decimal_part)} {decimal_text}"
    else:
        if decimal_part in (1, 2):
            result = f"{integer_text} و {decimal_text}"
        else:
            result = f"{integer_text} و {number_to_arabic_words(decimal_part)} {decimal_text}"

    return f"سالب {result}" if is_negative else result
