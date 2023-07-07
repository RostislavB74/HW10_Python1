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