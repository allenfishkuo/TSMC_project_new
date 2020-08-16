# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt

def show_train_history(train_history, train, validation):
    plt.plot(train_history.history[train])
    plt.plot(train_history.history[validation])
    plt.title('Train History')
    if train=='mean_square_error':
        plt.ylabel('mean_square_error')
        plt.xlabel('Epoch')
        plt.legend(['train', 'validation'], loc='center right')
        plt.savefig('LSTM_mean_square_error_no.png',dpi=300)
        plt.show()
        
    '''
    if train=='loss':
        plt.ylabel('loss')
        plt.xlabel('Epoch')
        plt.legend(['train', 'validation'], loc='center right')
        #plt.show()
    '''  
    
    '''plt.plot(history.history['mean_squared_error'])
    plt.plot(history.history['val_mean_squared_error'])
    plt.title('Train History')
    plt.ylabel('mean_square_error')
    plt.xlabel('Epoch')
    plt.legend(['train', 'validation'], loc='center right')
    #plt.savefig("filename.png")
    plt.show()'''
    
    
    '''
    plt.plot(denorm_pred,color='red', label='Prediction')
    plt.plot(denorm_ytest,color='blue', label='Answer')
    
    for i in range(len(sold_list)):
        plt.scatter(sold_list[i], sold_list_y[i], s=1, c=0, alpha=1)
    plt.grid(True)
    
    for xval,yval in zip(sold_list,sold_list_y):
        plt.plot(xval,yval,color='g')
    plt.legend(loc='best')
    plt.show()
    '''