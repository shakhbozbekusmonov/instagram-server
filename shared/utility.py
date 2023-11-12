import re
from rest_framework.exceptions import ValidationError

email_regex = re.compile(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")
phone_regex = re.compile(r"^[\d\s().-]+$")


def check_email_or_phone(email_or_phone):
    if re.fullmatch(email_regex, email_or_phone):
        email_or_phone = 'email'

    elif re.fullmatch(phone_regex, email_or_phone):
        email_or_phone = 'phone'

    else:
        data = {
            "success": False,
            "message": "Email yoki telefon raqamingiz noto'g'ri."
        }
        raise ValidationError(data)

    return email_or_phone