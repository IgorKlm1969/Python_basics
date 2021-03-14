"""
1. Написать функцию num_translate(), переводящую числительные от 0 до 10
c английского на русский язык. Например:
 num_translate("one")
"один"
 num_translate("eight")
"восемь"
Если перевод сделать невозможно, вернуть None. Подумайте, как и где лучше
хранить информацию, необходимую для перевода: какой тип данных выбрать,
в теле функции или снаружи.

2. * (вместо задачи 1) Доработать предыдущую функцию num_translate_adv(): реализовать корректную работу с
числительными, начинающимися с заглавной буквы. Например: num_translate_adv("One") "Один" num_translate_adv("two")
"два" """
dict_english = {'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять',
                'six': 'шесь', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}


def num_translate(eng):
    """
    :param eng: ключ словаря dict_english
    :return: перевод по ключу или None

    """
    if len(eng) > 0 and eng.isalpha() and dict_english.get(eng.lower()):
        # print(english.istitle())
        if eng.istitle():
            english_high = eng.lower()
            dict_english[english_high] = dict_english[english_high].capitalize()
            print(dict_english[english_high])
        else:
            print(dict_english[eng])
    else:
        print('Ошибка: вне области значений(return: None)')
        return None


english: str = input('Ведите числительное от 0 до 10 на ангийском языке одним словом  ')
num_translate(english)
