# -*- coding: utf-8 -*-
import requests
import json
import csv
import time, datetime,os
import random
import sys
import os
import pandas as pd
from bs4 import BeautifulSoup
dt = datetime.datetime.now()
dt.year
dt.month

def get_webmsg (year, month, stock_id):
    date = str (year) + "{0:0=2d}".format(month) +'01' ## format is yyyymmdd
    sid = str(stock_id)
    #proxies = {'http':'http://10.10.10.10:8765','https':'https://10.10.10.10:8765'}
    #headers = {'Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19'}
    
    url_twse = 'http://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date='+date+'&stockNo='+sid
    res =requests.post(url_twse)
    soup = BeautifulSoup(res.text , 'html.parser')
    smt = json.loads(soup.text)     #convert data into json
    #print(smt['data'][-1:][0][0][:3])
    #os.system("pause")
    return smt


def write_csv(smt, check,ex_year, ex_mon, ex_day) :
    #writefile = directory + filename               #set output file name
    if smt['stat'][0]!='OK':
        return
    if os.path.isfile('2330_stock_price.csv'):
        outputFile = open('2330_stock_price.csv','a',newline='',encoding='utf-8')
        outputWriter = csv.writer(outputFile)
        if check==2 :
            k=0
            for i in range(len(smt['data'])):
                check_date = "".join(smt['data'][i][0])
                check_year, check_month, check_day = check_date.split("/")
                check_year = int(check_year)
                check_month = int (check_month)
                check_day = int (check_day)
                if check_year==ex_year and check_month==ex_mon and check_day==ex_day:
                    k=1
                elif k==1:
                    print(check_year, check_month, check_day)
                    outputWriter.writerow(smt['data'][i])
            check+=1
        else:
            for data in (smt['data']):
                outputWriter.writerow(data)
    else:
        outputFile = open('2330_stock_price.csv','a',newline='',encoding='utf-8')
        outputWriter = csv.writer(outputFile)
        outputWriter.writerow(smt['fields'])
    outputFile.close()
def check_lastdate(ex_year, ex_mon, ex_day, exist):
    if os.path.isfile('2330_stock_price.csv'):
        exist = 1
        outputFile=pd.read_csv('2330_stock_price.csv', encoding = 'utf8')
        ex_date = outputFile['日期'][-1:]
        ex_date = "".join(ex_date)
        ex_year, ex_mon, ex_day = ex_date.split("/")
        ex_year = int(ex_year)
        ex_mon = int (ex_mon)
        ex_day = int (ex_day)
        print(ex_year, ex_mon, ex_day)
        return ex_year, ex_mon, ex_day, exist
    else:
        ex_year=93
        ex_mon=0
        ex_day=0
        return ex_year, ex_mon, ex_day, exist

#create a directory in the current one doesn't exist
def run_(stock_id,year_list,month_list,ex_year, ex_mon, ex_day,exist):    
    check=0
    for year in year_list:
        for month in month_list:
            if (dt.year == year and month > dt.month) :break  # break loop while month over current month
            if check<2 and exist==1:
                if check == 0 and year==1911+ex_year:
                    check+=1
                elif month == ex_mon-1 and check==1 :
                    check+=1
                elif check<1:
                    break
            else:
                print(year ,month)
                smt = get_webmsg(year ,month, stock_id)           #put the data into smt 
                write_csv (smt,check,ex_year, ex_mon, ex_day)    # write files into CSV
                check+=1
            time.sleep(random.randint(2,4))