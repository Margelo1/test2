#! Дан текстовый файл, с клавиатуры вводится символ, вывести слова в которых
#встречается этот символ, вывесли сколько раз встречвется
#предусмотреть предварительный просмотр файла и результатов
#открыть файл в диалоговом режиме имя файла выбирается 

import os
from tkinter import *
from tkinter.filedialog import *
from tkinter import ttk
from tkinter import messagebox as mbx

def EXIT(event): #ВЫХОД ИЗ ПРОГРАММЫ
    root.destroy()

def CLEAR(event):#ОЧИСТКА ОКОН
    win1.delete(1.0, END)
    win2.delete(1.0, END)

def READPRINT(event): #СЧИТЫВАНИЕ ИЗ ФАЙЛА
    file = askopenfilename()
    f = open(file, 'r')
    win1.insert(END,f.read())
    f.close()
    
def TRANSFORM(event): #ФУНКЦИЯ ВЫВОДА СЛОВ И ПОДСЧИТЫВАНИЕ СИМВОЛА
    a = ((win1.get(1.0, END)).lower()).split('\n') #СЧИТЫВАНИЕ ТЕКСТА 
    b = (entry.get()).lower() #СЧИТЫВАНИЕ СИМВОЛА
    n = 0
    for word in a:
        for elem in word.split(' '): #ПРОХОД ПО КАЖДОМУ СЛОВУ ИЗ СПИСКА
            if b in elem: #ПРОХОД ПО КАЖДОМУ ЭЛЕМЕНТУ СЛОВА
                win2.insert(END,elem+'\n')
                n+=1
    win2.insert(END,'\n' + 'Встречается ' + str(n) +' раз' + '\n')
    
def SAVE(event): #СОХРАНЕНИЕ
    b = asksaveasfilename() 
    q = open(b, 'w')
    q.write(win2.get(1.0, END)+'\n')
    q.close()

def inf(num): #ИНФОРМАЦИЯ
    if os.path.exists('info.txt') == True:
        file_program = open('info.txt','r')
        info_program = file_program.read().split("\n\n")
        file_program.close()
        name_title_messeg = ['О программе','Об авторе','Инструкция']
        mbx.showinfo(name_title_messeg[num], info_program[num])
    else:
        mbx.showerror("Ошибка", 'Пункт меню "Справка" недоступен.')

# Основная программа
root = Tk()
root.resizable (width=False, height=False)
root.title('Символ')
fra=Frame(root,width=800,height=500,bg='lightblue')
fra.grid(row=0,column=0)
but1 = Button(fra, text="Выбор файла для чтения",font='Areal 12',bg='white',fg='black')
but1.place(x=75,y=10)
but2 = Button(fra, text="Выбор файла для записи",font='Areal 12',bg='white',fg='Black')
but2.place(x=510,y=10)
but3 = Button(fra, text="Начать",font='Areal 12',bg='white',fg='Black')
but3.place(x=250,y=450)
but_exit = Button(fra, text="Выход",font='Areal 12',bg='white',fg='Black')
but_exit.place(x=560,y=450)
but_clear = Button(fra, text="Очистка",font='Areal 12',bg='white',fg='Black')
but_clear.place(x=170,y=450)
entry = ttk.Entry()
entry.place(x=130,y=50)
label = Label(root, text='Введите символ')
label.place(x=20,y=50)
win1 = Text(fra, width = 40, height =20, font = 'Areal 12',bg='White',fg='Black')
win1.place(x=20,y=80)
win2 = Text(fra, width = 40, height =20, font = 'Areal 12',bg='White',fg='Black')
win2.place(x=415,y=80)
m = Menu(root)
root.config(menu=m)
Fm = Menu(m)
m.add_cascade(label='Меню',menu=Fm)
Fm.add_command(label='О программе', command = lambda: inf(0))
Fm.add_command(label = 'Об авторе', command = lambda: inf(1))
Fm.add_command(label = 'Инструкция', command = lambda: inf(2))
but1.bind("<Button-1>", READPRINT)
but3.bind("<Button-1>", TRANSFORM)
but2.bind("<Button-1>", SAVE)
but_exit.bind("<Button-1>", EXIT)
but_clear.bind("<Button-1>", CLEAR)
root.mainloop()

