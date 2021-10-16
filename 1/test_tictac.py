"""Тестирование модуля TicTacGame"""

import unittest
from tictac import TicTacGame

class StartGameTest(unittest.TestCase):
    """Тестирование метода началы игры"""

    def setUp(self):
        self.game = TicTacGame()

    def test_start_game(self):
        result = self.game.start_game()
        self.assertEqual(result, ['1', '2', '3', '4', '5', '6', '7', '8', '9'])


class ValidateInputMakeMoveTests(unittest.TestCase):
    """Тестирование методов валидации введенных данных и изменений поля игры"""

    def setUp(self):
        self.game = TicTacGame()
        self.game.start_game()

    def test_make_correct_moves(self):
        input = '6'
        self.assertTrue(self.game.validate_input(input))
        result = self.game.make_move(input, 'X')
        self.assertEqual(result, ['1', '2', '3', '4', '5', 'X', '7', '8', '9'])

        input = '2'
        self.assertTrue(self.game.validate_input(input))
        result = self.game.make_move(input, '0')
        self.assertEqual(result, ['1', '0', '3', '4', '5', 'X', '7', '8', '9'])

    def test_not_a_number_input(self):
        input = "d4"
        with self.assertRaises(ValueError):
            self.game.make_move(input, 'X')

    def test_incorrect_number_input(self):
        input = "0"
        with self.assertRaises(ValueError):
            self.game.validate_input(input)

        input = "10"
        with self.assertRaises(ValueError):
            self.game.validate_input(input)

    def test_already_occupied_cell_input(self):
        input = '6'
        self.game.make_move(input, 'X')

        with self.assertRaises(RuntimeError):
            self.game.validate_input(input)


class CheckWinnerTests(unittest.TestCase):
    """Тестирование определения победителя игры"""

    def setUp(self):
        self.game = TicTacGame()
        self.game.start_game()

    def test_horizontal_wins(self):
        self.game.field = ['X', 'X', 'X',
                           '4', '5', '6',
                           '7', '8', '9']
        self.assertTrue(self.game.check_winner())

        self.game.field = ['0', '0', '0',
                           '4', '5', '6',
                           '7', '8', '9']
        self.assertTrue(self.game.check_winner())

        self.game.field = ['0', '0', '3',
                           'X', 'X', 'X',
                           '7', '8', '0']
        self.assertTrue(self.game.check_winner())


    def test_vertical_wins(self):
        self.game.field = ['X', '2', '3',
                           'X', '5', '6',
                           'X', '8', '9']
        self.assertTrue(self.game.check_winner())

        self.game.field = ['0', '2', '3',
                           '0', '5', '6',
                           '0', '8', '9']
        self.assertTrue(self.game.check_winner())

        self.game.field = ['0', 'X', '0',
                           '0', 'X', '6',
                           '7', 'X', '9']
        self.assertTrue(self.game.check_winner())


    def test_diagonal_wins(self):
        self.game.field = ['X', '2', '3',
                           '4', 'X', '6',
                           '7', '8', 'X']
        self.assertTrue(self.game.check_winner())

        self.game.field = ['0', '2', '3',
                           '4', '0', '6',
                           '7', '8', '0']
        self.assertTrue(self.game.check_winner())

        self.game.field = ['X', 'X', '0',
                           'X', '0', 'X',
                           '0', '8', 'X']
        self.assertTrue(self.game.check_winner())


    def test_not_winning(self):
        self.game.field = ['X', 'X', '0',
                           '0', '0', 'X',
                           'X', 'X', '0']
        self.assertFalse(self.game.check_winner())

        self.game.field = ['0', '2', '3',
                           '4', 'X', '6',
                           'X', '8', '0']
        self.assertFalse(self.game.check_winner())

        self.game.field = ['X', 'X', '0',
                           'X', '0', 'X',
                           '7', '8', 'X']
        self.assertFalse(self.game.check_winner())
