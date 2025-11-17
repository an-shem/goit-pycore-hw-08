from src.models.error import (
    ContactNotFoundError,
    DuplicatePhoneNumberError,
    InvalidArgumentsError,
    PhoneNumberNotFoundError,
)


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Command or data entered incorrectly"
        except KeyError:
            return "User with this name not found"
        except IndexError:
            return "Give me name please."
        except (
            ContactNotFoundError,
            InvalidArgumentsError,
            DuplicatePhoneNumberError,
            PhoneNumberNotFoundError,
        ) as e:
            return f"Error: {e}"
        except Exception as e:
            return f"Непредвиденная ошибка: {e}"

    return inner
