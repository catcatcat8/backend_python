"""Лебедев Евгений: Метакласс изменяющий названия атрибутов класса"""

class CustomMeta(type):
    """Класс метакласса"""

    def __new__(cls, name, bases, dct):
        """Изменение полей класса и названий функций класса"""

        new_dct = {
            key if key.startswith('__') else 'custom_' + key : value
            for key, value in dct.items()
        }
        return super().__new__(cls, name, bases, new_dct)

    def __call__(cls, *args):
        """Изменение полей объекта"""

        obj = type.__call__(cls, *args)  # вызывается метод __init__
        new_dct = {
            'custom_' + key : value
            for key, value in obj.__dict__.items()
        }
        obj.__dict__ = new_dct
        return obj


class CustomClass(metaclass=CustomMeta):
    """Класс, изменяемый метаклассом"""

    x = 50

    def __init__(self, val=99):
        self.val = val

    def line(self):
        return 100

inst = CustomClass()
print(inst.custom_x)  # верно
print(inst.custom_val)  # верно
print(inst.custom_line()) # верно
