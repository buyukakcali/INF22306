#data2 = [[['x','x',''],['x','x',''],['x','x','']],[['x','x',''],['x','x',''],['x','x','']],[['x','x',''],['x','x',''],['x','x','']]]

def titactoe(lst):
    list0 = []
    list1 = []
    visual = ''

    for i in range(len(lst)): # data ile test et
        list1 += lst[i]

#    for i in range(len(lst)): #1 Alt alta iki for döngüsü, içi içe geçmiş iki liste için tasarlandı. data2 ile test edilir!
#        list0 += lst[i]
#
#    for i in range(len(list0)): #2
#        list1 += list0[i]

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