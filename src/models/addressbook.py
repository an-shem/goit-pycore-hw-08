from collections import UserDict
from datetime import datetime
from src.models.error import (
    DuplicatePhoneNumberError,
    InvalidArgumentsError,
)
from src.models.record import Record


class AddressBook(UserDict):
    def add_record(self, record: Record):
        if not isinstance(record, Record):
            raise ValueError(
                "In AddressBook, you can append only an object of the Record class."
            )
        name_key = record.name.value
        if not name_key:
            raise ValueError("You cannot add a contact without a name to AddressBook.")
        if name_key in self.data:
            raise DuplicatePhoneNumberError("Contact with that name already exists.")
        self.data[name_key] = record
        return self.data[name_key]

    def find(self, name):
        if not name in self.data:
            return None
        return self.data[name]

    def delete(self, name):
        if not name:
            raise InvalidArgumentsError("Name entered incorrectly.")
        if name in self.data:
            contact = self.data[name]
            del self.data[name]
            return contact

    def get_upcoming_birthdays(self, interval=7):
        res = []
        today = datetime.today().date()

        for contact in self.data.values():
            user_birthday_datetime = datetime.strptime(
                contact.birthday.value, "%d.%m.%Y"
            ).date()
            birthday_this_year = user_birthday_datetime.replace(year=today.year)

            if 0 <= ((birthday_this_year - today).days) < interval:
                res.append(
                    {
                        "name": contact.name.value,
                        "congratulation_date": birthday_this_year.strftime("%d.%m.%Y"),
                    }
                )
        return sorted(res, key=lambda contact: contact["congratulation_date"])
