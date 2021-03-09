"""
Написать композицию из функций (не чистых функций)

Имеется словарь SCHOOL_DATA с данными школы класс-количество учеников

- Функция incr_students, которая принимает SCHOOL_DATA, название класса и
    увеличивает количество учеников на 1
- Функция decr_students, которая принимает SCHOOL_DATA, название класса и
    уменьшает количество учеников на 1, но не меньше 0
- Функция add_class, которая принимает SCHOOL_DATA, название класса и добавляет
    класс в словарь с количеством учеников 0
- Функция remove_class, которая принимает SCHOOL_DATA, название класса и удаляет
    класс из словаря
- Функция calc_students, которая принимает SCHOOL_DATA и возвращает кол-во
    учеников во всей школе
"""
school_data = {
    '1a': 15,
    '1b': 23,
    '2a': 13,
    '2b': 30
}

def inc_students(school_data: dict):
    for value in school_data.values():
        if value > 1 and value == int:
            school_data = round(value + 1)

        return school_data





def derc_student(school_data: dict):
    value = school_data.values()
    for key, value in school_data.values():
        school_data[key] = round(value - 1)

        return school_data






def add_class(school_data:dict):

    some_class = {'3d': 0}
    school_data.update(some_class)
    print(school_data)
    return school_data



def remove_class(school_data:dict):
    school_data.pop('2a')
    return school_data



def calc_students(school_data: dict):
    total_income = 0.00
    for value in school_data.values():
       total_income += value

       return total_income




def calc_students1(school_data: dict):
    total_income = 0.00
    for value in school_data.values():
       total_income = sum(school_data.values())
       return total_income



print(calc_students1(school_data))
print(calc_students(school_data))
print(remove_class(school_data))
print(add_class(school_data))

print(inc_students(school_data))

