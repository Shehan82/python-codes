<<<<<<< HEAD
def is_leap(year):
    leap = False
    if ((year % 4 == 0 and year %  100 != 0) or year % 400 == 0):
        leap = True

    return leap


year = int(input())
=======
def is_leap(year):
    leap = False
    if ((year % 4 == 0 and year %  100 != 0) or year % 400 == 0):
        leap = True

    return leap


year = int(input())
>>>>>>> b082e08ec0d5b605e157dfaaf21892a493998a3f
print(is_leap(year))