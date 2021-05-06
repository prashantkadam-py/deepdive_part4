import itertools
from timezone import TimeZone

class Account:
    
    transaction_id = itertools.count(100)

    def __init__(self, account_number, first_name, last_name, timezone=None):

        self._account_number = account_number
        self.first_name = first_name
        self.last_name = last_name
        
        if timezone is None:
            timezone = TimeZone('UTC', 0, 0)

        self.timezone = timezone

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
        if value is None or len(str(value).strip()) == 0:
            raise ValueError(f'{field_title} cannot be empty.')

    def validate_and_set_name(self, attr_name, value, field_title):
        if value is None or len(str(value).strip()) == 0:
            raise ValueError(f'{field_title} cannot be empty.')
        setattr(self, attr_name, value)

    @property
    def timezone(self):
        return self._timezone
    
    @timezone.setter
    def timezone(self, value):
        if not isinstance(value, TimeZone):
            raise ValueError("Time Zone must be a valid TimeZone object.")

        self._timezone = value





if __name__ == "__main__":
    #a1 = Account(1234, None, None)
    #a1.first_name
    a2 = Account(1234, "Tyrion", "Lannister")
    print(a2.first_name)
    print(a2.last_name)

    a2.timezone = TimeZone('MST', -7, 0)
    
    print(a2.timezone)

    a3 = Account(5467, "Jamie", "Lannister", "-7:00")
