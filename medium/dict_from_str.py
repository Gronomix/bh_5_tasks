"""
Написать функцию dict_from_str, которая принимает строковое значение STR_VAL,
из которого создает и возвращает словарь, следующего вида:
{
    'буква': количество-вхождений-в-строку
}

например: {
    'p': 2,
    'y': 1,
    ...
}
"""
STR_VAL = 'python is the fastest-growing major programming language'

def dict_from_str(STR_VAL):
    indecies = list(STR_VAL)
    values = (STR_VAL.count(a) for a in indecies)
    log_dict = dict(zip(indecies, values))

    return log_dict

som_dict = dict_from_str(STR_VAL)
print(som_dict)



