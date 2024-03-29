import os

#
# RULES FOR LEAP YEAR
#
# if (year is not divisible by 4) then (it is a common year)
# else if (year is not divisible by 100) then (it is a leap year)
# else if (year is not divisible by 400) then (it is a common year)
# else (it is a leap year)
#
# TEST CASES:
#
# 2000 is a leap year
# 1900 is NOT a leap year
# 4 is a leap year
#
def isLeapYear(year):
    # Determine if a leap year
    # TODO: Add code here
    '''
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True
    '''

    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    return year % 4 == 0

year = int(os.sys.argv[1])
if isLeapYear(year):
    print '%d is a leap year' % year
else:
    print '%d is NOT a leap year' % year
