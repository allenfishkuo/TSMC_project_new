# -*- coding: utf-8 -*-
from DataProcessing import ReadData, normalize, data_helper, denormalize
from model import build_model
from keras.callbacks import ModelCheckpoint
import numpy as np
from trans_info import info
from Window import show_win
from crawler import check_lastdate, run_
import datetime
import os

if __name__ == '__main__':
    stock_id='2330' #inout the stock IDs
    now = datetime.datetime.now()
    year_list = range (2005,now.year+1) #since 2007 to this year
    month_list = range(1,13)  # 12 months
    ex_year=0
    ex_mon=0
    ex_day=0
    exist=0
    ex_year,ex_mon,ex_day,exist =check_lastdate(ex_year, ex_mon, ex_day, exist)
    #run_(stock_id,year_list,month_list,ex_year, ex_mon, ex_day, exist)
    
    foxconndf = ReadData()
    foxconndf_norm= normalize(foxconndf)
    foxconndf_norm=foxconndf_norm[['開盤價','最低價','最高價','收盤價']]
    # 以20天為一區間進行股價預測
    X_train, y_train, X_test, y_test = data_helper(foxconndf_norm, 5)
    # 20天、5維
    model = build_model( 5, 4)
    
    #model.load_weights("weights.best.hdf5",by_name=False)
    
    filepath="weights.best.hdf5"
    checkpoint = ModelCheckpoint(filepath, monitor='val_mean_squared_error', verbose=1, save_best_only=True, mode='min')
    callbacks_list = [checkpoint]
    # 一個batch有128個instance，總共跑100個迭代
    history=model.fit( X_train, y_train, batch_size=50, epochs=100, validation_split=0.1,callbacks=callbacks_list, verbose=1)
    
    cvscores = []
    scores = model.evaluate(X_train, y_train, verbose=0)
    print("%s: %.2f%%" % (model.metrics_names[1], scores[1]*1000))
    cvscores.append(scores[0] * 100)
    print("%.2f%% (+/- %.2f%%)" % (np.mean(cvscores), np.std(cvscores)))
    
    # 用訓練好的 LSTM 模型對測試資料集進行預測
    pred = model.predict(X_test)
    #print(pred)
    #os.system("pause")
    # 將預測值與正確答案還原回原來的區間值
    denorm_pred = denormalize(foxconndf, pred)
    denorm_ytest = denormalize(foxconndf, y_test)
    #print(denorm_pred)
    #os.system("pause")
    new_pred=[]
    base=denorm_pred[0]
    #print(base)
    currnet=0
    for i in range(len(denorm_pred)):
        current=denorm_pred[i]
        #print(current)
        new_pred.append(current)
        print(len(new_pred))
    
    sold_list, sold_list_y, sold_date, buy_list, buy_list_y, sold_date = info(foxconndf, new_pred)
    show_win(denorm_pred, denorm_ytest, sold_list, sold_list_y, foxconndf, new_pred, buy_list, buy_list_y)