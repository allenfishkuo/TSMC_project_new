# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
from sklearn import preprocessing
import os


def ReadData():
    #Taiwan_stock=pd.read_csv('Taiwan_stock_price.csv')
    #print(Taiwan_stock)
    #dataset=pd.DataFrame()
    #dataset['Price_Rise'] = np.where(Taiwan_stock['Close'].shift(-1) > Taiwan_stock['Close'], 1, -1)
    #dataset['Price_Rise'] =Taiwan_stock['Close']
    #print(dataset)
    foxconndf= pd.read_csv('2330_stock_price.csv' )
    #foxconndf['Price_Rise']=dataset['Price_Rise'].values
    #print((foxconndf['日期'][len(foxconndf['日期'])-315:len(foxconndf['日期'])]))
    foxconndf.dropna(how='any',inplace=True)
    return foxconndf

def normalize(df):
    newdf= df.copy()
    min_max_scaler = preprocessing.MinMaxScaler()
    
    newdf['開盤價'] = min_max_scaler.fit_transform(df.開盤價.values.reshape(-1,1))
    newdf['最低價'] = min_max_scaler.fit_transform(df.最低價.values.reshape(-1,1))
    newdf['最高價'] = min_max_scaler.fit_transform(df.最高價.values.reshape(-1,1))
    newdf['收盤價'] = min_max_scaler.fit_transform(df.收盤價.values.reshape(-1,1))
    #newdf['Price_Rise'] = min_max_scaler.fit_transform(df.Price_Rise.values.reshape(-1,1))
    return newdf

def data_helper(df, time_frame):
    
    # 資料維度: 開盤價、收盤價、最高價、最低價、成交量, 5維
    number_features = len(df.columns)
    # 將dataframe 轉成 numpy array
    datavalue = df.as_matrix()
    result = []
    # 若想要觀察的 time_frame 為20天, 需要多加一天做為驗證答案
    for index in range( len(datavalue) - (time_frame+5) ): # 從 datavalue 的第0個跑到倒數第 time_frame+1 個
        result.append(datavalue[index: index + (time_frame+5) ]) # 逐筆取出 time_frame+1 個K棒數值做為一筆 instance
    
    result = np.array(result)
    number_train = round(0.9 * result.shape[0]) # 取 result 的前90% instance做為訓練資料
    
    #x_train = result[:int(number_train), :-1] # 訓練資料中, 只取每一個 time_frame 中除了最後一筆的所有資料做為feature
    #y_train = result[:int(number_train), -1][:,-1] # 訓練資料中, 取每一個 time_frame 中最後一筆資料的最後一個數值(收盤價)做為答案
    x_train = result[:int(number_train), :-5] # 訓練資料中, 只取每一個 time_frame 中除了最後一筆的所有資料做為feature
    y_train = result[:int(number_train), -5:][:,:,-1:] # 訓練資料中, 取每一個 time_frame 中最後一筆資料的最後一個數值(收盤價)做為答案
    #y_train = y_train.reshape(len(y_train),1,5)
    
    print(x_train.shape,'\n',y_train.shape)
    os.system("pause")
    
    # 測試資料
    #x_test = result[int(number_train):, :-1]
    #y_test = result[int(number_train):, -1][:,-1]
    x_test = result[int(number_train):, :-5]
    y_test = result[int(number_train):, -5:][:,:,-1:]
    #y_test = y_test.reshape(len(y_test),1,5)
    
    # 將資料組成變好看一點
    x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], number_features))
    x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], number_features))  
    return [x_train, y_train, x_test, y_test]

def denormalize(df, norm_value):
    original_value = df['收盤價'].values.reshape(-1,1)
    norm_value = norm_value.reshape(-1,1)
    
    min_max_scaler = preprocessing.MinMaxScaler()
    min_max_scaler.fit_transform(original_value)
    denorm_value = min_max_scaler.inverse_transform(norm_value)
    
    return denorm_value