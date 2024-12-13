import yfinance as yf
import warnings
import data_calculate as dc


def fetch_stock_data(ticker, period=['PP','1mo']):
    ''' Функция загрузки даты '''
    stock = yf.Ticker(ticker)
    ''' Указания на данные по тикеру '''
    if period[0] == 'PP':
        data = stock.history(period=period[1])
    elif period[0] == 'DP':
        data = stock.history(start=period[1], end=period[2])
    else:
        data = stock.history(period=period[1])
    ''' Фильтр данных по периоду '''
    return data


def add_moving_average(data, window_size=5):
    data['Moving_Average'] = data['Close'].rolling(window=window_size).mean()
    return data

def data_for_RSI_calculate(data):
    ''' Функция расчета RSI '''
    warnings.simplefilter(action='ignore', category=FutureWarning)
    ''' Отключение вывода данных по предупреждениям в консоль'''
    temp_data = data['Close'].copy(deep=True)
    work_data = temp_data.to_frame().reset_index()
    work_data = work_data.drop('Date', axis=1)
    ''' Выборка рабочих данных '''
    work_data['diff'] = work_data.diff(1)
    ''' Вычисление разницы цен '''
    work_data['gain'] = work_data['diff'].clip(lower=0).round(2)
    work_data['loss'] = work_data['diff'].clip(upper=0).abs().round(2)
    ''' Создание столбцов по прибыли и убыткам '''
    window_length = len(work_data['Close'])/10
    if window_length < 1:
        window_length = 1
    if window_length - int(window_length) < 0.6:
        window_length = int(window_length)
    else:
        window_length = int(window_length)+1
    ''' Вычисление размера окна для подсчета средних значений '''
    work_data['avg_gain'] = work_data['gain'].rolling(window=window_length,
                                                      min_periods=window_length).mean()[:window_length + 1]
    for i, row in enumerate(work_data['avg_gain'].iloc[window_length + 1:]):
        work_data['avg_gain'].iloc[i + window_length + 1] = \
            (work_data['avg_gain'].iloc[i + window_length] *
             (window_length - 1) +
             work_data['gain'].iloc[i + window_length + 1]) \
            / window_length
    ''' Создание столбца средней прибыли '''
    work_data['avg_loss'] = work_data['loss'].rolling(window=window_length,
                                                      min_periods=window_length).mean()[:window_length + 1]
    for i, row in enumerate(work_data['avg_loss'].iloc[window_length + 1:]):
        work_data['avg_loss'].iloc[i + window_length + 1] = \
            (work_data['avg_loss'].iloc[i + window_length] *
             (window_length - 1) +
             work_data['loss'].iloc[i + window_length + 1]) \
            / window_length
    ''' Создание столбца средним убыткам '''
    work_data['rs'] = work_data['avg_gain'] / work_data['avg_loss']
    ''' Создание столбца соотношения прибыли к убыткам '''
    work_data['rsi'] = 100 - (100 / (1.0 + work_data['rs']))
    ''' Создание столбца RSI '''
    work_data.index = data.index.tolist()
    ''' Добавление дат как индекса в базу '''
    return work_data

def data_for_standard_deviation_calculate(data):
    ''' Функция расчета среднего отклонения цены закрытия '''
    warnings.simplefilter(action='ignore', category=FutureWarning)
    ''' Отключение вывода данных по предупреждениям в консоль'''
    temp_data = data['Close'].copy(deep=True)
    work_data = temp_data.to_frame().reset_index()
    work_data = work_data.drop('Date', axis=1)
    ''' Выборка рабочих данных '''
    temp_data = []
    window_length = int(len(work_data['Close'])/10)
    if window_length < 1:
        window_length = 1
    ''' Создание дополнительных параметров'''
    for i in range(0, len(work_data['Close'])):
        if i - window_length <= 0:
            temp_data1 = work_data['Close'].loc[0:i + window_length]
            temp_data.append(temp_data1.std())
        elif i + window_length >= (len(work_data['Close']) - 1):
            temp_data1 = work_data['Close'].loc[i-window_length:(len(work_data['Close']) - 1)]
            temp_data.append(temp_data1.std())
        else:
            temp_data1 = work_data['Close'].loc[i-window_length:i+window_length]
            temp_data.append(temp_data1.std())
    ''' Расчет среднего стандартного отклонения'''
    work_data['Standart_deviation'] = temp_data
    work_data['dev_window'] = window_length
    ''' Формирование выходных данных '''
    work_data.index = data.index.tolist()
    ''' Добавление дат как индекса в базу '''
    return work_data

def name_return(ticker):
    ''' Функция нахождения имени компании по тикеру '''
    stock = yf.Ticker(ticker)
    ''' Выгрузка данных '''
    name = stock.info['longName']
    ''' Определение имени '''
    return name

def average_inteactive_graf_data_collector(data):
    ''' Функция расчета среднего отклонения цены закрытия '''
    warnings.simplefilter(action='ignore', category=FutureWarning)
    ''' Отключение вывода данных по предупреждениям в консоль'''
    temp_data = data['Close'].copy(deep=True)
    work_data = temp_data.to_frame().reset_index()
    work_data = work_data.drop('Date', axis=1)
    ''' Выборка рабочих данных '''
    work_ave = dc.calculate_and_display_average_price(data)
    work_data['ave'] = work_ave
    work_data.index = data.index.tolist()
    ''' Добавление дат как индекса в базу '''
    return work_data

    

