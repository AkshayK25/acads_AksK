book = ['physics', 'chemistry', 'maths']
try:
    value = int(input("Enter the number please!!!\n"))
    print(book[3])
    from maths import*

except (ValueError, IndexError, ImportError):
    print('Multiple Exception handling')

else:
    print(value)
