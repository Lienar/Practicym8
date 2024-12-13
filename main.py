import data_download as dd
import data_plotting as dplt
import dates_check as dcheck
import data_calculate as dc
import data_save as ds


def main():
    print("Добро пожаловать в инструмент получения и построения графиков биржевых данных.")
    print("Вот несколько примеров биржевых тикеров, которые вы можете рассмотреть: AAPL (Apple Inc), GOOGL (Alphabet Inc), MSFT (Microsoft Corporation), AMZN (Amazon.com Inc), TSLA (Tesla Inc).")
    print("Общие периоды времени для данных о запасах включают: 1д, 5д, 1мес, 3мес, 6мес, 1г, 2г, 5г, 10л, с начала года, макс.")
    #print("Заданы процент колебаний: от 0 до 100")

    ticker = input("Введите тикер акции (например, «AAPL» для Apple Inc):»")
    period = period_choice()
    stile = plotting_stile()
    #threshold = input("Введите заданный процент колебаний (например, '5.23' для 5.23 процентов): ")
    #filename = input("Введите имя файла для сохранения данных: ")

    # Fetch stock data
    stock_data = dd.fetch_stock_data(ticker, period)

    # Add moving average to the data
    stock_data = dd.add_moving_average(stock_data)

    # Plot the data
    #dplt.create_and_save_plot(stock_data, ticker, period, stile)

    # Сalculate the average
    #average = dc.calculate_and_display_average_price(stock_data)

    # Checking for exceeding the threshold
    #dc.notify_if_strong_fluctuations(stock_data, threshold)

    # Export data to file
    #ds.export_data_to_csv(stock_data, filename)

    # Creat data with RSI
    #rsi_data = dd.data_for_RSI_calculate(stock_data)

    # Return company name by ticker
    name = dd.name_return(ticker)

    # Plot RSI
    #dplt.RSI_plot(rsi_data, period, ticker, name, stile)

    # Creat data for Standart deviation
    #SD_data = dd.data_for_standard_deviation_calculate(stock_data)

    # Plot Standard deviation & values
    #dplt.Standard_deviation_and_values_plot(SD_data, period, ticker, name, stile)

    # Plot Standart deviation
    #dplt.Standard_deviation_plot(SD_data, period, ticker, name, stile)

    # Creat data for close ave and all graph
    ave_data = dd.average_inteactive_graf_data_collector(stock_data)

    # Plot close price ave and all graph
    dplt.create_interactive_chart(ave_data, period, ticker, name)

def period_choice():
    ''' Функция определения периода для данных '''
    index = input("выберите способ определения временного периода. PP для предустановленых периодов или DP для вабора периода по датам: ")
    ''' Выбор способа определения периода '''
    if index == 'PP':
        print("Общие периоды времени для данных о запасах включают: 1д, 5д, 1мес, 3мес, 6мес, 1г, 2г, 5г, 10л, с начала года, макс.")
        period_temp = input("Введите период для данных (например, '1mo' для одного месяца): ")
        ''' Ввод предустановленного периода  '''
        period = [index, period_temp]
        ''' Формирование данных по предустановленноу периоду '''
    elif index == 'DP':
        print("Укажите первую и вторую даты в формате гггг-мм-дд (например 2005-04-22)")
        period1_temp = input("Введите дату начала периода: ")
        period1_temp = dcheck.dates_rechandge(period1_temp)
        ''' Ввод первой даты '''
        period2_temp = input("Введите дату окончания периода: ")
        period2_temp = dcheck.dates_rechandge(period2_temp)
        period_temp = dcheck.dates_order(period1_temp, period2_temp)
        ''' Ввод второй даты '''
        period = ['DP', (f'{period_temp[0][0]}-{period_temp[0][1]}-{period_temp[0][2]}'),
                        (f'{period_temp[1][0]}-{period_temp[1][1]}-{period_temp[1][2]}')]
        ''' Формирование данных по датам '''
    else:
        period = ['DD', '1mo']
        ''' Формирование данных по умолчанию '''
    return period

def plotting_stile():
    ''' Функция меню настройки стиля графика '''
    print('Для входа в меню настройки стиля графика введите Yes для пропуск No')
    is_enter = input('Хотите войти в меню: ')
    ''' Вывозапроса на вход в меню '''
    enter = 'in'
    graf_names = ['Close Price', 'Moving Average', 'RSI', 'Standard dev & values', 'Standard deviation']
    stile = {'grid': True, 'font_size': 14, 'font_color': 'black', 'graf_names': graf_names}
    mark_stile = [['точка', '.'], ['ромб', 'D'], ['круг', 'o'], ['треугольник вниз', 'v'], ['треугольник вверх', '^']]
    line_stile = [['Сплошная линия', 'solid'], ['Точка-точка', 'dotted'],
                  ['Тире-тире', 'dashed'], ['Точка-тире', 'dashdot']]
    palitra = [['черный', 'black'], ['красный', 'red'], ['синий', 'blue'], ['зеленый', 'green'],
               ['фиолетовый', 'purple'], ['серый', 'grey'], ['желтый', 'yellow']]
    palitra_index = 0
    for name in graf_names:
        stile[f'{name}'] = name
        stile[f'{name}_stile'] = line_stile[0][1]
        stile[f'{name}_stile_op'] = line_stile[0][0]
        stile[f'{name}_color'] = palitra[palitra_index][1]
        stile[f'{name}_color_op'] = palitra[palitra_index][0]
        stile[f'{name}_mark'] = None
        stile[f'{name}_mark_op'] = 'не отображается'
        stile[f'{name}_mark_color'] = palitra[palitra_index][1]
        stile[f'{name}_mark_color_op'] = palitra[palitra_index][0]
        stile[f'{name}_mark_size'] = 3
        palitra_index += 1
        if palitra_index > len(palitra):
            palitra_index = 0
    ''' Создание вспомогательных переменных '''
    if is_enter.lower() == 'yes':
        while enter.lower() != 'exit':
            print(' ')
            print('Выберите параметр для настройки')
            print(f'1. Размер текста текущие значение {stile['font_size']}')
            print(f'2. Цвет текста текущие значение {stile['font_color']}')
            print(f'3. Отображение сетки текущие значение {stile['grid']}')
            print('4. Подменю настройки графиков')
            enter = input('Введите номер пункта для установки значения или exit для выхода: ')
            ''' Отображение меню настройки '''
            if enter == '1':
                print(' ')
                font_size = int(input('Введите значение размера шрифта от 8 до 24: '))
                if font_size < 8:
                    font_size = 8
                    print('Размер шрифта слишком мал установлен минимальный размер')
                if font_size > 24:
                    font_size = 24
                    print('Размер шрифта слишком велик установлен максимальный размер')
                stile['font_size'] = font_size
                ''' Настройка размера шрифта '''
            if enter == '2':
                print(' ')
                print('Выберите параметр для настройки')
                for i in range(0, len(palitra)):
                    print(f'{i+1}. {palitra[i][0]}')
                index = input('Введите номер цвета: ')
                stile['font_color'] = palitra[int(index)-1][1]
                ''' Настройка цвета информационного текста '''
            if enter == '3':
                print(' ')
                is_grid = input('Введите Yes для отображения сетки и No чтобы их скрыть '
                                '(по умолчанию сетка отображается): ')
                if is_grid.lower() == 'yes':
                    stile['grid'] = True
                else:
                    stile['grid'] = False
                ''' Настройка отображения сетки '''
            if enter == '4':
                stile_graf_temp = grafs_plot_menu(stile, line_stile, palitra, mark_stile)
                index = 0
                for name in graf_names:
                    stile[f'{name}_stile'] = stile_graf_temp[0][index]
                    stile[f'{name}_color'] = stile_graf_temp[0][index + 1]
                    stile[f'{name}_mark'] = stile_graf_temp[0][index + 2]
                    stile[f'{name}_mark_color'] = stile_graf_temp[0][index + 3]
                    stile[f'{name}_mark_size'] = stile_graf_temp[0][index + 4]
                    index += 5
                index_op = 0
                for name in graf_names:
                    stile[f'{name}_stile_op'] = stile_graf_temp[1][index_op]
                    stile[f'{name}_color_op'] = stile_graf_temp[1][index_op + 1]
                    stile[f'{name}_mark_op'] = stile_graf_temp[1][index_op + 2]
                    stile[f'{name}_mark_color_op'] = stile_graf_temp[1][index_op + 3]
                    index_op += 4
                ''' Настройка отображения графиков '''
    return stile

def grafs_plot_menu(stile, line_stile, palitra, mark_stile):
    ''' Функция настройки параметров графики '''
    enter = 'in'
    graf_stile = []
    temp_graf_param = []
    return_data = []
    graf_names = stile['graf_names']
    for name in graf_names:
        graf_stile.append(stile[f'{name}_stile'])
        temp_graf_param.append(stile[f'{name}_stile_op'])
        graf_stile.append(stile[f'{name}_color'])
        temp_graf_param.append(stile[f'{name}_color_op'])
        graf_stile.append(stile[f'{name}_mark'])
        temp_graf_param.append(stile[f'{name}_mark_op'])
        graf_stile.append(stile[f'{name}_mark_color'])
        temp_graf_param.append(stile[f'{name}_mark_color_op'])
        graf_stile.append(stile[f'{name}_mark_size'])
        temp_graf_param.append(stile[f'{name}_mark_size'])
    ''' Настройка дополнительных параметров '''
    while enter.lower() != 'exit':
        print(' ')
        print('Выберите название графика для редактирования параметров')
        name_index = 1
        for name in graf_names:
            print(f'{name_index} {name}')
            name_index += 1
        print('для выхода введите exit')
        print(' ')
        enter = input('Введите номер позиции:')
        if enter.lower() != 'exit':
            name = graf_names[int(enter)-1]
            param_index = int((int(enter)-1) * (len(graf_stile)/len(graf_names)))
            choose_index = 'in'
        else:
            choose_index = 'exit'
        ''' Цикл выбора графика'''
        while choose_index != 'exit':
            plot_menu_for_graf(temp_graf_param, name, param_index)
            choose_index = input('Введите номер позиции: ')
            if choose_index == '1':
                print(' ')
                print('Выберите стиль линии графика')
                menu_attribute_plot(line_stile)
                temp_index = input('Введите номер стиля: ')
                if temp_index.lower() != 'back':
                    temp_index = int(temp_index)-1
                    graf_stile[param_index] = line_stile[temp_index][1]
                    temp_graf_param[param_index] = line_stile[temp_index][0]
                ''' Меню настройки стиля линий графика '''
            if choose_index == '2':
                print(' ')
                print('Выберите цвет линии графика')
                menu_attribute_plot(palitra)
                temp_index = input('Введите номер цвета: ')
                if temp_index.lower() != 'back':
                    temp_index = int(temp_index)-1
                    graf_stile[param_index + 1] = palitra[temp_index][1]
                    temp_graf_param[param_index + 1] = palitra[temp_index][0]
                ''' Меню настройки цвета линий графика '''
            if choose_index == '3':
                menu_attribute_plot(mark_stile)
                print('для отключения маркеров введите None')
                temp_index = input('Введите номер стиля: ')
                if temp_index == 'None':
                    graf_stile[param_index + 3] = None
                    temp_graf_param[param_index + 3] = 'не отображается'
                elif temp_index.lower() != 'back':
                    temp_index = int(temp_index)-1
                    graf_stile[param_index + 2] = mark_stile[temp_index][1]
                    temp_graf_param[param_index + 2] = mark_stile[temp_index][0]
                ''' Меню настройки вывода меток на значениях '''
            if choose_index == '4':
                print(' ')
                print('Выберите цвет маркера: ')
                menu_attribute_plot(palitra)
                temp_index = input('Введите номер цвета: ')
                if temp_index.lower() != 'back':
                    temp_index = int(temp_index)-1
                    graf_stile[param_index + 3] = palitra[temp_index][1]
                    temp_graf_param[param_index + 3] = palitra[temp_index][0]
                ''' Меню настройки цвета меток на значениях '''
            if choose_index == '5':
                temp_size = int(input('Выберите размер маркера от 1 до 10:'))
                if temp_size < 1:
                    temp_size = 1
                if temp_size > 10:
                    temp_size = 10
                graf_stile[param_index + 4] = temp_size
                temp_graf_param[param_index + 4] = temp_size
                ''' Меню настройки размера меток на значениях '''
        print(' ')
        return_data = [graf_stile, temp_graf_param]
    return return_data

def plot_menu_for_graf(stile, name, index):
    ''' Функция отрисовки меню выбора изменяемого параметра графика '''
    print(' ')
    print(f'1. Выбор стиля линии графика {name} текущие значение {stile[index]}')
    print(f'2. Выбор цвет графика {name} текущие значение {stile[index + 1]}')
    print(f'3. Отображение меток значений для графика {name} текущие значение {stile[index + 2]}')
    print(f'4. Выбор цвета меток для графика {name} текущие значение {stile[index + 3]}')
    print(f'5. Выбор размера меток для графика {name} текущие значение {stile[index + 4]}')
    print('для выхода введите exit')
    print(' ')

def menu_attribute_plot(objects):
    ''' Функция отрисовки меню выбора значения изменяемого параметра графика '''
    index = 1
    for object in objects:
        print(f'{index} описание {object[0]}, обозначение {object[1]}')
        index += 1
    ''' Цикл отрисовки вариантов выборва '''
    print('для возврашения введите back')
    print(' ')


if __name__ == "__main__":
    main()

