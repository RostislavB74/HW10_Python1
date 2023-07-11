from collections import UserDict

def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except IndexError:
            print("Give me a name one phone number or several phone numbers please")
        except TypeError:
            print("Give me a name one phone number or several phone numbers please")
        except ValueError:
            print("Give me a name one phone number or several phone numbers please")
    return wrapper


class AddressBook(UserDict):
    ab={}
    cotacts =[]


class ControlBot:

    def hello(*args):
        return "How can I help you?"

    def exit(*args):
        return "Good bye!"
    
    def no_command(*args, **kwargs):
        return "Unknown command"



class Field():
    pass


class Name(Field):

    def __init__(self, data):
        self.name = data


class Phone(Field):

    def __init__(self, num_phone):
        self.phone = num_phone


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




class Parser():

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

    def __repr__(self, records):
        # result = map(str, reсords)
        return "\n".join(str(rec) for rec in records)
        #   return str(.....)

class Record():
    
    def __init__(self, name, num_phone):
        self.name = name
        self.phone = num_phone
    @input_error
    def add(*args):
        print (Name(args[0]))
        print (Phone(args[1]))
        if len(args) ==2: 
            name =  args[0]
            phone = args[1]
            rec = Record(name, phone)
        if len(args) > 2:
            phone = []
            name = Name(args[0])
            for i in range(1,len(args)):
                phone.append(Phone(args[i]))
            rec = Record(name, phone)
        AddressBook.ab[name] = phone
        AddressBook.cotacts.append(rec)
        return f"Add success {name} {phone}"

    def change(*args):
        name = Name(args[0])
        phone_old = Phone(args[1])
        phine_new = Phone(args[2])
        AddressBook.ab[name] = phone
        return f"Change success {name} from {phone_old} to {phone_new}"
   
class RequestContacts():
   
    @input_error
    def get_phone(*args):
        name = str.capitalize(args[0])
        return f"User:{name}  Phone: {address_book[name]}"

    def show_all(*args):
        [print(f"Name contact: {key}  Phone number: {value}", end="\n") for key,
        value in address_book.items()]
        return
   
   
        # add_record(rec)
    #     name = str.capitalize(args[0])
    # phone = args[1]
    # address_book[str.capitalize(name)] = phone
    # return f"Add success {name} {phone}" 


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
