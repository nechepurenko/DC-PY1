def get_count_char(str_):
    dict = {}
    DEFAULT_COUNT = 0
    str_lower = str_.lower()
    for letter in str_lower:# TODO посчитать количество каждой буквы в строке в аргументе str_
        if letter.isalpha():
            dict[letter] = dict.get(letter, DEFAULT_COUNT) + 1
    return dict

def perc_dict(dict_):
    sum_values = sum(dict_.values())
    for key in dict_:
        dict_[key] = round((dict_[key] / sum_values) * 100, 2)
    return dict_

main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
result = get_count_char(main_str)
print(perc_dict(result))
