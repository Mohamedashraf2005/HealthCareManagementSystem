from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image 

root = Tk()
root.geometry('1000x750+200+40')
root.title('welcome page')
root.iconbitmap('logo.ico')
root.config(background='#B5B9F1')

#img_logo= Image.open('D:\paython tasks\SWE project\logo.png').resize((100,100))
#img_logo= ImageTk.PhotoImage(img_logo)
#mylabel= Label(root , image=img_logo, )
#mylabel.pack(padx=1,pady=10)

f1= Frame(width=1600,height=70,bg='#B5B9F1')
f1.place(x=1,y=1)

btn1=Button(f1,text='Home',fg='black',bg='#B5B9F1',activeforeground='black',borderwidth=.5)
btn1.place(x=100,y=10)

btn2=Button(f1,text='Doctors',fg='black',bg='#B5B9F1',activeforeground='black',borderwidth=.5)
btn2.place(x=250,y=10)

btn3=Button(f1,text='About us',fg='black',bg='#B5B9F1',activeforeground='black',borderwidth=.5)
btn3.place(x=400,y=10)

btn4=Button(f1,text='Contact us',fg='black',bg='#B5B9F1',activeforeground='black',borderwidth=.5)
btn4.place(x=550,y=10)

btn5=Button(f1,text='Sign up',fg='white',bg='black',activeforeground='black',width=20,height=1,font='10')
btn5.place(x=1000,y=6)

btn6=Button(f1,text='Log in',fg='black',bg='#B5B9F1',activeforeground='black',width=20,height=1,font='10',borderwidth=2)
btn6.place(x=1200,y=6)

f2= Frame(width=1600,height=100,bg='#B5B9F1')
f2.place(x=1,y=100)

lab1=Label(f2,text='Welcome',fg='white',bg='black',font=20,width=25,height=3,borderwidth=3)
lab1.place(x=700,y=20)


f3=Frame(width=800,height=500,bg='#B5B9F1')
f3.place(x=20,y=250)

lab2=Label(f3,text='Healing Elevation',fg='red',bg='#B5B9F1',font=("Arial", 30))
lab2.place(x=20,y=100)
lab3=Label(f3,text='Revitalize Your Health',fg='white',bg='#B5B9F1',font=("Arial", 30))
lab3.place(x=20,y=147)
lab4=Label(f3,text='Book your appointment now',fg='black',bg='white',width=25,height=2,font=15)
lab4.place(x=100,y=230)


f4= Frame(width=600,height=600,bg='#B5B9F1')
f4.place(x=1000,y=240)

img_logo= Image.open('welcome page.png').resize((500,500))
img_logo= ImageTk.PhotoImage(img_logo)
mylabel= Label(f4 , image=img_logo, )
mylabel.pack(padx=1,pady=10)



root.mainloop()