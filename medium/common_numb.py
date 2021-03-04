"""
Написать функцию common_numbers, которая принимает 2 списка, которые содержат
целые числа.

Функция должна вернуть список общих чисел, который отсортирован по убыванию
"""

some_list1 = [1, 2, 3]
some_list2 = [7, 11, 33]

def common_numbers(some_list1: list, some_list2: list):
    common_list = []
    for i in some_list1 and i in some_list2:
        if i == int:
            common_list.append(i)
            common_list.sort(reverse=True)
    else:
        print('ERROR')
    return common_list



print(common_list)

if __name__ == '__main__':
    print(common_numbers)


