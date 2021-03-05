"""
Написать функцию multiply, которая принимает аргумент n.
и возвращает функцию closure, которая принимает аргумент x и возвращает x * n
"""


def multiply(n: int):
    def closure(x: int):
        result = n * x
        return result
    return closure



if __name__ == '__main__':
    add_two = multiply(2)
    print(add_two(123))


