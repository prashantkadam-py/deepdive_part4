class ValidString:

    def __init__(self, min_len=None):
        self.min_len = min_len

    def __set_name__(self, owner_class, property_name):
        self.property_name = property_name

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError(f"{self.property_name} must be a string")

        if self.min_len is not None and len(value) < self.min_len :
            raise ValueError(f"{self.property_name} must be at least {self.min_len} characters.")
        
        key = "_" + self.property_name
        instance.__dict__[key] = value 


    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        else:
            #return instance.__dict__.get(self.property_name, None)
            key = "_" + self.property_name
            return getattr(instance, key, None)

class Person:
    first_name = ValidString(1)
    last_name = ValidString(1) 


p = Person()
print(p.__dict__)
p.first_name = "Tyrion"
p.last_name = "Lannister"
print(p.__dict__)
print(p.first_name)

