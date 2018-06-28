class Error(Exception):
    """ Base class for other exceptions """
    pass


class AgeToSmallError(Error):
    """ Raised when Age is smaller than 18 """
    pass


print("----------------------------------Welcome To Voting Age check Scenario-------------------------------")
while True:
    try:
        num = int(input("Please Enter your to Age for voting criteria :\n"))
        if num < 18:
            raise AgeToSmallError
        elif num > 18:
         break
    except AgeToSmallError:
        print("Sorry!! Age too small to cast vote, Try_Again", num, 'years')
        print()
print("Congratulations!! You are eligible for voting as your age is : ", num, 'Years')
print('------------------------------------End of the program-------------------------------------------------')
