from collections import UserDict


class AddressBook(UserDict):
    def add_record(rec):
        pass


class Record():
    
    def __init__(self, name, num_phone):
        self.name = name
        self.phone = num_phone


class Parser():

    def parser(text: str): #-> tuple[callable, tuple[str] | None]:

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


    def __repr__(self, records):
        # result = map(str, reсords)
        return "\n".join(str(rec) for rec in records)
        #   return str(.....)


class Field():
    pass


class Name(Field):
    def __init__(self, data):
        self.name = data


class Main():
    def main():
        while True:
            user_input = input(">>>")
            if user_input:
                command, data = Parser.parser(user_input)
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


class Phone(Field):
    def __init__(self, num_phone):
        self.phone = num_phone



if __name__ == "__main__":
    Main.main()





# ab = AddressBook()
# name = Name("Bill")
# phone1 = Phone("12345")
# rec = Record(name, phone1)
# print(rec.name)

# ab.add_record(rec)

# ab.add_record(Record(Name("Jill")))

# for rec in ab.values():
#     assert isinstance(rec, Record)

#     phone2 = Phone("56784")
#     print(ab)


# reсords = [Record(...), Record(...) ]
# return = "\n".join(reсords)
# print (return)
# result = map(str, reсords)
# return = "\n".join(result)
