from ab_classes import AddressBook, Name, Phone, Record, ControlBot


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
    return wrapper


def main():
    while True:
        user_input = input(">>>")
        if user_input:
            command, data = parser(user_input)
            result = command(*data)
            if result:
                if result == "Good bye!":
                    print(result)
                    break
                print(result)
            continue
        else:
            print(ControlBot.no_command())


def parser(text: str): #-> tuple[callable, tuple[str] | None]:

    if text:
        text1 = text.lower()
        if text1.startswith("add"):
            return Record.add, text1.replace("add", "").strip().split()
        if text1.startswith("hello"):
            return ControlBot.hello, "How can I help you?"
        if text1.startswith("close") or text1.startswith("exit") or text1.startswith("good bye"):
            return ControlBot.exit, "Good bye!"
        if text1.startswith("show all"):
            return RequestContacts.show_all, 'show all'
        if text1.startswith("phone"):
            return RequestContacts.get_phone, text.replace("phone", "").strip().split()
        if text1.startswith("change"):
            return Record.change, text.replace("change", "").strip().split()
        else:
            return ControlBot.no_command, ''
    else:
        return ControlBot.no_command, ''


@input_error
def add(*args):
    if len(args) == 2:
        name = Name(args[0])
        phone = Phone(args[1])
        rec = Record(name, phone)
    if len(args) > 2:
        phone = []
        name = Name(args[0])
        for i in range(1, len(args)):
            phone.append(Phone(args[i]))
        rec = Record(name, phone)
    AddressBook.ab[name] = phone
    AddressBook.cotacts.append(rec)

    return f"Add success {name} {phone}"

def change(*args):
    name = Name(args[0])
    phone_old = Phone(args[1])
    phone_new = Phone(args[2])
    AddressBook.ab[name] = phone_new
    return f"Change success {name} from {phone_old} to {phone_new}"


class RequestContacts:

    @input_error
    def get_phone(*args):
        name = args[0]
        return f"User:{name}  Phone: {AddressBook.ab[name]}"

    def show_all(*args):
        [print(f"Name contact: {key}  Phone number: {value}", end="\n") for key,
         value in AddressBook.ab.items()]
        return

 

if __name__ == "__main__":
    main()

