from src.models.name import Name
from src.models.birthday import Birthday
from src.models.error import (
    DuplicatePhoneNumberError,
    InvalidArgumentsError,
    PhoneNumberNotFoundError,
)
from src.models.phone import Phone


class Record:
    def __init__(self, name: str):
        try:
            self.name = Name(name)
        except InvalidArgumentsError:
            raise
        self.phones = []
        self._birthday = None

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}{", birthday: " + self.birthday.value if self.birthday else ""}"

    def add_phone(self, phone: str):
        try:
            ph = Phone(phone)
            if ph:
                for p in self.phones:
                    if p.value == ph.value:
                        raise DuplicatePhoneNumberError(
                            f"Contact {self.name} already has the telephone number {phone}."
                        )
                self.phones.append(ph)
        except (InvalidArgumentsError, DuplicatePhoneNumberError):
            raise
        except Exception:
            raise

    def edit_phone(self, old_phone, new_phone):
        if not old_phone or not new_phone or old_phone == new_phone:
            raise InvalidArgumentsError("Phone numbers entered incorrectly.")
        [index] = [i for i, p in enumerate(self.phones) if p.value == old_phone]
        self.phones[index] = Phone(new_phone)

    def find_phone(self, phone):
        if not phone:
            raise InvalidArgumentsError("Phone numbers entered incorrectly.")
        for p in self.phones:
            if p.value == phone:
                return p.value
        raise PhoneNumberNotFoundError("Phone number not found.")

    def find_all_phones(self):
        if len(self.phones) > 0:
            return f"Phones: {'; '.join(p.value for p in self.phones)}"
        return None

    def remove_phone(self, phone):
        if not phone or len(phone) != 10:
            raise InvalidArgumentsError("Phone numbers entered incorrectly.")
        [index] = [i for i, p in enumerate(self.phones) if p.value == phone]
        del self.phones[index]
        return phone

    @property
    def birthday(self):
        return self._birthday

    @birthday.setter
    def birthday(self, birthday):
        self._birthday = Birthday(birthday)
