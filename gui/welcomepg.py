import customtkinter as ctk
from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.geometry('1200x750+150+25')
root.title('welcome page')
root.resizable(False, False)
root.config(background='#B5B9F1')

#switching Between pages here 
def switch_to_signin():
    root.destroy()  # Close the current window
    import SignIN  
    SignIN.main() 

def switch_to_signup():
    root.destroy()  # Close the current window
    import SignUP  
    SignUP.main() 


def logo_image():
    image = Image.open("PHOTO\logo.png").resize((150, 100)).convert("RGBA")
    datas = image.getdata()
    new_data = []
    for item in datas:
        if item[0] > 200 and item[1] > 200 and item[2] > 200:
            new_data.append((255, 255, 255, 0))
        else:
            new_data.append(item)
    image.putdata(new_data)
    image = ImageTk.PhotoImage(image)
    label = Label(root, text='DOCHUB' ,compound="top", image=image, borderwidth=0,
                  font=("IM FELL Double Pica", 13, "bold"), bg="#B5B9F1",fg='#194C7C')
    label.image = image
    label.place(x=0, y=0)
    return label

logo_img = logo_image()




f1 = Frame(width=1200, height=70, bg='#B5B9F1')  
f1.place(x=150, y=17) 


btn1 = ctk.CTkButton(f1, text='Home', fg_color='#B5B9F1', text_color='black', border_width=2,border_color="black", corner_radius=20, hover_color='#A3A6F1')
btn1.place(x=15, y=20)

btn2 = ctk.CTkButton(f1, text='Doctors', fg_color='#B5B9F1', text_color='black', border_width=2,border_color="black", corner_radius=20, hover_color='#A3A6F1')
btn2.place(x=165, y=20)

btn3 = ctk.CTkButton(f1, text='About us', fg_color='#B5B9F1', text_color='black', border_width=2,border_color="black", corner_radius=20, hover_color='#A3A6F1')
btn3.place(x=315, y=20)

btn4 = ctk.CTkButton(f1, text='Contact us', fg_color='#B5B9F1', text_color='black', border_width=2,border_color="black", corner_radius=20, hover_color='#A3A6F1')
btn4.place(x=465, y=20)

btn5 = ctk.CTkButton(f1, text='Sign up', fg_color='black', text_color='white', border_width=2 ,border_color="black",corner_radius=20, hover_color='#A3A6F1',command=switch_to_signup)
btn5.place(x=700, y=20)

btn6 = ctk.CTkButton(f1, text='Log in', fg_color='#B5B9F1', text_color='black', border_width=2, 
                     border_color="black", corner_radius=20, hover_color='#A3A6F1', command=switch_to_signin)
btn6.place(x=850, y=20)


f2 = Frame(width=1600, height=100, bg='#B5B9F1')  
f2.place(x=1, y=150) 

lab1 = ctk.CTkLabel(f2, text='Welcome', fg_color='black', text_color='white', font=('Helvetica', 33),corner_radius=15)
lab1.place(x=550, y=20)


f3 = Frame(width=800, height=500, bg='#B5B9F1') 
f3.place(x=20, y=250) 

lab2 = Label(f3, text='Healing Elevation', fg='red', bg='#B5B9F1', font=("Arial", 35))  
lab2.place(x=20, y=100) 

lab3 = Label(f3, text='Revitalize Your Health', fg='white', bg='#B5B9F1', font=("Arial", 35))  
lab3.place(x=20, y=155) 

lab4 = Label(f3, text='Book your appointment now !', fg='black', bg='white', width=27, height=2, font=('Arial',15))  
lab4.place(x=100, y=290) 


f4 = Frame(width=400, height=400, bg='#B5B9F1') 
f4.place(x=730, y=250)  

img = Image.open("PHOTO\welcome.png").resize((465,500))
img = ImageTk.PhotoImage(img)
img_label = Label(f4, image=img, bg='#B5B9F1')  
img_label.pack()

root.mainloop()