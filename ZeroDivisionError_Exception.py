def abyb(a, b):
    try:
        c = (a+b)/(a-b)
    except ZeroDivisionError:
        print('Error info -> (a/b result in zero)')
    else:
        print('Answer::', c)


print('---------------------------------ZeroDivisionError_Exception_Handling---------------------')
abyb(2.0, 3.0)
abyb(2.0, 2.0)
print("\n------------------------------End of the program-----------------------------------------")
