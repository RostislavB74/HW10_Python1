from collections import UserDict


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


class Field():
    pass


class Name(Field):
    def __init__(self, data):
        self.name = data


class Phone(Field):
    def __init__(self, num_phone):
        self.phone = num_phone


if __name__ == "__main__":

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
