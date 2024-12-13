
def calculate_and_display_average_price(data):
    ''' Функция подсчет и отображение среднего значения цены при закрытии '''

    close_data = data["Close"]
    ''' Выделение данных по цене закрытия '''
    data_number = 0
    data_all = 0
    ''' Создание дополнительных переменных '''
    for data_temp in close_data:
        data_all += data_temp
        data_number += 1
    ''' Подсчет всех суммы всех закрытий и их числа '''
    data_average = data_all/data_number
    ''' Подсчет среднего арифметического значения '''
    print(f"Среднее значение цены закрытия {data_average:.6f}")
    ''' Вывод среднего арифметического значения '''
    return data_average


def notify_if_strong_fluctuations(data, threshold):
    ''' Функция вызова предупреждения при превышение порога '''

    close_data = data["Close"]
    ''' Выделение данных по цене закрытия '''
    work_data = []
    for data_temp in close_data:
        work_data.append(data_temp)
    ''' Формирование рабочего массива '''
    one_percent_value = work_data[0]/100
    ''' Определение размера одного процента '''
    for i in range(0, len(work_data)):
        for j in range(0, len(work_data) - i - 1):
            if float(work_data[j]) > float(work_data[j + 1]):
                tempo = work_data[j]
                work_data[j] = work_data[j + 1]
                work_data[j + 1] = tempo
    ''' Сортировка рабочего массива по возрастанию '''
    delta = (work_data[len(work_data) - 1] - work_data[0]) / one_percent_value
    ''' Определение величины колебания '''

    if delta > float(threshold):
        ''' Проверка на превышение порога '''
        print("Колебания превышают заданный процент")
        print(f"Колебания составили {delta:.2f} процентов")
        ''' Вывод результата если порог превышен '''
    else:
        print("Колебания не превышают заданный процент")
        print(f"Колебания составили {delta:.2f} процентов")
        ''' Вывод результата если порог не превышен  '''

