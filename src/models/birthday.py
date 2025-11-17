from datetime import datetime

from src.models.field import Field


class Birthday(Field):
    def __init__(self, value):
        try:
            if datetime.strptime(value, "%d.%m.%Y"):
                super().__init__(value)
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")
