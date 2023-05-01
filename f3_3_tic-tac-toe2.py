#data2 = [[['x','x',''],['x','x',''],['x','x','']],[['x','x',''],['x','x',''],['x','x','']],[['x','x',''],['x','x',''],['x','x','']]]

def titactoe(lst):
    list0 = []
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

def who_won(board): #main function
    return 0 #return "both,x,o or nobody"

def check_vertically(board,row,player):
    for col in range(len(board)):
        board[row][col]
    return 0 #return True or False

if __name__ == '__main__':
    board = [['x', 'o', ''], ['x', '', ''], ['o', '', '']]
    print(titactoe(board))