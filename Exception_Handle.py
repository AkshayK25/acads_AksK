a = 3
try:
    if a < 4:
        a = a/(a-3)

except ZeroDivisionError:
    print('Error hai bhai sahab Zara denominator toh dekh lo !!!')

else:
    print(a)
