"""Лебедев Евгений: Кастом-список с переопределенными операциями сложения, вычитания, сравнения"""

def copy_lst_add_zeros_to_the_end(lst, amount):
    """Функция копирующая 'lst' и добавляющая 'amount' нулей в конец"""

    new_lst = lst[:]
    [new_lst.append(0) for i in range(0, amount)]
    return new_lst

class CustomList(list):
    """Класс кастомного списка"""

    def __init__(self, *args):
        super(CustomList, self).__init__(args[0])

    def __add__(self, other):
        difference = abs(len(self) - len(other))
        if len(self) > len(other):
            copy_other = copy_lst_add_zeros_to_the_end(other, difference)
            new_list = CustomList(map(lambda x, y: x + y, self, copy_other))
        elif len(self) < len(other):
            copy_self = copy_lst_add_zeros_to_the_end(self, difference)
            new_list = CustomList(map(lambda x, y: x + y, copy_self, other))
        else:
            new_list = CustomList(map(lambda x, y: x + y, self, other))
        return new_list

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        difference = abs(len(self) - len(other))
        if len(self) > len(other):
            copy_other = copy_lst_add_zeros_to_the_end(other, difference)
            new_list = CustomList(map(lambda x, y: x - y, self, copy_other))
        elif len(self) < len(other):
            copy_self = copy_lst_add_zeros_to_the_end(self, difference)
            new_list = CustomList(map(lambda x, y: x - y, copy_self, other))
        else:
            new_list = CustomList(map(lambda x, y: x - y, self, other))
        return new_list

    def __rsub__(self, other):
        difference = abs(len(self) - len(other))
        if len(self) > len(other):
            copy_other = copy_lst_add_zeros_to_the_end(other, difference)
            new_list = CustomList(map(lambda x, y: x - y, copy_other, self))
        elif len(self) < len(other):
            copy_self = copy_lst_add_zeros_to_the_end(self, difference)
            new_list = CustomList(map(lambda x, y: x - y, other, copy_self))
        else:
            new_list = CustomList(map(lambda x, y: x - y, other, self))
        return new_list

    def __lt__(self, other):
        return sum(self) < sum(other)

    def __le__(self, other):
        return sum(self) <= sum(other)

    def __eq__(self, other):
        return sum(self) == sum(other)

    def __ne__(self, other):
        return sum(self) != sum(other)

    def __gt__(self, other):
        return sum(self) > sum(other)

    def __ge__(self, other):
        return sum(self) >= sum(other)
