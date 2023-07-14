from ab_classes_new import AddressBook, Name, Phone, Record

address_book = AddressBook()


def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except IndexError:
            print("Give me a name one phone number or several phone numbers please")
        except TypeError:
            print("Give me a name one phone number or several phone numbers please")
        except UnboundLocalError:
            print("Give me a name one phone number or several phone numbers please")
        except ValueError:
            print("Give me a name one phone number or several phone numbers please")
        except AttributeError:
            print("Give me a name one phone number or several phone numbers please")
    return wrapper


@input_error
def add_contact(*args):
    name = Name(args[0])
    phone = Phone(args[1])
    rec: Record = address_book.get(str(name))
    if rec:
        return rec.add_phone(phone)
    rec = Record(name, phone)
    return address_book.add_record(rec)

# змінити


@input_error
def change_phone(*args):
    name = Name(args[0])
    old_phone = Phone(args[1])
    new_phone = Phone(args[2])
    rec: Record = address_book.get(str(name))
    print(rec)
    if rec:
        return rec.change_phone(old_phone, new_phone)
    return f"No contact {name} in address book"

# показати контакт


@input_error
def get_phone(*args):
    name = Name(args[0])
    # return f"User {name.value}"
    return f"User {address_book.get(str(name))}"

# Привіт


def hello(*args):
    return "How can I help you?"

# Вийти


def exit_command(*args):
    return "Good bye!"

# Невідома команда пуста команда


def no_command(*args, **kwargs):
    return "Unknown command"

# показати все


def show_all_command(*args):
    return address_book


# Команди додати, змінити, вихід, показати все, показати контакт
COMMANDS = {
    add_contact: ("add", "+"),
    change_phone: ("change", "зміни"),
    exit_command: ("good bye", "bye", "exit", "end", "close"),
    show_all_command: ("show all", "show"),
    get_phone: ("phone",)
}


def parser(text: str):
    for cmd, kwds in COMMANDS.items():
        for kwd in kwds:
            if text.lower().startswith(kwd):
                data = text[len(kwd):].strip().split()
                return cmd, data
    return no_command, []


def main():
    while True:
        user_input = input(">>>")
        cmd, data = parser(user_input)
        result = cmd(*data)
        print(result)
        if cmd == exit_command:
            break


if __name__ == "__main__":
    main()
