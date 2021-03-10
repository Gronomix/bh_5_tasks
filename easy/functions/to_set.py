"""
Написать функцию to_set, которая принимает список, а возвращает множество,
созданное из этого списка и длину этого множества
"""

some_list = [2, 4, 6, 8]

def to_set(some_list: list):
    some_set = set(some_list)
    print(some_set)
    result = len(some_set)
    print(result)
    return some_set, result

if __name__ == '__main__':
    print(to_set(some_list))






