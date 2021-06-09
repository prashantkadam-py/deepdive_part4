from enum import Enum, unique

class Timeout(Exception):
    pass

@unique
class AppException(Enum):

    Generic = 100, Exception, "App Exception"
    Timeout = 101, Timeout, "Timeout Connecting to resource"
    NotAnInteger = 200, ValueError, "Value must be an Integer"
    NotAList = 200, ValueError, "Value must be a list"


    def __new__(cls, ex_code, ex_class, ex_msg):
        member = object.__new__(cls)
        member._value = ex_code
        member.exception = ex_class
        member.message = ex_msg
        return member

    @property
    def code(self):
        return self._value

    
    def throw(self, message = None):
        message  = message or self.message
        raise self.exception(f"{self.code} - {message}")
        


if __name__ == "__main__":
    print(AppException.Timeout.code)
    print(AppException.Timeout.throw("My timeout Error msg"))


