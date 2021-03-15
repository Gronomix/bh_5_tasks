"""
Написать функцию common_numbers, которая принимает 2 списка, которые содержат
целые числа.

Функция должна вернуть список общих чисел, который отсортирован по убыванию
"""

some_list1 = [1, 2, 3, 11, 25, 5, 8]
some_list2 = [7, 11, 33, 8, 25]

def common_numbers(some_list1: list, some_list2: list):
    common_list = []

    for i in some_list1:
        if i in some_list2:

            common_list.append(i)
            common_list.sort(reverse=True)


    return common_list





sum_list = common_numbers(some_list1,some_list2)
print(sum_list)

