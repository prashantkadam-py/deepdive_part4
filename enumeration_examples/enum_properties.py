from enum import Enum

class AppStatus(Enum):

    OK = (0, "NO PROBLEM!")
    FAILED = (1, "CRAP!!!!")
    
    @property
    def code(self):
        return self.value[0]

    @property
    def phrase(self):
        return self.value[1]


class TwoValueEnum(Enum):
    def __new__(cls, member_value, member_phrase):
        member = object.__new__(cls)
        member.code = member_value
        member.phrase = member_phrase
        return member


class AppStatus1(TwoValueEnum):
    OK = (0, "NO PROBLEM!")
    FAILED = (1, "CRAP!!!!")




if __name__ == "__main__":
    print(AppStatus.OK.code, AppStatus.OK.phrase)
    print(AppStatus.FAILED.code, AppStatus.FAILED.phrase)

    
    print(AppStatus1.OK.code, AppStatus1.OK.phrase)
    print(AppStatus1.FAILED.code, AppStatus1.FAILED.phrase)



