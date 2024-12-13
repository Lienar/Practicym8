from datetime import datetime


def dates_rechandge(data):
    ''' Функция преобразования дат для обработки '''
    data_temp = []
    index = 0
    index1 = 0
    index2 = 0
    ''' Создание вспомогательных параметров '''
    for simbol in data:
        if simbol == '-' and index1 == 0:
            index1 = index
        elif simbol == '-' and index1 != 0:
            index2 = index
        index += 1
    ''' Определения индексов разделителей '''
    data_temp = dates_correct_check([int(data[:index1]), int(data[index1+1:index2]), int(data[index2+1:])])
    ''' Преобразование даты из str в list'''
    return data_temp

def dates_correct_check(data):
    ''' Функция проверки корректности дат '''
    current_year = datetime.now().year
    current_month = datetime.now().month
    current_day = datetime.now().day
    month_big = [1, 3, 5, 7, 8, 10, 12]
    month_small = [4, 6, 9, 11]
    if data[0] % 4 != 0:
        leap_year = False
    elif data[0] % 100 == 0:
        if data[0] % 400 == 0:
            leap_year = True
        else:
            leap_year = False
    else:
        leap_year = True
    ''' Создание вспомогательных параметров '''
    if data[0] < 1000:
        if data[0] < 100:
            if (data[0] + 2000) <= current_year:
                data[0] += 2000
            else:
                data[0] += 1900
        else:
            if data[0] < 200:
                data[0] = data[0] - 100 + 1900
            else:
                data_temp = str(data[0])
                data[0] = int(data_temp[1])*10 + int(data_temp[2])
                data[0] += 2000
    if data[0] > current_year:
        data = [current_year, current_month, current_day]
    ''' Проверка года на соответствие '''
    if data[1] > 12:
        data_temp = str(data[1])
        data[1] = int(data_temp[1])
    if data[0] == current_year and data[1] > current_month:
        data = [current_year, current_month, current_day]
    ''' Проверка месяца на соответствие '''
    if not leap_year and data[1] > 28:
        data[1] = 28
    if leap_year and data[1] > 29:
        data[1] = 29
    for days in month_big:
        if data[1] == days and data[2] > 31:
            data[2] = 31
    for days in month_small:
        if data[1] == days and data[2] > 30:
            data[2] = 30
    ''' Проверка дня на соответствие '''
    return data

def dates_order(data1, data2):
    ''' Функция определения порядка дат '''
    month_big = [1, 3, 5, 7, 8, 10, 12]
    month_small = [4, 6, 9, 11]
    ''' Создание вспомогательных параметров '''
    if data1[0] > data2[0]:
        data_temp = [data2, data1]
        ''' Сортировка по годам '''
    elif data1[0] < data2[0]:
        data_temp = [data1, data2]
        ''' Сортировка по годам '''
    else:
        if data1[0] % 4 != 0:
            leap_year = False
            ''' Проверка года на високосность '''
        elif data1[0] % 100 == 0:
            if data1[0] % 400 == 0:
                leap_year = True
            else:
                leap_year = False
            ''' Проверка года на високосность '''
        else:
            leap_year = True
            ''' Проверка года на високосность '''
        if data1[1] > data2[1]:
            data_temp = [data2, data1]
            ''' Сортировка по месяцам '''
        elif data1[1] < data2[1]:
            data_temp = [data1, data2]
            ''' Сортировка по месяцам '''
        else:
            if data1[2] > data2[2]:
                data_temp = [data2, data1]
                ''' Сортировка по дням '''
            elif data1[2] < data2[2]:
                data_temp = [data1, data2]
                ''' Сортировка по дням '''
            else:
                if data1[2] - 1 > 0:
                    data1[2] -= 1
                else:
                    if data1[1] == 3:
                        data1[1] -= 2
                        if leap_year:
                            data1[2] = 29
                        else:
                            data1[2] = 28
                    else:
                        data_change = False
                        for days in month_big:
                            if data1[1] == days:
                                data1[2] -= 1
                                if data1[1] == 7:
                                    data1[2] = 31
                                else:
                                    data1[2] = 30
                                data_change = True
                        for days in month_small and not data_change:
                            if data1[1] == days:
                                data1[2] -= 1
                                data1[2] = 30
                ''' Преобразование дат в случае равенства '''
                data_temp = [data1, data2]
    ''' Формирование порядка дат '''
    return data_temp