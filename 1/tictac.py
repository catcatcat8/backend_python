"""Лебедев Евгений: Консольная игра крестики-нолики в виде класса"""

class TicTacGame:
    """Класс игры в крестики-нолики"""

    def show_board(self):
        """Выводит содержимое игрового поля в консоль"""

        print('-'*9)
        for i in range(0, 3):
            print(f'|{self.field[i*3]}|{self.field[i*3+1]}|{self.field[i*3+2]}|')
        print('-'*9)

    def make_move(self, position, symbol):
        """Делает очередной ход игры и возвращает содержимое игрового поля"""

        self.field[int(position) - 1] = symbol
        return self.field

    def validate_input(self, input):
        """Возвращает True, если ввод был корректен, вызывает ValueError в противном случае"""

        if (input.isdigit() and 1 <= int(input) <= 9):
            if (self.field[int(input) - 1] not in ['X', '0']):
                return True
            raise RuntimeError
        raise ValueError

    def start_game(self):
        """Создает игровое поле и возвращает его"""

        self.field = ['1', '2', '3',
                      '4', '5', '6',
                      '7', '8', '9']
        return self.field

    def check_winner(self):
        """Возвращает True если игра окончена для текущего поля, в противном случае - False"""

        win_combinations = ((0, 1, 2), (3, 4, 5), (6, 7, 8),
                            (0, 3, 6), (1, 4, 7), (2, 5, 8),
                            (0, 4, 8), (2, 4, 6))
        for combination in win_combinations:
            if self.field[combination[0]] == self.field[combination[1]] == self.field[combination[2]]:
                return True
        return False


# pylint: disable-msg=C0103
if __name__ == '__main__':

    player1 = input('Enter the nickname of the player for "X": ')
    player2 = input('Enter the nickname of the player for "0": ')

    game = TicTacGame()
    game.start_game()

    winner_found = False
    move_number = 0
    game.show_board()

    while not winner_found:
        if move_number % 2 == 0:
            print(f'{player1} turn ("X"): ')
            current_player = player1
            symbol = 'X'
        else:
            print(f'{player2} turn ("0"): ')
            current_player = player2
            symbol = '0'

        while True:
            position = input()
            try:
                game.validate_input(position)
            except ValueError:
                print('Wrong input! It is allowed only to input numbers from 1 to 9!\nTry one more time: ')
            except RuntimeError:
                print('Wrong input! This cell is already occupied!\nTry one more time: ')
            else:
                game.make_move(position, symbol)
                move_number += 1
                break
        game.show_board()

        if game.check_winner():
            winner_found = True
            print(f'Player "{current_player}" won!!! Congratulations :)')
        elif move_number == 9:
            print('The game is finished! Draw!')
            break
