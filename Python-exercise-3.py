#def odd_number(y =7):
#def even_number(x = 6):
   # return 
def isEven(number):
    return number % 2 == 0

def isOdd(number): 
    return number % 2 != 0

print(isEven(0))


# Not correct


assert isOdd(42) == False
assert isOdd(9999) == True
assert isOdd(-10) == False
assert isOdd(-11) == True
assert isOdd(3.1415) == False
assert isEven(42) == True
assert isEven(9999) == False
assert isEven(-10) == True
assert isEven(-11) == False
assert isEven(3.1415) == False
assert isEven(0) == True
assert isOdd(0) == False

