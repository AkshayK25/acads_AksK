try:
    raise NameError('hi There')

except NameError:
    print('An exception')
    raise

# output:
# An exception
# Traceback (most recent call last):
#   File "D:/hello-git/NameError_Exception.py", line 2, in <module>
#     raise NameError('hi There')
# NameError: hi There    