#Необходима программа с интерфейсом. Она должна выполнять обработку элементов прямоугольной матрицы B,
#что имеет N строк и M столбцов, что задаются пользователем. Необходимо определить, сколько нулевых
#элементов содержится в каждом из столбцов и строк. Результат сохранить в текстовом файле.
#pip3 install numpy

import numpy as np
from tkinter import *
from tkinter import messagebox
import math

root = Tk()     
root.title('Билет 14')    

#Задаём матрицы и считаем нули
def matrix1(x):
    matri = np.random.randint(1, size=(3, 3))
    #количество нулей в каждой строке
    zrow = np.sum(matri == 0, axis=1)
    #количество нулей в каждом столбце
    zcol = np.sum(matri == 0, axis=0)
    #Меняем текст лейблов
    labmat.config(text=matri)
    labzerow.config(text=zrow)
    labzercol.config(text=zcol)
    
def matrix2(x):
    matri = np.array([[2,0],[0,1],[0,0],[5,5]])
    #количество нулей в каждой строке
    zrow = np.sum(matri == 0, axis=1)
    #количество нулей в каждом столбце
    zcol = np.sum(matri == 0, axis=0)
    #Меняем текст лейблов
    labmat.config(text=matri)
    labzerow.config(text=zrow)
    labzercol.config(text=zcol)
    
def matrix3(x):
    matri = np.array([[5,5,5,5],[6,6,6,6],[3,3,3,3]])
    #количество нулей в каждой строке
    zrow = np.sum(matri == 0, axis=1)
    #количество нулей в каждом столбце
    zcol = np.sum(matri == 0, axis=0)
    #Меняем текст лейблов
    labmat.config(text=matri)
    labzerow.config(text=zrow)
    labzercol.config(text=zcol)
    
def matrix(x):
    rows = int(entN.get())
    cols = int(entM.get())
    matri = np.random.randint(2, size=(rows, cols))
    
    #количество нулей в каждой строке
    zrow = np.sum(matri == 0, axis=1)
    #количество нулей в каждом столбце
    zcol = np.sum(matri == 0, axis=0)
    #Меняем текст лейблов
    labmat.config(text=matri)
    labzerow.config(text=zrow)
    labzercol.config(text=zcol)
    
    # Создаем подписи
    headers = ['Матрица', 'Количество нулей в строках', 'Количество нулей в столбцах']

    # Сохраняем результаты в текстовый файл с подписями
    with open('results.txt', 'w') as f:
        np.savetxt(f, matri, fmt='%d', delimiter='\t', header=headers[0], comments='')
        np.savetxt(f, zrow, fmt='%d', delimiter='\t', header=headers[1], comments='')
        np.savetxt(f, zcol, fmt='%d', delimiter='\t', header=headers[2], comments='')
    
#Виджеты 
lab = Label(text='Введите количество строк и количество столбцов')
lab1 = Label(text='Строки') 
entN = Entry(width=5)
lab2 = Label(text='Столбцы')
entM = Entry(width=5)
lab0 = Label(text='   ') 
lab01 = Label(text='   ') 
lab02 = Label(text='   ') 
lab03 = Label(text='   ')
lab04 = Label(text='   ')
lab05 = Label(text='   ')
btn1 = Button (text='Задать матрицу')
btn01 = Button (text='Тест1')
btn02 = Button (text='Тест2')
btn03 = Button (text='Тест3')
labzerow0 = Label(text='Кол-во нулей в каждой строке (Первая, вторая и т.д. строка)')
labzercol0 = Label(text='Кол-во нулей в каждом столбце (Первый, второй и т.д. столбец')

#Виджеты для вывода данных
labmat = Label(text='   ')
labzerow = Label(text='   ')
labzercol = Label(text='   ')

#Меню и функции для него
def spr():
    messagebox.showinfo('СПРАВКА', 'Просто следуйте шагам на рабочем меню')
def kill():
    exit()
root.option_add('*tearOff', FALSE)
main_menu = Menu()
file_menu = Menu()
file_menu.add_command(label='Справка',command = spr)
file_menu.add_separator()
file_menu.add_command(label='Выход', command = kill)
main_menu.add_cascade(label='Меню', menu = file_menu)
root.config(menu=main_menu)


lab.pack()
lab0.pack()
lab1.pack()
entN.pack()
lab01.pack()
lab2.pack()
entM.pack()
lab02.pack()
lab03.pack()
btn01.pack()
btn02.pack()
btn03.pack()
btn1.pack()
lab04.pack()
labmat.pack()
lab05.pack()
labzerow0.pack()
labzerow.pack()
labzercol0.pack()
labzercol.pack()

btn01.bind("<ButtonPress>", matrix1)
btn02.bind("<ButtonPress>", matrix2)
btn03.bind("<ButtonPress>", matrix3)
btn1.bind("<ButtonPress>", matrix)

root.mainloop()
