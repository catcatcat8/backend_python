"""Тестирование модуля CustomList"""

import unittest
from customlist import CustomList

class AddTests(unittest.TestCase):
    """Тестирование сложения списков"""

    def setUp(self):
        self.custom_list_1 = CustomList([5, 1, 3, 7])
        self.custom_list_2 = CustomList([1, 2, -4])
        self.custom_list_3 = CustomList([1, 2, -4, 5])

        self.basic_list = [1, 2, -4]

    def test_larger_add_smaller(self):
        """Прибавление к большему CustomList списку меньшего CustomList"""

        result = self.custom_list_1 + self.custom_list_2
        self.assertEqual(result, CustomList([6, 3, -1, 7]))

    def test_smaller_add_larger(self):
        """Прибавление к меньшему CustomList большего CustomList"""

        result = self.custom_list_2 + self.custom_list_1
        self.assertEqual(result, CustomList([6, 3, -1, 7]))

    def test_equal_size_adding(self):
        """Сложение равных по длине CustomList"""

        result = self.custom_list_1 + self.custom_list_3
        self.assertEqual(result, CustomList([6, 3, -1, 12]))

    def test_basic_list_adding_right(self):
        """Прибавление к CustomList обычного List"""

        result = self.custom_list_1 + self.basic_list
        self.assertEqual(result, CustomList([6, 3, -1, 7]))
        self.assertIsInstance(result, CustomList)

    def test_basic_list_adding_left(self):
        """Прибавление к обычному list списка CustomList"""

        result = self.basic_list + self.custom_list_1
        self.assertEqual(result, CustomList([6, 3, -1, 7]))
        self.assertIsInstance(result, CustomList)


class SubTests(unittest.TestCase):
    """Тестирование вычитания списков"""

    def setUp(self):
        self.custom_list_1 = CustomList([5, 1, 3, 7])
        self.custom_list_2 = CustomList([1, 2, -4])
        self.custom_list_3 = CustomList([1, 2, -4, 5])

        self.basic_list = [1, 2, -4]

    def test_larger_sub_smaller(self):
        """Вычитание из большего CustomList списка меньшего CustomList"""

        result = self.custom_list_1 - self.custom_list_2
        self.assertEqual(result, CustomList([4, -1, 7, 7]))

    def test_smaller_sub_larger(self):
        """Вычитание из меньшего CustomList большего CustomList"""

        result = self.custom_list_2 - self.custom_list_1
        self.assertEqual(result, CustomList([-4, 1, -7, -7]))

    def test_equal_size_subbing(self):
        """Разность одинаковых по размеру CustomList"""

        result = self.custom_list_1 - self.custom_list_3
        self.assertEqual(result, CustomList([4, -1, 7, 2]))

    def test_basic_list_subbing_right(self):
        """Вычитание из CustomList обычного List"""

        result = self.custom_list_1 - self.basic_list
        self.assertEqual(result, CustomList([4, -1, 7, 7]))
        self.assertIsInstance(result, CustomList)

    def test_basic_list_subbing_left(self):
        """Вычитание из обычного List списка CustomList"""

        result = self.basic_list - self.custom_list_1
        self.assertEqual(result, CustomList([-4, 1, -7, -7]))
        self.assertIsInstance(result, CustomList)


class ListComparisonTests(unittest.TestCase):
    """Тестирование сравнения списков"""

    def setUp(self):
        self.custom_list_1 = CustomList([5, 0, 0, 0])
        self.custom_list_2 = CustomList([1, 2, 5])
        self.custom_list_3 = CustomList([1, 2, 1, 1])

        self.basic_list_1 = [6, 2, -4]
        self.basic_list_2 = [4, 1, 1]
        self.basic_list_3 = [-2, 7]

    def test_lt(self):
        """Тестирование операции 'меньше'"""

        self.assertTrue(self.custom_list_1 < self.custom_list_2)
        self.assertFalse(self.custom_list_1 < self.custom_list_3)
        self.assertFalse(self.custom_list_3 < self.custom_list_1)

        self.assertTrue(self.custom_list_1 < self.basic_list_2)
        self.assertTrue(self.basic_list_1 < self.custom_list_1)
        self.assertTrue(self.basic_list_2 < self.custom_list_2)

    def test_le(self):
        """Тестирование операции 'меньше-равно'"""

        self.assertTrue(self.custom_list_1 <= self.custom_list_2)
        self.assertTrue(self.custom_list_1 <= self.custom_list_3)
        self.assertTrue(self.custom_list_3 <= self.custom_list_1)

        self.assertTrue(self.custom_list_1 <= self.basic_list_2)
        self.assertTrue(self.basic_list_3 <= self.custom_list_1)

    def test_eq(self):
        """Тестирование операции 'равно'"""

        self.assertTrue(self.custom_list_1 == self.custom_list_3)
        self.assertFalse(self.custom_list_1 == self.custom_list_2)

        self.assertTrue(self.custom_list_1 == self.basic_list_3)
        self.assertFalse(self.custom_list_1 == self.basic_list_1)

    def test_ne(self):
        """Тестирование операции 'не равно'"""

        self.assertTrue(self.custom_list_1 != self.custom_list_2)
        self.assertFalse(self.custom_list_1 != self.custom_list_3)

        self.assertFalse(self.custom_list_1 != self.basic_list_3)
        self.assertTrue(self.custom_list_1 != self.basic_list_1)

    def test_gt(self):
        """Тестирование операции 'больше'"""

        self.assertTrue(self.custom_list_2 > self.custom_list_1)
        self.assertFalse(self.custom_list_1 > self.custom_list_3)
        self.assertFalse(self.custom_list_3 > self.custom_list_1)

        self.assertFalse(self.custom_list_1 > self.basic_list_2)
        self.assertFalse(self.basic_list_1 > self.custom_list_1)
        self.assertTrue(self.custom_list_2 > self.basic_list_2)

    def test_ge(self):
        """Тестирование операции 'больше-равно'"""

        self.assertFalse(self.custom_list_1 >= self.custom_list_2)
        self.assertTrue(self.custom_list_2 >= self.custom_list_1)
        self.assertTrue(self.custom_list_1 >= self.custom_list_3)

        self.assertTrue(self.basic_list_3 >= self.custom_list_1)
        self.assertTrue(self.basic_list_2 >= self.custom_list_1)
