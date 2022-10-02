import tkinter
from tkinter import *
from tkinter import scrolledtext

import sys

from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)

from Rosenbrock_function import makeData


def Lab_3_window():
    def draw():
        fig.clf()

        ax = fig.add_subplot(projection='3d')
        ax.plot_surface(x, y, z, rstride=5, cstride=5, alpha=0.5, cmap="inferno")
        canvas.draw()

        '''
        x_cs = []
        y_cs = []
        z_cs = []

        for i in range(len(x)):
            x_cs.append(x[i])
            y_cs.append(y[i])
            z_cs.append(z[i])
            txt.insert(INSERT, f"{i}) ({x_cs[i]})({y_cs[i]}) = {z_cs[i]}\n")

        for i in range(len(x_cs)):
            if i < (len(x_cs) - 1):
                ax.scatter(x_cs[i - 1], y_cs[i - 1], z_cs[i - 1], c="black", s=1, marker="s")
            else:
                ax.scatter(x_cs[i - 1], y_cs[i - 1], z_cs[i - 1], c="red")
                canvas.draw()
        '''

    def delete():
        txt.delete(1.0, END)

    window_lab_3 = tkinter.Tk()

    if ( sys.platform.startswith('win')): 
        window_lab_3.iconbitmap(r'pic/Pop_cat_open.ico')
    else:
        window_lab_3.iconbitmap(r'@pic/Pop_cat_open.xbm')

    window_lab_3.wm_title("Лабораторная работа № 3")

    x, y, z = makeData()

    fig = plt.figure()

    ax = fig.add_subplot(projection='3d')

    canvas = FigureCanvasTkAgg(fig, master=window_lab_3)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

    toolbar = NavigationToolbar2Tk(canvas, window_lab_3)
    toolbar.update()
    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

    lbl_1 = Label(window_lab_3, text="X")
    lbl_1.pack(side=LEFT, padx=5, pady=5)

    txt_1 = Entry(window_lab_3, width=10)
    txt_1.pack(side=LEFT, padx=5, pady=5)

    lbl_2 = Label(window_lab_3, text="Y")
    lbl_2.pack(side=LEFT, padx=5, pady=5)

    txt_2 = Entry(window_lab_3, width=10)
    txt_2.pack(side=LEFT, padx=5, pady=5)

    lbl_3 = Label(window_lab_3, text="Начальный шаг")
    lbl_3.pack(side=LEFT, padx=5, pady=5)

    txt_3 = Entry(window_lab_3, width=10)
    txt_3.pack(side=LEFT, padx=5, pady=5)

    lbl_4 = Label(window_lab_3, text="Число Итераций")
    lbl_4.pack(side=LEFT, padx=5, pady=5)

    txt_4 = Entry(window_lab_3, width=10)
    txt_4.pack(side=LEFT, padx=5, pady=5)

    lbl_5 = Label(window_lab_3, text="Функция Розенброка")
    lbl_5.pack(side=LEFT, padx=5, pady=5, anchor=N)

    lbl_5 = Label(window_lab_3, text="Консоль лог")
    lbl_5.pack(side=TOP, padx=5, pady=5)

    txt = scrolledtext.ScrolledText(window_lab_3, width=40, height=10)
    txt.pack(side=RIGHT, padx=5, pady=5)

    btn_del = Button(window_lab_3, text="Очистить лог", width=10, command=delete)
    btn_del.pack(side=RIGHT, padx=5, pady=5, anchor=S)

    btn = Button(window_lab_3, text="Выполнить", width=10, command=draw)
    btn.pack(side=RIGHT, padx=5, pady=5, anchor=S)

    tkinter.mainloop()
