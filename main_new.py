from collections import UserDict


class AddressBook(UserDict):
    def add_record(rec):
        pass


class Record():
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

    ab.add_record(rec)

    ab.add_record(Record(Name("Jill")))

    for rec in ab.values():
        assert isinstance(rec, Record)

        phone2 = Phone("56784")
        print(ab)


# reсords = [Record(...), Record(...) ]
# return = "\n".join(reсords)
# print (return)
# result = map(str, reсords)
# return = "\n".join(result)
