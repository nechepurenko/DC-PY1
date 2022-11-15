import random


def get_unique_list_numbers(start=-10, stop=10, size=15) -> list[int]:
    list_ = []  # TODO написать функцию для получения списка уникальных целых чисел
    while len(list_) < size:
        list_.append(random.randint(start, stop))
        [list_.pop(i) for i, x in enumerate(list_) if x in list_[:i]]
    return list_


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
