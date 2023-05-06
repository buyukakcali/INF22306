# I have a list of lists. For example,
a_list = [ [0,1,'f'], [4,2,'t'], [9,4,'afsd'] ]

# If I wanted to sort the outer list by the string field of the inner lists, how would you do that in python?

# This is a job for itemgetter

from operator import itemgetter

new_sorted_list = sorted(a_list, key=itemgetter(2))

# It is also possible to use a lambda function here, however the lambda function is slower in this simple case
print(f'Original list: ',a_list)
print(f'Sorted list:   ',new_sorted_list)

assert new_sorted_list == [[9, 4, 'afsd'], [0, 1, 'f'], [4, 2, 't']]