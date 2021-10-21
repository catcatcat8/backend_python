"""Тестирование модуля CustomMeta"""

import unittest
from custommeta import CustomMeta

class MetaClassProcessing(unittest.TestCase):
    """Тестирование изменения названий атрибутов класса"""

    def setUp(self):
        class CustomClass(metaclass=CustomMeta):
            """Класс для тестирования"""
            x = 50

            def __init__(self, val=99):
                self.val = val

            def line(self):
                return 100

        self.inst = CustomClass()

    def test_class_instance_changed(self):
        """Тестирование изменения полей класса"""

        self.assertEqual(self.inst.custom_x, 50)
        with self.assertRaises(AttributeError):
            self.inst.x

    def test_class_function_changed(self):
        """Тестирование изменения функций класса"""

        self.assertEqual(self.inst.custom_line(), 100)
        with self.assertRaises(AttributeError):
            self.inst.line()

    def test_object_instance_changed(self):
        """Тестирование изменения полей объекта"""

        self.assertEqual(self.inst.custom_val, 99)
        with self.assertRaises(AttributeError):
            self.inst.val
