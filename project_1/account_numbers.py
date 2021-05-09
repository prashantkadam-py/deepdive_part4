import itertools
from timezone import TimeZone
import numbers
from datetime import datetime
from collections import namedtuple

Confirmation = namedtuple("Confirmation", "account_number, transaction_code, transaction_id, time_utc, time")

class Account:
    
    transaction_id = itertools.count(100)
    _interest_rate = 0.5
    _transaction_codes = {
            "deposit" : "D",
            "withdraw" : "W",
            "interest" : "I",
            "rejected" : "X"
            }

    def __init__(self, account_number, first_name, last_name, timezone=None, initial_balance=0):

        self._account_number = account_number
        self.first_name = first_name
        self.last_name = last_name
        
        if timezone is None:
            timezone = TimeZone('UTC', 0, 0)

        self.timezone = timezone

        self._balance = float(initial_balance)


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

    @property
    def balance(self):
        return self._balance

    @classmethod
    def get_interest_rate(cls):
        return cls._interest_rate

    @classmethod
    def set_interest_rate(cls, value):
        if not isinstance(value, numbers.Real):
            raise ValueError("Interest Rate must be a Real Number.")

        if value < 0:
            raise ValueError("Interest Rate cannot be negative number.")

        cls._interest_rate = value

    
    def generate_confirmation_code(self, transaction_code):
        dt_str = datetime.utcnow().strftime("%Y%m%d%H%M%S")
        confirmation_code = f"{transaction_code}-{self.account_number}-{dt_str}-{next(Account.transaction_id)}"
        return confirmation_code

    def make_transactions(self):
        return self.generate_confirmation_code("dummy")


    @staticmethod
    def parse_confirmation_code(confirmation_code, preferred_time_zone=None):
        parts = confirmation_code.split("-")
        
        if len(parts) !=4:
            raise ValueError("Invalid Confirmation Code.")

        transaction_code, account_number, raw_dt_utc, transaction_id = parts

        try:
            dt_utc = datetime.strptime(raw_dt_utc, "%Y%m%d%H%M%S")
        except ValueError as ex:
            raise ValueError("Invalid Transction Datetime.") from ex

        if preferred_time_zone is None:
            preferred_time_zone = TimeZone("UTC", 0, 0)

        if not isinstance(preferred_time_zone, TimeZone):
            raise ValueError("Invalid Timezone specified.")

        dt_preferred = dt_utc + preferred_time_zone.offset
        dt_preferred_str = f"{dt_preferred.strftime('%Y-%m-%d %H:%M:%S')} ({preferred_time_zone.name})"

        return Confirmation(account_number, transaction_code, transaction_id, dt_utc.isoformat(), dt_preferred_str)

    @staticmethod
    def validate_real_number(value, min_value=None):
        
        if not isinstance(value, numbers.Real):
            raise ValueError("Value must be a real number.")

        if min_value is not None and value < min_value:
            raise ValueError(f"Value must be atleast {min_value}")

        return value


    def deposit(self, value):
        value = Account.validate_real_number(value, min_value=0.1)
        transaction_code = Account._transaction_codes["deposit"]
        conf_code = self.generate_confirmation_code(transaction_code)
        self._balance += value 
        return conf_code


    def withdraw(self, value):
        value = Account.validate_real_number(value, min_value=0.1)
        
        accepted = False
        if self.balance - value < 0:
            transaction_code = Account._transaction_codes["rejected"]
        else:
            transaction_code = Account._transaction_codes["withdraw"]
            accepted = True

        conf_code = self.generate_confirmation_code(transaction_code)
    
        if accepted:
            self._balance -= value

        return conf_code
        

    def pay_interest(self):
        interest = self.balance * Account.get_interest_rate() / 100
        transaction_code = Account._transaction_codes["interest"]
        conf_code = self.generate_confirmation_code(transaction_code)
        self._balance += interest
        return conf_code


if __name__ == "__main__":
    #a1 = Account(1234, None, None)
    #a1.first_name
    a2 = Account(1234, "Tyrion", "Lannister", initial_balance=100)
    print(a2.first_name)
    print(a2.last_name)

    a2.timezone = TimeZone('MST', -7, 0)
    
    print(a2.timezone)

    #a3 = Account(5467, "Jamie", "Lannister", "-7:00")
    
    a4 = Account(5467, "Cersei", "Lannister", initial_balance=100)
    print(a4.balance)

    #a2.balance = 50

    print(Account.get_interest_rate())
    Account.set_interest_rate(10)
    print(Account.get_interest_rate())

    confirmation_code = a2.make_transactions()
    print(confirmation_code)

    print(Account.parse_confirmation_code(confirmation_code))

    print("Transactions.........")
    print(a2.balance)
    print("deposit", a2.deposit(200))
    print("balance", a2.balance)
    print("pay interest", a2.pay_interest())
    print("balance", a2.balance)
    print("withdraw", a2.withdraw(50))
    print("balance", a2.balance)

