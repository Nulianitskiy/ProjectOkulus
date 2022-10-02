import tkinter
from tkinter import *
from tkinter import scrolledtext

import sys
import time

from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)

from gradient_d import makeData, Funct_consider


def Lab_1_window():
    def draw():
        fig.clf()

        ax = fig.add_subplot(projection='3d')
        ax.plot_surface(x, y, z, rstride=5, cstride=5, alpha=0.5, cmap="inferno")
        canvas.draw()

        res_x = txt_1.get()
        res_y = txt_2.get()
        res_step = txt_3.get()
        res_iterations = txt_4.get()

        x_cs, y_cs, z_cs = Funct_consider(float(res_x), float(res_y), float(res_step), int(res_iterations))

        for i in range(len(x_cs)):
            if i < (len(x_cs) - 1):
                ax.scatter(x_cs[i - 1], y_cs[i - 1], z_cs[i - 1], c="black", s=1, marker="s")
            else:
                ax.scatter(x_cs[i - 1], y_cs[i - 1], z_cs[i - 1], c="red")

            canvas.draw()
            txt.insert(INSERT, f"{i}) ({round(x_cs[i], 2)})({round(y_cs[i], 2)}) = {z_cs[i]}\n")

            window_lab_1.update() # Ты был очень близок. Тебе просто нужно было нагуглить эту функцию обновления отрисовки)
            time.sleep(0.5)


    def delete():
        txt.delete(1.0, END)

    window_lab_1 = tkinter.Tk()

    if ( sys.platform.startswith('win')): 
        window_lab_1.iconbitmap(r'pic/Pop_cat_open.ico')
    else:
        window_lab_1.iconbitmap(r'@pic/Pop_cat_open.xbm')

    window_lab_1.wm_title("Лабораторная работа № 1")

    x, y, z = makeData()

    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')

    canvas = FigureCanvasTkAgg(fig, master=window_lab_1)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=2)

    toolbar = NavigationToolbar2Tk(canvas, window_lab_1)
    toolbar.update()
    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=2)

    lbl_1 = Label(window_lab_1, text="X")
    lbl_1.pack(side=LEFT, padx=5, pady=5)

    txt_1 = Entry(window_lab_1, width=10)
    txt_1.pack(side=LEFT, padx=5, pady=5)

    lbl_2 = Label(window_lab_1, text="Y")
    lbl_2.pack(side=LEFT, padx=5, pady=5)

    txt_2 = Entry(window_lab_1, width=10)
    txt_2.pack(side=LEFT, padx=5, pady=5)

    lbl_3 = Label(window_lab_1, text="Начальный шаг")
    lbl_3.pack(side=LEFT, padx=5, pady=5)

    txt_3 = Entry(window_lab_1, width=10)
    txt_3.pack(side=LEFT, padx=5, pady=5)

    lbl_4 = Label(window_lab_1, text="Число Итераций")
    lbl_4.pack(side=LEFT, padx=5, pady=5)

    txt_4 = Entry(window_lab_1, width=10)
    txt_4.pack(side=LEFT, padx=5, pady=5)

    lbl_5 = Label(window_lab_1, text="Функция Химмельблау")
    lbl_5.pack(side=LEFT, padx=5, pady=5, anchor=N)

    lbl_5 = Label(window_lab_1, text="Консоль лог")
    lbl_5.pack(side=TOP, padx=5, pady=5)

    txt = scrolledtext.ScrolledText(window_lab_1, width=40, height=10)
    txt.pack(side=RIGHT, padx=5, pady=5)

    btn_del = Button(window_lab_1, text="Очистить лог", width=10, command=delete)
    btn_del.pack(side=RIGHT, padx=5, pady=5, anchor=S)

    btn = Button(window_lab_1, text="Выполнить", width=10, command=draw)
    btn.pack(side=RIGHT, padx=5, pady=5, anchor=S)

    tkinter.mainloop()
