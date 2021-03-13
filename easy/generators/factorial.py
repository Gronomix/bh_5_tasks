"""
Написать генератор factorial, который возвращает подряд числа факториала

Например:

factorial_gen = factorial()

next(factorial_gen) -> 1
next(factorial_gen) -> 2
next(factorial_gen) -> 6
next(factorial_gen) -> 24
"""
def factorial(x):
    a = 1
    b = 1
    if x == 0:
        a = 1
    if x < 0:
        print('введите правильное число')
    if x > 0:
        while b < x:
            a = a * b
            b += 1
            yield a

factorial_gen = factorial(20)

print(next(factorial_gen))
print(next(factorial_gen))
print(next(factorial_gen))
print(next(factorial_gen))
print(next(factorial_gen))
print(next(factorial_gen))
print(next(factorial_gen))
print(next(factorial_gen))
