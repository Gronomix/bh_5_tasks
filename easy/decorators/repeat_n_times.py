"""
Написать функцию bang, которая печатает "Boom"

Написать декоратор repeat_n_times, у которого есть параметр n.
Декоратор должен выполнить функцию bang n раз
"""


def repeat_n_times(bang):
    def wrapper(n):
        print('Результат')
        result = print( f'{bang * n}')
        return result

    return wrapper


def bang(n):
    print('BOOM \n')
    return

bang_func = bang(6)



print(bang_func)