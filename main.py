address_book = {}


<<<<<<< HEAD
def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except IndexError:
            print("Give me name and phone please")
        except TypeError:
            print("Give me name and phone please")
        except ValueError:
            print("Give me name and phone please")
    return wrapper


@input_error
def add(*args):
    name = str.capitalize(args[0])
    phone = args[1]
    address_book[str.capitalize(name)] = phone
    return f"Add success {name} {phone}"
=======
class AddressBook(UserDict):
    contacts = []


class Record():

    def add_record(self, *args):
        name = Name(args[0])
        phone = Phone(args[1])
        rec = Record(name, phone)
        print(rec)
        ab.append(rec)
        return ab.add_rec(rec)

    def remove_record(self):
        pass

    def edit_field(self):
        pass

    def save_name(self):
        pass

    def __init__(self, name, num_phone):
        self.name = name
        self.phone = num_phone

    def __repr__(self, records):
        # result = map(str, reсords)
        return "\n".join(str(rec) for rec in records)
        #   return str(.....)
>>>>>>> 1db26908da596147dfca76ef3a11109af2a4d992


@input_error
def change(*args):
    name = str.capitalize(args[0])
    phone = args[1]
    address_book[str.capitalize(name)] = phone
    return f"Change success {str.capitalize(name)} {phone}"


def exit(*args):
    return "Good bye!"


@input_error
def get_phone(*args):
    name = str.capitalize(args[0])
    return f"User:{name}  Phone: {address_book[name]}"


def hello(*args):
    return "How can I help you?"


# @input_error
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
            print(no_command())


def no_command(*args, **kwargs):
    return "Unknown command"


def parser(text: str): #

    if text:
        text1 = text.lower()
        if text1.startswith("add"):
            return add, text1.replace("add", "").strip().split()
        if text1.startswith("hello"):
            return hello, "How can I help you?"
        if text1.startswith("close") or text1.startswith("exit") or text1.startswith("good bye"):
            return exit, "Good bye!"
        if text1.startswith("show all"):
            return show_all, 'show all'
        if text1.startswith("phone"):
            return get_phone, text.replace("phone", "").strip().split()
        if text1.startswith("change"):
            return change, text.replace("change", "").strip().split()
        else:
            return no_command, ''
    else:
        return no_command, ''


def show_all(*args):

    [print(f"Name contact: {key}  Phone number: {value}", end="\n") for key,
     value in address_book.items()]
    return


if __name__ == "__main__":
<<<<<<< HEAD
    main()
=======

    ab = AddressBook()
    name = Name("Bill")
    phone1 = Phone("12345")
    rec = Record(name, phone1)
    print(rec.name)
    res = ab.contacts.append(Record.add_record(rec))
    print(res)

    # for rec in ab.values():
    #     assert isinstance(rec, Record)

    #     phone2 = Phone("56784")
    #     print(ab)


# reсords = [Record(...), Record(...) ]
# return = "\n".join(reсords)
# print (return)
# result = map(str, reсords)
# return = "\n".join(result)
# def __init__(self):
#         self.contacts = []


#     def list_contacts(self, contacts):

#         return self.contacts


#     def add_contacts(self, name, phone, email, favorite=False):
#         contacts = []
#         ab={}
#         ab['id']= Contacts.current_id
#         ab['name'] = name
#         ab['phone'] = phone
#         ab['email'] = email
#         ab['favorite'] = favorite
#         contacts.append(ab)

#         print (contacts)

#         Contacts.current_id+=1
#         print(Contacts.current_id)
#         return contacts

# print (Contacts.list_contacts(Contacts.add_contacts(1,"Wylie Pope", "(692) 802-2949", "est@utquamvel.net", True)))
>>>>>>> 1db26908da596147dfca76ef3a11109af2a4d992
