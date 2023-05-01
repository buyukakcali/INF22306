
def check_row0(board, row, player):   # original one, but you had better ideas!
    has_won = True
    for col in range(len(board[row])):
        elem = board[row][col]
        if elem != player:
            has_won = False
    return has_won


def check_row(board, row, player):
    has_won = board[row] == [player] * len(board[row])
    return has_won


def check_col(board, col, player):
    has_won = True
    for row in range(len(board)):
        elem = board[row][col]
        if elem != player:
            has_won = False
    return has_won


def check_diagonal1(board, player):
    has_won = True
    for i in range(len(board)):
        elem = board[i][i]
        if elem != player:
            has_won = False
    return has_won


def check_diagonal2(board, player):
    has_won = True
    for i in range(len(board)):
        elem = board[i][-i - 1]   # len(board) - 1 - i
        if elem != player:
            has_won = False
    return has_won


def who_won(board):         # main function, uses (calls) the others
    has_x_won = False
    has_o_won = False

    for row in range(len(board)):
        x_won = check_row(board, row, 'x')
        o_won = check_row(board, row, 'o')
        has_x_won = x_won or has_x_won
        has_o_won = o_won or has_o_won

    for col in range(len(board[0])):
        x_won = check_col(board, col, 'x')
        o_won = check_col(board, col, 'o')
        has_x_won = x_won or has_x_won
        has_o_won = o_won or has_o_won

    x_won = check_diagonal1(board, 'x') or check_diagonal2(board, 'x')
    o_won = check_diagonal1(board, 'o') or check_diagonal2(board, 'o')
    has_x_won = x_won or has_x_won
    has_o_won = o_won or has_o_won

    if has_x_won and has_o_won:
        result = 'Both'
    elif has_x_won:
        result = 'x'
    elif has_o_won:
        result = 'o'
    else:
        result = 'Neither'
    return result

# Yukarısı sınıf egzersizindeki kodlar

def titactoe(lst):
    list1 = []
    visual = ''

    for i in range(len(lst)): # data ile test et
        list1 += lst[i]

    for i in range(len(list1)):
        if list1[i] == '' and i%3 != 2:
            visual += '   |'
        elif list1[i] == '' and i%3 == 2 and i != len(list1)-1:
            visual += '   \n---+---+---\n'

        elif list1[i] == 'o' and i%3 != 2:
            visual += ' o |'
        elif list1[i] == 'o' and i%3 == 2 and i != len(list1)-1:
            visual += ' o \n---+---+---\n'

        elif list1[i] == 'x' and i%3 != 2:
            visual += ' x |'
        elif list1[i] == 'x' and i%3 == 2 and i != len(list1)-1:
            visual += ' x \n---+---+---\n'
    return visual

if __name__ == '__main__':
    board = [['x', 'o', ''], ['x', '', ''], ['o', '', '']]
    print(titactoe(board))