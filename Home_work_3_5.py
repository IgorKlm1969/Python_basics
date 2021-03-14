"""
Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из двух случайных слов, взятых из трёх списков:
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
        Например:
 get_jokes(2)
["лес завтра зеленый", "город вчера веселый"]

        # for random.choice(nouns), get_adverbs, get_adjectives in zip(ouns, adverbs, adjectives):
"""
import random

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(nums):
    """

    :param nums: int
    :return: выводит в терминал случайный набор слов из списков слов
    """
    for counts in range(nums):
        first_word = random.choice(nouns)
        second_word = random.choice(adverbs)
        third_word = random.choice(adjectives)
        print(f'{first_word} {second_word} {third_word}')


numbers = int(input('Введите количество повторов шуток, '))
get_jokes(numbers)
# get_jokes(3)
