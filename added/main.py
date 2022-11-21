from typing import List


class Class2:
    pass


class Class:
    TYPES_OF_OBJ = ('std', 'xtd')

    def __init__(self, type_of_obj):
        self.type_of_obj = type_of_obj

    @classmethod
    def create_std_obj(cls) -> 'Class':  # Class2 without quotes
        return cls(cls.TYPES_OF_OBJ[0])

    def __repr__(self):
        return f"<{self.__class__.__name__}:{self.type_of_obj}>"


def summary(x: int, y: int) -> int:
    return x + y


def print_objs(objs: List[Class]) -> None:
    for obj in objs:
        print(obj)


to_sum = [5, 5]
print(summary(*to_sum))

std_obj = Class.create_std_obj()
print(std_obj.type_of_obj)
print(std_obj)
print_objs([std_obj])
