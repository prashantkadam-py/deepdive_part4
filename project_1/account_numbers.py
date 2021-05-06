import itertools

class Account:
    
    transaction_id = itertools.count(100)

    def __init__(self, account_number, first_name, last_name):

        self._account_number = account_number
        self.first_name = first_name
        self.last_name = last_name

    @property
    def account_number(self):
        return self._account_number

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        self.validate_and_set_name("_first_name",value, "First Name")

    @property
    def last_name(self):
        return self._last_name
    
    @last_name.setter
    def last_name(self, value):
        self.validate_and_set_name("_last_name",value, "Last Name")
    
    @staticmethod
    def validate_name(value, field_title):
        if value is None and len(str(value).strip()) == 0:
            raise ValueError(f'{field_title} cannot be empty.')

    def validate_and_set_name(self, attr_name, value, field_title):
        if value is None and len(str(value).strip()) == 0:
            raise ValueError(f'{field_title} cannot be empty.')
        setattr(self, attr_name, value)

if __name__ == "__main__":
    a1 = Account(1234, None, None)
    a1.first_name
    a1.last_name
    a2 = Account(1234, "Tyrion", "Lannister")
    print(a2.first_name)
    print(a2.last_name)
