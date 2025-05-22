import re

phone_number = [
    "    +38(050)123-32-34"
"     0503451234"
"(050)8889900"
"38050-111-22-22"
"38050 111 22 11   "
]


def normalize_phone(phone_number):
    # Видаляємо всі символи, крім цифр
    digits = re.sub(r'\D', '', phone_number)

    # Якщо номер починається з '380', додаємо '+' спереду
    if digits.startswith('380'):
        normalized = '+' + digits
    # Якщо номер починається з '0', додаємо '+38' спереду
    elif digits.startswith('0'):
        normalized = '+38' + digits
    # Якщо номер вже містить правильну кількість цифр (наприклад, 9 цифр без коду)
    elif len(digits) == 9:
        normalized = '+380' + digits
    else:
        # Якщо нічого не підходить — просто повертаємо з +38
        normalized = '+38' + digits

    return normalized