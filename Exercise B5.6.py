count = 1
board = [["-" for i in range(j, j + 3)] for j in range(1, 3 * 3 - 1, 3)]
print("Game start!")


def board_to_console():
    """Удобоваримый вывод"""
    print("   0 1 2")
    for i in range(len(board)):
        print(f"{i} ", " ".join(board[i]))


def check_coordinates(coord, value):
    """Получаем True, если значение есть"""
    return board[coord[0]][coord[1]] == value


def check_win(turn):
    """Проверяем есть ли координаты с одинаковыми значениями в кортеже"""
    win_coordinate = (
        ((0, 0), (0, 1), (0, 2)),
        ((1, 0), (1, 1), (1, 2)),
        ((2, 0), (2, 1), (2, 2)),
        ((0, 0), (1, 0), (2, 0)),
        ((0, 1), (1, 1), (2, 1)),
        ((0, 2), (1, 2), (2, 2)),
        ((0, 0), (1, 1), (2, 2)),
        ((0, 2), (1, 1), (2, 0)),
                      )
    for row in win_coordinate:
        if turn[0] in row and all([check_coordinates(cell, turn[1]) for cell in row]):
            return True
    return False


while count < 10:
    board_to_console()
    turn = tuple(map(int, input("Enter coordinates x, y: ").split())), str("X" if count % 2 == 0 else "O")
    try:
        cell = board[turn[0][0]][turn[0][1]]
    except IndexError:
        print("Coordinate is out of board. Enter another coordinate")
        continue
    if board[turn[0][0]][turn[0][1]] == "-":
        board[turn[0][0]][turn[0][1]] = turn[1]
        count += 1
    else:
        print("Coordinate is already in. Enter another coordinate")
    if check_win(turn):
        print(f"The WINNER is \"{turn[1]}\"")
        count = 10
