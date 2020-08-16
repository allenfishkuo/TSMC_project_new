# -*- coding: utf-8 -*-
import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, LSTM, GRU, TimeDistributed
import os

def build_model(input_length, input_dim):
    d = 0.3
    model = Sequential()
    model.add(GRU(512, input_shape=(input_length, input_dim), return_sequences=True))
    model.add(Dropout(d))
    #model.add(GRU(256, input_shape=(input_length, input_dim), return_sequences=False))
    #model.add(Dropout(d))
    model.add(Dense(128,kernel_initializer="uniform",activation='relu'))
    model.add(Dense(64,kernel_initializer="uniform",activation='relu'))
    model.add(Dense(16,kernel_initializer="uniform",activation='relu'))
    model.add(Dense(5,kernel_initializer="uniform",activation='linear'))
    model.add(TimeDistributed(Dense(1)))
    model.compile(loss='mean_squared_error',optimizer='adam', metrics=['mean_squared_error'])
    
    
    
    return model