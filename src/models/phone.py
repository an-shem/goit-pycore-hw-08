import re
from src.models.field import Field
from src.models.error import InvalidArgumentsError


class Phone(Field):
    def __init__(self, phone):
        phone = phone.strip()
        pattern = r"^\d{10}$"
        if not re.fullmatch(pattern, phone):
            raise InvalidArgumentsError(
                f"The number '{phone}' is invalid! It must be 10 characters (numbers) long."
            )
        super().__init__(phone)
