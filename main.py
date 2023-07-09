from collections import UserDict


class AddressBook(UserDict):
    pass


class Record():
   def __repr__(self):
       return str(.....)


class Field():
    pass


class Name():
    pass


class Phone():
    pass


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
