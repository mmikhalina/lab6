# 1. За датою d, m, y визначити дату наступного і попереднього дня. В програмі врахувати наявність високосних років.
# Міхаліна Мирослав Олексанлрович 122-Д


days = range(1, 32)
months = range(1, 13)
years = range(1901, 2020)
while True:
    # перевірка умов
    while True:
        try:
            day = int(input('day: '))
            if day not in days:
                print('Неправильно введений день')
                continue

            month = int(input('months: '))
            if month not in months:
                print('Неправильно введений місяць')
                continue

            year = int(input('years: '))
            if year not in years:
                print('Вибеіть рік з цього проміжку (1901-2020)')
                continue
            break
        except ValueError:
            print('Тільки цифри!')
    # перевірка умов

    february = 28

    if year % 4 == 0:
        february = 29

    months_list = [['Январь', 31],
                   ['Февраль', february],
                   ['Март', 31],
                   ['Апрель', 30],
                   ['Май', 31],
                   ['Июнь', 30],
                   ['Июль', 31],
                   ['Август', 31],
                   ['Сентябрь', 30],
                   ['Октябрь', 31],
                   ['Ноябрь', 30],
                   ['Декабрь', 31]]

    if day > months_list[month - 1][1]:
        print('Different number of days')
        continue

    d, m, y = day, month, year
    d -= 1
    m -= 1
    if d < 1:
        m -= 1
        d = months_list[m][1]
    if m < 0:
        y -= 1
    previous_day = f'previous day: {d} - {months_list[m][0]} - {y}'

    d, m, y = day, month, year
    d += 1
    m -= 1
    if d > months_list[m][1]:
        m += 1
        d = 1
    if m > 11:
        m = 0
        y += 1
    next_day = f'next day: {d} - {months_list[m][0]} - {y}'

    print(previous_day)
    print(next_day)
    if input('Press "Enter" for continue: ') == '':
        continue
    break