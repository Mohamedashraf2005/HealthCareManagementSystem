import customtkinter as ctk
from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.geometry('1200x750')
root.title('welcome page')
root.resizable(False, False)

root.config(background='#B5B9F1')


f1 = Frame(width=1200, height=70, bg='#B5B9F1')  
f1.place(x=1, y=0) 


btn1 = ctk.CTkButton(f1, text='Home', fg_color='#B5B9F1', text_color='black', border_width=2,border_color="black", corner_radius=20, hover_color='#A3A6F1')
btn1.place(x=15, y=20)

btn2 = ctk.CTkButton(f1, text='Doctors', fg_color='#B5B9F1', text_color='black', border_width=2,border_color="black", corner_radius=20, hover_color='#A3A6F1')
btn2.place(x=165, y=20)

btn3 = ctk.CTkButton(f1, text='About us', fg_color='#B5B9F1', text_color='black', border_width=2,border_color="black", corner_radius=20, hover_color='#A3A6F1')
btn3.place(x=315, y=20)

btn4 = ctk.CTkButton(f1, text='Contact us', fg_color='#B5B9F1', text_color='black', border_width=2,border_color="black", corner_radius=20, hover_color='#A3A6F1')
btn4.place(x=465, y=20)

btn5 = ctk.CTkButton(f1, text='Sign up', fg_color='#B5B9F1', text_color='black', border_width=2 ,border_color="black",corner_radius=20, hover_color='#A3A6F1')
btn5.place(x=900, y=20)

btn6 = ctk.CTkButton(f1, text='Log in', fg_color='#B5B9F1', text_color='black', border_width=2, border_color="black",corner_radius=20, hover_color='#A3A6F1')
btn6.place(x=1050, y=20)


f2 = Frame(width=1600, height=100, bg='#B5B9F1')  
f2.place(x=1, y=100) 

lab1 = ctk.CTkLabel(f2, text='Welcome', fg_color='#B5B9F1', text_color='black', font=('Helvetica', 33))
lab1.place(x=550, y=20)


f3 = Frame(width=800, height=500, bg='#B5B9F1') 
f3.place(x=20, y=250) 

lab2 = Label(f3, text='Healing Elevation', fg='red', bg='#B5B9F1', font=("Arial", 30))  
lab2.place(x=20, y=100) 

lab3 = Label(f3, text='Revitalize Your Health', fg='white', bg='#B5B9F1', font=("Arial", 30))  
lab3.place(x=20, y=147) 

lab4 = Label(f3, text='Book your appointment now', fg='black', bg='#B5B9F1', width=25, height=2, font=22)  
lab4.place(x=12, y=230) 

f4 = Frame(width=400, height=400, bg='#B5B9F1') 
f4.place(x=790, y=300)  


img = Image.open("welcome page.png").resize((400, 400))  
img = ImageTk.PhotoImage(img)


img_label = Label(f4, image=img, bg='#B5B9F1')  
img_label.pack()

root.mainloop()
