class ValidType:

    def __init__(self, type_):
        self._type = type_


    def __set_name__(self, owner_class, property_name):
        self._property_name = property_name

    
    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        else:
            return instance.__dict__.get(self._property_name, None)

    def __set__(self, instance, value):

        if not isinstance(value, self._type):
            raise ValueError(f"{self._property_name} must be of type {self._type}")

        instance.__dict__[self._property_name] = value


class Person:

    age = ValidType(int)
    height = ValidType(float)
    tags = ValidType(list)
    favourite_foods = ValidType(tuple)


p = Person()
p.height = 10.0
print(f"person height is {p.height}")
p.height = 10

