API_KEY = 'a783c1ce2b4581b7f17a82d99418e8627fafcc0f2ecc5ec82ef6e04fc755674e'

import datetime

import matplotlib.pyplot as plt
import pandas as pd
from numpy.lib.stride_tricks import as_strided
from pandas.plotting import register_matplotlib_converters
from locale import currency
import time
import cryptocompare.cryptocompare as cc

ccobj = cc._set_api_key_parameter(API_KEY)
def get_data(crypto: str):

    data =cc.get_historical_price_day(crypto, currency='USD')
    df = data_to_dataframe(data)
    plot_data(df,crypto,'USD')
   
    

def plot_data(df, cryptocurrency, target_currency):
    
    register_matplotlib_converters()
    
    plt.figure()
    plt.title('{} / {} price data'.format(cryptocurrency, target_currency))
    plt.plot(df.index, df.close)
    plt.axhline(y=get_avg(cryptocurrency), color='r', linestyle='-')

    plt.show()
    
    


def data_to_dataframe(data):
    
    df = pd.DataFrame.from_dict(data)
    
    df['time'] = pd.to_datetime(df['time'], unit='s')
    df.set_index('time', inplace=True)
  
    
    return df
def get_avg(coin: str)->float:
    sum=0
    try:
        data =cc.get_historical_price_day(coin, currency='USD', limit=180)
    
        for i in data:

            sum+=i['close']
    
    except:
        print("problem z API")
        return 
    
    
    return sum/len(data)



def start()-> list:
    #zrobiłem tylko dla 20, ponieważ dal wszystkich 7000 cryptowalut czas pobrania danych przekraczał 10 min
    coins = ['BTC', 'ETH', 'DOGE', 'LUNA', 'ATOM', 'BNB', 'ADA', 'FTM', 'XRP', 'SHIB', 'DOT', 'MATIC', 'LINK', 'TRX', 'AVAX', 'NEAR', 'LTC', 'BCH', 'SAND', 'ETC']

    lista =[]


    for coin in coins:
        
        price = cc.get_price(coin, currency='USD', full=False)

        price = price[coin]['USD']
        avg = get_avg(coin)

        #wyliczam o ile procent cena z dzisiaj jest mniejsza/większa od średniej ceny z pół roku

        mark = (1 -  price/avg) * -100 
        mark = round(mark, 2)
        crypto = {
            'coin': coin,
            'mark': mark
        }
        lista.append(crypto)

        
    
    lista = sorted(lista, key=lambda d: d['mark']) 


    return lista
        
    