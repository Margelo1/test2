from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from random import choice
import random

clicks = 0

def obprogramme():  
    messagebox.showinfo('Заголовок', 'Текст')

def obavtore():  
    messagebox.showinfo('Заголовок1', 'Текст1')
    
def click_button():
    global clicks
    
    clicks += 1
    # изменяем текст на кнопке
    btn = f"Clicks {generate}"
    
def generate():
    pas = ''
    for x in range(6): #Количество символов (6)
        pas = pas + random.choice(list('1,2,3,4,5,6,7,8,9,10'))
        lbl = Label(window, text="{pas}", command=click_button)
        lbl.grid(column=0, row=0)
        

def win():  
    messagebox.showinfo('ПОБЕДА', 'Вы победили!')
def loss():
    messagebox.showinfo('ПРОИГРЫШЬ', 'Вы проиграли...')


window = Tk()  
window.title("Удивительные цифровые билеты!")  
window.geometry('400x250')

menu = Menu(window)  
new_item = Menu(menu)  
new_item.add_command(label='О программе',command = obprogramme)  
new_item.add_command(label='Об авторе',command = obavtore )  
menu.add_cascade(label='Помощь', menu=new_item)  
window.config(menu=menu)


lbl = Label(window, text=" Удивительные цифровые билеты! ")  
lbl.grid(column=0, row=0)


txt = Entry(window,width=10)  
txt.grid(column=2, row=0)

btn = ttk.Button(text="Клик!", command=click_button)
btn.grid(column=5, row=0)


btn = Button(text="Выход", command=window.destroy).grid(column=7, row=0)

window.mainloop()
