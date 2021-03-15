"""
Написать рекурсивную функцию check_number, которая должна возвращать True,
если переданное ей число n является степенью двойки (1 тоже степень двойки) и 
False, если нет

Нельзя пользоваться операцией возведения в степень
"""

def check_number(n):

    i = 1
    result = 0
    while i < n:
        i = i * 2
    if i == n:
        result = 1
    else:
        result = 0
    if result == 1:
        return True
    else:
        return False

num = check_number(3)
print(num)

