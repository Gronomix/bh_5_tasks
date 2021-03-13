"""
Написать функцию reverse_dict, которая принимает словарь ключ-значение и
возвращает новый словарь, у которого ключи - значения первого, а значения -
ключи первого

Тело функции может состоять из одной строки!

"""
some_dict = {'one': 1, 'two': 2, 'tree': 3}

def reverse_dict(some_dict: dict):
    new_dict = dict(zip(some_dict.values(), some_dict.keys()))
    return new_dict

sdict = reverse_dict(some_dict)
print(sdict)