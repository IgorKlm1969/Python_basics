"""
Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах:
до минуты: <s> сек;
до часа: <m> мин <s> сек;
до суток: <h> час <m> мин <s> сек;
* в остальных случаях: <d> дн <h> час <m> мин <s> сек. #duration_sec // 3600 < 0  and
"""

while True:
    duration_sec = int(input('Ведите время время в секундах '))

    if 0 <= duration_sec < 60:
        print('duration: ', duration_sec, '\n', duration_sec, ' сек.')

    elif 0 <= duration_sec < 3600:
        minutes = duration_sec // 60
        seconds = duration_sec % 60
        print('duration: ', duration_sec, '\n', minutes, 'мин', seconds, ' сек.')
    elif 0 <= duration_sec < 86400:
        ours = duration_sec // 3600
        minutes = (duration_sec % 3600) // 60
        seconds = duration_sec % 60
        print('duration: ', duration_sec, '\n', ours, 'час', minutes, 'мин', seconds, ' сек.')
    elif 0 <= duration_sec:
        days = duration_sec // 86400
        ours = (duration_sec - days * 86400) // 3600
        minutes = (duration_sec % 3600) // 60
        seconds = duration_sec % 60
        print('duration: ', duration_sec, '\n', days, 'дней', ours, 'час', minutes, 'мин', seconds, ' сек.')
