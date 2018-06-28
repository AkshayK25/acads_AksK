my_list = [1, 2, 3]
try:
    print(my_list[3])

except IndexError:
    print('--------------------It will show index error bcz that index was not exists in the list---------------------')
