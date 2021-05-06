#Making use of class to generate transaction ids

class TransactionID:

    def __init__(self, start_id):
        self._start_id = start_id


    def next(self):
        self._start_id += 1
        return self._start_id


class Account:

    transaction_counter = TransactionID(100)

    def make_transaction(self):
        new_transaction_id = Account.transaction_counter.next()
        return new_transaction_id



a1 = Account()
a2 = Account()
print("Making use of class to generate transaction ids")
print(a1.make_transaction())
print(a1.make_transaction())
print(a2.make_transaction())

#Making use of generator protocol to generate transaction ids

def transaction_ids(start_id):
    while True:
        start_id += 1
        yield start_id

class Account1:

    transaction_counter = transaction_ids(100)

    def make_transaction(self):
        new_transaction_id = next(Account1.transaction_counter)
        return new_transaction_id

a1 = Account1()
a2 = Account1()
print("\n\n\n\n")
print("Making use of generator protocol to generate transaction ids")
print(a1.make_transaction())
print(a1.make_transaction())
print(a2.make_transaction())


# Making use of itertools module to generate transaction ids
import itertools

class Account2:

    transaction_counter = itertools.count(100)

    def make_transaction(self):
        new_transaction_id = next(Account2.transaction_counter)
        return new_transaction_id

a1 = Account2()
a2 = Account2()
print("\n\n\n\n")
print("Making use of itertools module to generate transaction ids")
print(a1.make_transaction())
print(a1.make_transaction())
print(a2.make_transaction())

  
