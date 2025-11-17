from src.models.field import Field
from src.models.error import InvalidArgumentsError


class Name(Field):
    def __init__(self, name):
        if type(name) != str:
            raise InvalidArgumentsError(f"Name must be a string")
        name = name.strip()
        super().__init__(name)
