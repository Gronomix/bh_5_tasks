"""
Напишите функцию yes_or_no, которая принимает список из целых чисел,
проходит по нему и выводит Yes, если число уже встречалось и No, если нет
"""

A = [10, 10, 23, 10, 123, 66, 78, 123]

def yes_or_no(A):
    for i in A:
        if A.count(i) >= 2:
            print('Yes')

        else:
            print('NO')
    return


num = yes_or_no(A)
print(num)
