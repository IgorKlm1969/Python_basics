"""
Создать список, состоящий из кубов нечётных чисел от 1 до 1000:
Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
Например, число «19 ^ 3 = 6859» будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7.
Внимание: использовать только арифметические операции!
К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка,
сумма цифр которых делится нацело на 7.
* Решить задачу под пунктом b, не создавая новый список.

"""
list1 = []
for number in range(1, 1000, 2):
    # print(number)
    number = number ** 3
    list1.append(number)
    sorted(list1)

print('Кубы нечетных чисел от 1 до 1000\n', list1)

list_of_number = []
list_on_7 = []
d = 0
sum1 = 0
sum_of_list = 0
for number_in_l1 in list1:
    for d in str(number_in_l1):
        list_of_number.append(d)
        # print((list_of_number))
        sum1 += int(d)
        if sum1 % 7 == 0:
            list_on_7.append(sum1)
            for every_number in list_on_7:
                sum_of_list += every_number
print('Список чисел суммы цифр которых делятся на 7\n', list_on_7)
print('Сумма чисел, которые делятся на 7: \n', sum_of_list)

for ind in range(len(list_on_7)):
    list_on_7[ind] += 17

print(list_on_7)

list_of_number = []
list_on_7_sec = []
d = 0
sum1 = 0
sum_of_list = 0
for number_in_l1 in list_on_7:
    for d in str(number_in_l1):
        list_of_number.append(d)
        sum1 += int(d)
        if sum1 % 7 == 0:
            list_on_7_sec.append(sum1)
            for every_number in list_on_7_sec:
                sum_of_list += every_number
print('Список чисел суммы цифр которых делятся на 7, версия 2\n', list_on_7_sec)
print('Сумма чисел, которые делятся на 7, версия 2: \n', sum_of_list)
