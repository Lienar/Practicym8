import matplotlib.pyplot as plt
import pandas as pd
import data_save as ds
import plotly.graph_objects as go
import plotly as plotly
import plotly.subplots as ps
import warnings


def create_and_save_plot(data, ticker, period, stile, filename=None):
    plt.figure(figsize=(24, 12))
    plt.rcParams.update({'font.size': stile['font_size']})
    graf_names = stile['graf_names']

    if 'Date' not in data:
        if pd.api.types.is_datetime64_any_dtype(data.index):
            dates = data.index.to_numpy()
            plt.plot(dates, data['Close'].values, label=stile[f'{graf_names[0]}'],
                     linestyle=stile[f'{graf_names[0]}_stile'], color=stile[f'{graf_names[0]}_color'],
                     marker=stile[f'{graf_names[0]}_mark'], markerfacecolor=stile[f'{graf_names[0]}_mark_color'],
                     markersize=stile[f'{graf_names[0]}_mark_size'])
            plt.plot(dates, data['Moving_Average'].values, label=stile[f'{graf_names[1]}'],
                     linestyle=stile[f'{graf_names[1]}_stile'], color=stile[f'{graf_names[1]}_color'],
                     marker=stile[f'{graf_names[1]}_mark'], markerfacecolor=stile[f'{graf_names[1]}_mark_color'],
                     markersize=stile[f'{graf_names[1]}_mark_size'])
            plt.grid(stile['grid'], which='both')
        else:
            print("Информация о дате отсутствует или не имеет распознаваемого формата.")
            return
    else:
        if not pd.api.types.is_datetime64_any_dtype(data['Date']):
            data['Date'] = pd.to_datetime(data['Date'])
        plt.plot(data['Date'], data['Close'], label=stile[f'{graf_names[0]}'],
                 linestyle=stile[f'{graf_names[0]}_stile'], color=stile[f'{graf_names[0]}_color'],
                 marker=stile[f'{graf_names[0]}_mark'], markerfacecolor=stile[f'{graf_names[0]}_mark_color'],
                 markersize=stile[f'{graf_names[0]}_mark_size'])
        plt.plot(data['Date'], data['Moving_Average'], label=stile[f'{graf_names[1]}'],
                 linestyle=stile[f'{graf_names[1]}_stile'], color=stile[f'{graf_names[1]}_color'],
                 marker=stile[f'{graf_names[1]}_mark'], markerfacecolor=stile[f'{graf_names[1]}_mark_color'],
                 markersize=stile[f'{graf_names[1]}_mark_size'])
        plt.grid(stile['grid'], which='both')

    plt.title(f"{ticker} Цена акций с течением времени", color=stile['font_color'])
    plt.xlabel("Дата", color=stile['font_color'])
    plt.ylabel("Цена", color=stile['font_color'])
    plt.legend()

    file_data = ds.file_name_creator(filename, period, ticker, 'Default')

    plt.savefig(file_data[0])
    print(f"График сохранен как {file_data[0]}")

def RSI_plot(data, period, ticker, name, stile, filename=None):
    ''' Функция создания файла с графиком RSI по заданным значениям '''
    plt.figure(figsize=(24, 12))
    plt.rcParams.update({'font.size': stile['font_size']})
    graf_names = stile['graf_names']
    ''' Настройка окна графика и шрифа в нем '''
    if 'Date' not in data:
        if pd.api.types.is_datetime64_any_dtype(data.index):
            dates = data.index.to_numpy()
            plt.plot(dates, data['rsi'].values, label=stile[f'{graf_names[2]}'],
                     linestyle=stile[f'{graf_names[2]}_stile'], color=stile[f'{graf_names[2]}_color'],
                     marker=stile[f'{graf_names[2]}_mark'], markerfacecolor=stile[f'{graf_names[2]}_mark_color'],
                     markersize=stile[f'{graf_names[2]}_mark_size'])
        else:
            print("Информация о дате отсутствует или не имеет распознаваемого формата.")
            return
    else:
        if not pd.api.types.is_datetime64_any_dtype(data['Date']):
            data['Date'] = pd.to_datetime(data['Date'])
        plt.plot(data['Date'], data['rsi'], label=stile[f'{graf_names[2]}'],
                 linestyle=stile[f'{graf_names[2]}_stile'], color=stile[f'{graf_names[2]}_color'],
                 marker=stile[f'{graf_names[2]}_mark'], markerfacecolor=stile[f'{graf_names[2]}_mark_color'],
                 markersize=stile[f'{graf_names[2]}_mark_size'])
    ''' Отрисовка графика по дате и значениям RSI '''
    plt.title(f"RSI {name} ({ticker}) с течением времени")
    plt.xlabel("Дата")
    plt.ylabel("RSI индекс")
    plt.grid()
    plt.legend()
    ''' Отрисовка информации по графику '''
    file_data = ds.file_name_creator(filename, period, ticker, 'RSI')
    ''' Определение имени сохраняемого файла '''
    plt.savefig(file_data[0])
    ''' Сохранение графика '''
    print(f"График сохранен в {file_data[1]} имя файла {file_data[2]}")
    ''' Сообщение о создание файла с его данными '''

def Standard_deviation_and_values_plot(data, period, ticker, name, stile, filename=None):
    ''' Функция создания файла с графиком стандартного отклонения исходя из заданных значений '''
    plt.figure(figsize=(24, 12))
    plt.rcParams.update({'font.size': stile['font_size']})
    ''' Настройка окна графика и шрифа в нем '''
    for work_object in data['dev_window']:
        window_size = work_object
    full_window = (window_size * 2) + 1
    graf_names = stile['graf_names']
    if stile[f'{graf_names[3]}_mark'] == None:
        stile[f'{graf_names[3]}_mark'] = 'o'
    ''' Настройка дополнительных параметров '''
    if 'Date' not in data:
        if pd.api.types.is_datetime64_any_dtype(data.index):
            dates = data.index.to_numpy()
            ax = plt.subplot()
            ax.errorbar(dates, data['Close'].values, data['Standart_deviation'].values,
                        fmt=stile[f'{graf_names[3]}_mark'], linewidth=2, capsize=6, label=stile[f'{graf_names[3]}'],
                        markerfacecolor=stile[f'{graf_names[3]}_mark_color'], ecolor=stile[f'{graf_names[3]}_color'])
        else:
            print("Информация о дате отсутствует или не имеет распознаваемого формата.")
            return
    else:
        if not pd.api.types.is_datetime64_any_dtype(data['Date']):
            data['Date'] = pd.to_datetime(data['Date'])
        ax = plt.subplot()
        ax.errorbar(data['Date'], data['Close'], data['Standart_deviation'], fmt=stile[f'{graf_names[3]}_mark'],
                    linewidth=2, capsize=6, label=stile[f'{graf_names[3]}'],
                    markerfacecolor=stile[f'{graf_names[3]}_mark_color'], ecolor=stile[f'{graf_names[3]}_color'])
    ''' Отрисовка графика по дате и значениям закрытия с указанием стандартного отклонения '''
    if period[0] == 'PP':
        plt.title(f"Стандартное отклонение для окна в {full_window} соседних значений компании {name} "
                  f"({ticker}) за период {period[1]} ")
    if period[0] == 'DP':
        plt.title(f"Стандартное отклонение для окна в {full_window} соседних значений компании {name}  \n"
                  f"({ticker}) за период c {period[1]} по {period[2]}")
    plt.xlabel("Дата")
    plt.ylabel("Цена закрытия")
    plt.grid()
    plt.legend()
    ''' Отрисовка информации по графику '''
    file_data = ds.file_name_creator(filename, period, ticker, 'SD1')
    ''' Определение имени сохраняемого файла '''
    plt.savefig(file_data[0])
    ''' Сохранение графика '''
    print(f"График сохранен в {file_data[1]} имя файла {file_data[2]}")
    ''' Сообщение о создание файла с его данными '''

def Standard_deviation_plot(data, period, ticker, name, stile, filename=None):
    ''' Функция создания файла с графиком стандартного отклонения без привязки к значениям '''
    plt.figure(figsize=(18, 12))
    plt.rcParams.update({'font.size': stile['font_size']})
    ''' Настройка окна графика и шрифа в нем '''
    for work_object in data['dev_window']:
        window_size = work_object
    full_window = (window_size * 2) + 1
    graf_names = stile['graf_names']
    if stile[f'{graf_names[3]}_mark'] == None:
        stile[f'{graf_names[3]}_mark'] = 'o'
    ''' Настройка дополнительных параметров '''
    if 'Date' not in data:
        if pd.api.types.is_datetime64_any_dtype(data.index):
            dates = data.index.to_numpy()
            plt.plot(dates, data['Standart_deviation'].values, label=stile[f'{graf_names[4]}'],
                     linestyle=stile[f'{graf_names[4]}_stile'], color=stile[f'{graf_names[4]}_color'],
                     marker=stile[f'{graf_names[4]}_mark'], markerfacecolor=stile[f'{graf_names[4]}_mark_color'],
                     markersize=stile[f'{graf_names[4]}_mark_size'])
        else:
            print("Информация о дате отсутствует или не имеет распознаваемого формата.")
            return
    else:
        if not pd.api.types.is_datetime64_any_dtype(data['Date']):
            data['Date'] = pd.to_datetime(data['Date'])
        plt.plot(data['Date'], data['Standart_deviation'], label=stile[f'{graf_names[4]}'],
                 linestyle=stile[f'{graf_names[4]}_stile'], color=stile[f'{graf_names[4]}_color'],
                 marker=stile[f'{graf_names[4]}_mark'], markerfacecolor=stile[f'{graf_names[4]}_mark_color'],
                 markersize=stile[f'{graf_names[4]}_mark_size'])
    ''' Отрисовка графика стандартного отклонения по датам '''
    if period[0] == 'PP':
        plt.title(f"Стандартное отклонение для окна в {full_window} соседних значений компании {name} "
                  f"({ticker}) за период {period[1]} ")
    if period[0] == 'DP':
        plt.title(f"Стандартное отклонение для окна в {full_window} соседних значений компании {name}  \n"
                  f"({ticker}) за период c {period[1]} по {period[2]}")
    plt.xlabel("Дата")
    plt.ylabel("Цена закрытия")
    plt.grid()
    plt.legend()
    ''' Отрисовка информации по графику '''
    file_data = ds.file_name_creator(filename, period, ticker, 'SD2')
    ''' Определение имени сохраняемого файла '''
    plt.show()
    print(file_data)
    plt.savefig(file_data[0])
    ''' Сохранение графика '''
    print(f"График сохранен в {file_data[1]} имя файла {file_data[2]}")
    ''' Сообщение о создание файла с его данными '''

def create_interactive_chart(data, period, ticker, name):
    ''' Функция создания интерактивного графика'''
    warnings.simplefilter(action='ignore', category=FutureWarning)
    ''' Отключение вывода данных по предупреждениям в консоль'''
    if 'Date' not in data:
        if pd.api.types.is_datetime64_any_dtype(data.index):
            dates = data.index.to_numpy()
            fig1 = go.Scatter(x=dates, y=data['Close'].values, name='Close price',
                              marker=dict(color='red', line=dict(color='black', width=1)),)
            fig2 = go.Scatter(x=dates, y=data['ave'], name='Average close price',
                              marker=dict(color='blue', line=dict(color='red', width=1)),)
        else:
            print("Информация о дате отсутствует или не имеет распознаваемого формата.")
            return
    else:
        if not pd.api.types.is_datetime64_any_dtype(data['Date']):
            data['Date'] = pd.to_datetime(data['Date'])
        fig1 = go.Scatter(x=data['Date'], y=data['Close'], name='Close price',
                          marker=dict(color='red', line=dict(color='black', width=1)),)
        fig2 = go.Scatter(x=data['Date'], y=data['ave'], name='Average close price',
                          marker=dict(color='blue', line=dict(color='blue', width=1)),)
    ''' Отрисовка графика стандартного отклонения по датам '''
    fig = ps.make_subplots(rows=1, cols=1, vertical_spacing=0.5, x_title='Дата', y_title='Значение цены')
    if period[0] == 'PP':
        fig.update_layout(title=f"Цена закрытия с отображением линии средней цены "
                                f"компании {name} ({ticker}) за период {period[1]} ")
    if period[0] == 'DP':
        fig.update_layout(title=f"Цена закрытия с отображением линии средней цены "
                                f"компании {name} ({ticker}) за период c {period[1]} по {period[2]} ")
    ''' Создание общего графика для отображения с названием '''
    fig.add_trace(fig1)
    fig.add_trace(fig2)
    ''' Добавление графиков значений на основной'''
    fig.show()
    ''' Вывод результирующего графика'''



