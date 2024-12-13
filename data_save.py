import pandas as pd
import os

def export_data_to_csv(data, filename):
    ''' Функция сохранения данных как CSV файла '''
    file_path = f'{os.path.dirname(__file__)}\\database'
    full_filename = f"{file_path}\\{filename}.csv"
    ''' Задание полного имени файла '''
    data.to_csv(full_filename, sep='\t', encoding='utf-8', index=False, header=True)
    ''' Запись данных в файл '''
    print(f"Данные записаны в файл {full_filename}")
    ''' Сообщение о записи файла '''


def file_name_creator(filename, period, ticker, plotting_type):
    ''' Функция создания имени файла и пути к нему '''
    file_path = f'{os.path.dirname(__file__)}\\Screens'
    ''' Определение пути к файлу '''
    if plotting_type == 'RSI':
        file_path = f'{file_path}\\RSI'
        if filename is None:
            if period[0] == 'PP':
                filename = f"{ticker}_{period[1]}_RSI"
            elif period[0] == 'DP':
                filename = f"{ticker}_data_from_{period[1]}_to_{period[2]}_RSI"
            else:
                filename = f"{ticker}_1mo_RSI"
    elif plotting_type == 'SD2':
        file_path = f'{file_path}\\SD'
        if filename is None:
            if period[0] == 'PP':
                filename = f"{ticker}_{period[1]}_SD"
            elif period[0] == 'DP':
                filename = f"{ticker}_data_from_{period[1]}_to_{period[2]}_SD"
            else:
                filename = f"{ticker}_1mo_SD"
    elif plotting_type == 'SD1':
        file_path = f'{file_path}\\SD'
        if filename is None:
            if period[0] == 'PP':
                filename = f"{ticker}_{period[1]}_SD&V"
            elif period[0] == 'DP':
                filename = f"{ticker}_data_from_{period[1]}_to_{period[2]}_SD&V"
            else:
                filename = f"{ticker}_1mo_SD&V"
    else:
        file_path = f'{file_path}\\Default'
        if filename is None:
            if period[0] == 'PP':
                filename = f"{ticker}_{period[1]}_stock_price_chart"
            elif period[0] == 'DP':
                filename = f"{ticker}_data_from_{period[1]}_to_{period[2]}_stock_price_chart"
            else:
                filename = f"{ticker}_data_1mo_stock_price_chart"
        ''' Проверка на наличие базового имени '''
    full_filename = f"{file_path}\\{filename}.png"
    ''' Создание полного пути '''
    file_data = [full_filename, file_path, filename]
    ''' Формироваание возвращаемых данных '''
    return file_data