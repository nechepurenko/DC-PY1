import random
def get_unique_list_numbers() -> list[int]:
    list_ = [] # TODO написать функцию для получения списка уникальных целых чисел
    while len(set(list_)) < 15:
        list_.append(random.randint(-10, 10))
    return list(set(list_))


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
