class IntegerValue:

    def __set__(self, instance, value):
        self._value = value

    def __get__(self, instance, owner_class):
        if instance is None:
            return self

        else:
            return self._value


class Point2D:
    x = IntegerValue()
    y = IntegerValue()


p1 = Point2D()
p2 = Point2D()

p1.x = 1.1
print(f"p1.x = {p1.x}")
print(f"p2.x = {p2.x}")

p2.y = 2.2
p2.x = 10.0
print(f"p1.x = {p1.x}")
print(f"p2.x = {p2.x}")

print(f"p1.y = {p1.y}")
print(f"p2.y = {p2.y}")

