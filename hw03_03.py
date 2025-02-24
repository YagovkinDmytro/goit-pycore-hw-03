import re

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

def normalize_phone(phone_number):
    pattern = r"\D"
    replacement = r""
    formatted_phone = re.sub(pattern, replacement, phone_number)
    if len(formatted_phone) == 12:
        formatted_phone = "+" + formatted_phone
    elif len(formatted_phone) == 10:
        formatted_phone = "+38" + formatted_phone
    elif len(formatted_phone) == 11:
        formatted_phone = "+3" + formatted_phone
    elif len(formatted_phone) == 9:
        formatted_phone = "+380" + formatted_phone
    else:
        formatted_phone = f"Номер телефону некоректний: {phone_number}"
    return formatted_phone

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)