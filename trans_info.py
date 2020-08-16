# -*- coding: utf-8 -*-

def info(foxconndf, new_pred):
    index1=0
    sold_list=[]
    buy_list=[]
    sold_list_y=[]
    buy_list_y=[]
    buy_date=[]
    sold_date=[]
    max=0
    
    #print(len(denorm_pred))
    i=1
    while(i<len(new_pred)):
        negative=0
        #print("i=",i)
        if new_pred[i-1]>new_pred[i]:
        
            negative=new_pred[i]-new_pred[i-1]
            t=i+1
            if t+10<len(new_pred):
                for j in range(10):
                    negative=negative+(new_pred[t+j]-new_pred[t+j-1])
                if negative<0 :
                    index1=i
                    i+=15
                    sold_list.append(index1)
                    sold_list_y.append(new_pred[index1][0])
                    sold_date.append(foxconndf['日期'][len(foxconndf['日期'])-len(new_pred)+index1])
                if negative>=0:
                    i+=1
                #negative=0
            else:
                i+=1
        else:
            i+=1
    min=0
    index2=0
    i=1
    while(i<len(new_pred)):
        positive=0
        if new_pred[i-1]<new_pred[i]:
            
            positive=new_pred[i]-new_pred[i-1]
            t=i+1
            if t+10<len(new_pred):
                for j in range(10):
                    positive=positive+(new_pred[t+j]-new_pred[t+j-1])
                    #print(negative)
                if positive>0:
                    index2=i
                    i+=15
                    buy_list.append(index2)
                    buy_list_y.append(new_pred[index2][0])
                    buy_date.append(foxconndf['日期'][len(foxconndf['日期'])-len(new_pred)+index1])
                if positive<=0:
                    i+=1
            else:
                i+=1
        else:
            i+=1
        
            
    #print('最終NG:',max)
    #print('最終PG:',min)   
    
    print('最佳賣點:',sold_list)
    print('最佳賣點:',sold_list_y)
    print('最佳賣點:',sold_date)
    print('最佳買點:',buy_list)
    print('最佳買點:',buy_list_y)  
    print('最佳賣點:',sold_date)  
    return sold_list, sold_list_y, sold_date, buy_list, buy_list_y, sold_date