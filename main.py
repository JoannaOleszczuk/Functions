def add(a, b):
    return a + b


def divide(a, b):
    if b == 0:
        print("Do not divide by 0")
        return None
    else:
        return a / b


def substract(a, b):
    return a - b


def multiply(a, b):
    return a * b


print(add(2, 3))
print(divide(2, 0))
print(divide(4, 3))
print(substract(3, 4))
print(multiply(2, 5))

print(add(substract(2, 3), multiply(4, 5)))

