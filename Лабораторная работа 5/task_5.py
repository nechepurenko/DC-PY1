from random import sample
import string
def get_random_password() -> str:
    empty_password = ""  # TODO написать функцию генерации случайных паролей
    length = 8
    comb = string.ascii_letters + string.digits
    return empty_password.join(sample(comb, length))

print(get_random_password())
