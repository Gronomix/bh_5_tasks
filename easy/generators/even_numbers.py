"""
Написать генератор get_even_number, который возвращает подряд четные числа

Например:

even_gen = get_even_number()

next(even_gen) -> 2
next(even_gen) -> 4
next(even_gen) -> 6
"""
def get_ever_number(n: int):
    even = []

    for x in range(n):
        if x % 2 == 0:
            even.append(x)
    return even



if __name__ == '__main__':
    n = int(input('Ведите количество генерируемых значений '))
    even_gen = get_ever_number
    print(next(even_gen))