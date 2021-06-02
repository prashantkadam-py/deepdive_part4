import weakref 

class ValidString:

    def __init__(self, min_len=0, max_len=255):
        self.data = {}
        self.min_len = min_len
        self.max_len = max_len


    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError("Value must be string")
        
        if len(value) < self.min_len:
            raise ValueError(f"Value must be less than {self.min_len}")

        if len(value) > self.max_len:
            raise ValueError(f"Value must be greater than {self.max_len}")

        self.data[id(instance)] = (weakref.ref(instance, 
                                    self._finalize_instance), value)



    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        else:
            value_tuple = self.data.get(id(instance), [])
            val = value_tuple[1] if len(value_tuple) == 2 else None
            return val


class Person:
    __slots__ = "__weakref__"

    first_name = ValidString(1, 100)
    last_name = ValidString(1, 100)

    def __eq__(self, other):
        return  (isinstance(other, Person) and \ 
                self.first_name == other.first_name and \ 
                self.last_name == other.last_name)



