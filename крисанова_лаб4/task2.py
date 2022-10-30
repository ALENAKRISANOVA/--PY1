def get_count_char(str_):
    symbol_dict  = {}
    DEFAULT_CAUNT = 0
    new_str = str_.lower()
    for symbol in new_str:
        if symbol.isalpha():
            symbol_dict[symbol] = symbol_dict.get(symbol, DEFAULT_CAUNT)+1
    return symbol_dict

main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
new = get_count_char(main_str)

def get_percentage_dict(dict_):
        s = sum(dict_.values())
        for symbol in dict_.keys():
            dict_[symbol] /= s
            dict_[symbol] *= 100
        return dict_

print(get_count_char(main_str))

