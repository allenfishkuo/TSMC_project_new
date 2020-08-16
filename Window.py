# -*- coding: utf-8 -*-
import tkinter as Tk
import matplotlib 
matplotlib.use('TkAgg')
from numpy import arange, sin, pi
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg,NavigationToolbar2TkAgg
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import matplotlib.dates as mdates
import datetime

def show_win(denorm_pred, denorm_ytest, sold_list, sold_list_y, foxconndf, new_pred, buy_list, buy_list_y):
    matplotlib.use('TkAgg')
    root =Tk.Tk()
    root.title("TSMC")
    #设置图形尺寸与质量
    f =Figure(figsize=(10,5), dpi=100)
    a = f.add_subplot(111)
    #绘制图形
    
    a.grid(True)
    #a.plot_date(foxconndf['日期'][len(foxconndf['日期'])-315:len(foxconndf['日期'])], denorm_pred, fmt='o', tz=None, xdate=True, ydate=False,color='red', label='Prediction')
    #a.set_axes_locator
    a.plot(denorm_pred,color='red', label='Prediction')
    a.plot(denorm_ytest,color='blue', label='Answer')
    for i in range(len(sold_list)):
        a.scatter(sold_list[i], sold_list_y[i], s=100, c='black', alpha=1,marker='v')
        a.annotate(foxconndf['日期'][len(foxconndf['日期'])-len(new_pred)+sold_list[i]], 
                   xy=(sold_list[i], sold_list_y[i]), xytext=(sold_list[i]+5, sold_list_y[i]+5),
                arrowprops=dict(facecolor='white', shrink=0.05,frac=5,width=0.05),horizontalalignment='right',verticalalignment='top')
    for i in range(len(buy_list)):
        a.scatter(buy_list[i], buy_list_y[i], s=100, c='orange', alpha=1,marker='^')
        a.annotate(foxconndf['日期'][len(foxconndf['日期'])-len(new_pred)+buy_list[i]], 
                   xy=(buy_list[i], buy_list_y[i]), xytext=(buy_list[i]-5, buy_list_y[i]-5),
                arrowprops=dict(facecolor='gray', shrink=0.05,frac=5,width=0.05),horizontalalignment='left',verticalalignment='bottom')
    #把绘制的图形显示到tkinter窗口上
    canvas =FigureCanvasTkAgg(f, master=root)
    canvas.show()
    canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)
    #把matplotlib绘制图形的导航工具栏显示到tkinter窗口上
    toolbar =NavigationToolbar2TkAgg(canvas, root)
    toolbar.update()
    canvas._tkcanvas.pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)
    #button =Tk.Button(master=root, text='Quit', command=quit)
    #button.pack(side=Tk.BOTTOM)
    Tk.mainloop()