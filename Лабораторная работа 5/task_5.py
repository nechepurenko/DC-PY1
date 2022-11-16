from random import sample
import string


def get_random_password(n=8) -> str:
    empty_password = ""  # TODO написать функцию генерации случайных паролей
    comb = string.ascii_letters + string.digits
    return empty_password.join(sample(comb, n))


print(get_random_password())
