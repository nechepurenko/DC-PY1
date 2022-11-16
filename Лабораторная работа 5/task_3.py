import random


def get_unique_list_numbers(start=-10, stop=10, size=15) -> list[int]:
    list_ = []  # TODO написать функцию для получения списка уникальных целых чисел
    while len(list_) < size:
        random_n = random.randint(start, stop)
        if random_n not in list_:
            list_.append(random_n)
    return list_


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
