from datetime import datetime
from collections import UserDict

class Field():
    def __init__(self, value=None):
        self.__value = None
        self.value = value
    
    def __str__(self):
        return str(self.value)
    
    def __repr__(self):
        return str(self.value)    
    
    @property
    def value(self):
        return self.__value
    
    @value.setter
    def value(self, value):
        if value:
            self.__value = value
        
class Name(Field):
    pass


class Phone(Field):
    @property
    def value(self):
        return self.__value
    
    @value.setter
    def value(self, value):
        self.__value = Phone.__test_phone(value)        

    @staticmethod
    def __test_phone(value):
        if value:
            if value.startswith("+"):
                value = value[1:]
            
            if value.isdigit():
                return value
            else:
                raise ValueError("Phone must be a number.")
        else:            
            raise ValueError("Enter phone number.")


class Birthday(Field):
    @property
    def value(self):
        return self.__value
    
    @value.setter
    def value(self, value):
        self.__value = Birthday.__test_date(value)
           
    @staticmethod
    def __test_date(value):
        if value:
            try:
                return datetime.strptime(value, "%d-%m-%Y").date()                
            except ValueError as e:
                raise ValueError(f"{e} \nPlease enter the date in the format dd-mm-yyyy.")
        else:
            raise TypeError("Please enter birthday.")

class Record():
    def __init__(self, name:Name, phone: Phone=None, birthday: Birthday=None):
        self.name = name        
        self.phones = []
        self.birthday = birthday        
        if phone:
            self.add_phone(phone)

    def __str__(self):
        return f"self.name: self.phones"
        
    def __repr__(self):
        return f"self.name: self.phones"
        
    def add_phone(self, phone: Phone):
        if phone.value not in [p.value for p in self.phones]:
            self.phones.append(phone)
            return f"Phone {phone} add to contact {self.name}"
        return f"Phone {phone} present in phones of contact {self.name}"

    def delete_phone(self, phone):
        for item in self.phones:
            if item.value == phone.value:
                self.phones.remove(item)

    def change_phone(self, old_phone: Phone, new_phone: Phone):
        self.delete_phone(old_phone)
        self.phones.append(new_phone)
        return f"phone {old_phone} was replaced by {new_phone}"
    
    def add_birthday(self, birthday: Birthday):
        if self.birthday:
            return f"The contact {self.name} contains a birthday {self.birthday}"
        
        else:
            self.birthday = birthday
            return f"Birthday {self.birthday} add to contact {self.name}"

    
    def days_to_birthday(self, birthday):
        date_now = datetime.now().date()
        date_bd = birthday.value.replace(year=date_now.year)
        if date_bd >= date_now:            
            result = date_bd - date_now
        else:
            date_bd = birthday.value.replace(year=date_now.year + 1)
            result = date_bd - date_now
        return f"{self.name}'s birthday will be in {result.days} days"


class AddressBook(UserDict):    
    def add_record(self, record: Record):
        if record.name.value not in self.keys():
            self.data[record.name.value] = record 
            return f"Added {record.name.value} with phone number {', '.join(str(phone) for phone in record.phones)}"
        else:            
            return f"Record {record.name.value} alredy exists"
    
    def __iter__(self):
        return self.iterator()

    def iterator(self, group_size):
        records = list(self.data.values())
        self.current_index = 0

        while self.current_index < len(records):
            group_items = records[self.current_index:self.current_index + group_size]
            group = [rec for rec in group_items]
            self.current_index += group_size
            yield group

        