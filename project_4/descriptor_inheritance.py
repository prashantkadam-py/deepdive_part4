class BaseValidator():

    def __init__(self, min_ = None, max_ = None):
        self.min_value = min_
        self.max_value = max_

    def __set_name__(self, owner_class, prop_name_):
        self.prop_name = prop_name_


    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        else:
            return instance.__dict__.get(self.prop_name, None)
    
    def validate(self, value):
        pass

    def __set__(self, instance, value):
        self.validate(value)
        return instance.__dict__[self.prop_name] = value


class IntegerField(BaseValidator):
    def validate(self, value):
        if not isinstance(value, numbers.Integral):
            raise ValueError(f"{self.prop_name} must be an integer.")

        if self.min_value is not None and self.min_value > value:
            raise ValueError(f"{self.prop_name} must be greater than {self.min_value}")

        if self.max_value is not None and value > self.max_value:
            raise ValueError(f"{self.prop_name} must be less than {self.max_value}")

        
class CharField(BaseValidator):
    
    def __init__(self, min_, max_):
        min_ = max(min_ or 0, 0)
        super().__init__(min_, max_)

    def validate(self, value):
        if not isinstance(value, str):
            raise ValueError(f"{self.prop_name} must be a string.")

        if self.min_value is not None and len(value) < self.min_value:
            raise ValueError(f"{self.prop_name} must be >= {self.min_value} chars")

        if self.max_value is not None and len(value) > self.max_value:
            raise ValueError(f"{self.prop_name} must be < {self.max_value} chars")



