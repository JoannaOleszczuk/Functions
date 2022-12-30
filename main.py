def add2(c):
    tmpSum = 0
    for i in c:
        tmpSum += i
    return tmpSum


print(add2([1, 2, 3, 4, 5]))


def multiply2(d):
    tmpMul = 1
    for i in d:
        tmpMul = tmpMul * i
    return tmpMul


print(multiply2([1, 2, 3, 4, 5]))


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

print("Factorial")

# n! = (n-1)*n*(n+1)*...*(n+i), n,i=int
# n*(n-1)!, n>1
def factorial(n):
    if n<0:
        return None
    elif n>1:
        return n*factorial(n-1)
    elif n==1:
        return 1
    elif n==0:
        return 0

print(factorial(10))

# factorial(3) = 3*factorial(2)=3*2*factorial(1)