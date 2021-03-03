"""
Реализовать склонение слова «процент» для чисел до 20. Например, задаем число 5 — получаем «5 процентов»,
задаем число 2 — получаем «2 процента». Вывести все склонения для проверки.
"""




while True:
    end_of_procent = int(input('Введите количество процентов от 1 до 100'))

    if end_of_procent == 1 or (end_of_procent > 20 and end_of_procent % 10 == 1):
        print(end_of_procent, 'процент')
    elif 1 < end_of_procent <= 4 or (end_of_procent > 19 and 2 <= end_of_procent % 10 <= 4):
        print(end_of_procent, 'процента')
    elif 5 <= end_of_procent <= 19 or end_of_procent % 10 == 0 or 5 <= end_of_procent % 10 <= 9:
        print(end_of_procent, 'процентов')

