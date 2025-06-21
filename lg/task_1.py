def isEven(value):
    return value % 2 == 0


def isEven2(num):
    return num % 10 in (0, 2, 4, 6, 8)


def isEven3(num):
    return (num & 1) == 0


print(isEven2(7))
test
