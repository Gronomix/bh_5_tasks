"""
Напишите функцию to_dict(lst), которая принимает аргумент в виде списка и
возвращает словарь, в котором каждый элемент списка является и ключом и
значением. Предполагается, что элементы списка будут соответствовать
правилам задания ключей в словарях.

"""

some_list = [1, 2, 3, 4]
def to_dict(some_list: list):
    new_dict = dict(zip(some_list, some_list))
    return new_dict


slist = to_dict(some_list)
print(slist)
