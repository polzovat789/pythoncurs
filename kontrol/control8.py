def print_board(board):
    # Выводим поле 5x5
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def check_win(board, player):
    # Проверяем строки, столбцы и диагонали на победу
    # Проверка строк и столбцов
    for i in range(5):
        if all([board[i][j] == player for j in range(5)]) or all([board[j][i] == player for j in range(5)]):
            return True

    # Проверка диагоналей
    if all([board[i][i] == player for i in range(5)]) or all([board[i][4 - i] == player for i in range(5)]):
        return True

    return False


def is_full(board):
    # Проверяем, заполнено ли поле
    return all([board[i][j] != ' ' for i in range(5) for j in range(5)])


def make_move(board, player):
    while True:
        try:
            # Запрос хода у игрока
            row, col = map(int, input(
                f"Игрок {player}, введите ваш ход (строка и столбец от 0 до 4 через пробел): ").split())

            # Проверяем, что ввод корректен
            if row < 0 or row >= 5 or col < 0 or col >= 5:
                print("Неверные координаты. Попробуйте еще раз.")
            elif board[row][col] != ' ':
                print("Эта ячейка уже занята. Попробуйте еще раз.")
            else:
                board[row][col] = player
                break
        except ValueError:
            print("Ошибка ввода. Введите два числа через пробел.")


def play_game():
    # Инициализация игрового поля
    board = [[' ' for _ in range(5)] for _ in range(5)]

    # Очередность игроков
    players = ['X', 'O']
    turn = 0

    while True:
        # Отображаем текущее состояние поля
        print_board(board)

        # Определяем текущего игрока
        current_player = players[turn % 2]

        # Игрок делает ход
        make_move(board, current_player)

        # Проверка на победу
        if check_win(board, current_player):
            print_board(board)
            print(f"Поздравляем! Игрок {current_player} победил!")
            break

        # Проверка на ничью (если поле полностью заполнено)
        if is_full(board):
            print_board(board)
            print("Ничья!")
            break

        # Переход к следующему игроку
        turn += 1


# Запуск игры
play_game()
