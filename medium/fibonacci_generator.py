"""
Написать генератор fibonacci, которая принимает номер значения num_count
из чисел Фибоначчи и выводит на экран результат до заданного значения.

Номер значения нужно проверить

Пример:

fibonacci(0) -> 'Введите значение больше 1'
fibonacci(5)
1
2
3
5
8
Traceback (most recent call last):
File «C:/Python/Python3/python_generator.py», line 29, in
print(next(fib))
StopIteration
"""
def fibonacci(xterms):

    x1 = 0
    x2 = 1
    count = 0

    if xterms <= 0:
        print("Укажите целое число больше 0")
    elif xterms == 1:
        print("Последовательность Фибоначчи до", xterms, ":")
        print(x1)
    else:
        while count < xterms:
            xth = x1 + x2
            x1 = x2
            x2 = xth
            count += 1
            yield xth

fib = fibonacci(5)

print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
