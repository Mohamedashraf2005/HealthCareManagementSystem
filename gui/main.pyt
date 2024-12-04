import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

def login():
    username = username_entry.get()
    password = password_entry.get()
    # هنا ممكن تضيف لوجيك تسجيل الدخول
    messagebox.showinfo("Login", f"Username: {username}\nPassword: {password}")

def back_action():
    messagebox.showinfo("Back", "Going back!")

# إنشاء النافذة الرئيسية
root = tk.Tk()
root.title("Banana Clinic")
root.geometry("900x600")
root.configure(bg="#EAEAFD")

# تقسيم النافذة إلى قسمين
left_frame = tk.Frame(root, width=450, height=600, bg="#F4D0D0")
left_frame.grid(row=0, column=0)

right_frame = tk.Frame(root, width=450, height=600, bg="#D1C8F0")
right_frame.grid(row=0, column=1)

# شعار العيادة
logo = tk.Label(left_frame, text="BANANA CLINIC", font=("Arial", 16, "bold"), bg="#F4D0D0", fg="#DF1515")
logo.grid(row=0, column=0, pady=20)

# اختيار نوع الدخول
select_label = tk.Label(left_frame, text="Select\nThe Type of\nLog In:", font=("Arial", 18, "bold"), bg="#F4D0D0", fg="black", justify="left")
select_label.grid(row=1, column=0, padx=20)

# صور الأنواع
def create_button(frame, image_path, text):
    img = Image.open(image_path).resize((100, 100))
    img = ImageTk.PhotoImage(img)
    button = tk.Button(frame, text=text, compound="top", image=img, bg="#F4D0D0", borderwidth=0)
    button.image = img  # لتجنب حذف الصورة من الذاكرة
    button.pack(side=tk.LEFT, padx=15)
    return button

buttons_frame = tk.Frame(left_frame, bg="#F4D0D0")
buttons_frame.grid(row=2, column=0)

# أزرار الأنواع
create_button(buttons_frame, "patain.jpg", "Patient")
create_button(buttons_frame, "doctorimage.jpg", "Doctor")
create_button(buttons_frame, "admin.jpg", "Admin")

# شاشة تسجيل الدخول
back_button = tk.Label(right_frame, text="< back", font=("Arial", 12, "underline"), bg="#D1C8F0", fg="blue", cursor="hand2")
back_button.grid(row=0, column=0, sticky="w", padx=10, pady=10)
back_button.bind("<Button-1>", lambda e: back_action())

username_label = tk.Label(right_frame, text="Username", font=("Arial", 14), bg="#D1C8F0")
username_label.grid(row=1, column=0, padx=50, pady=10)

username_entry = tk.Entry(right_frame, font=("Arial", 14), width=25)
username_entry.grid(row=2, column=0, padx=50, pady=10)

password_label = tk.Label(right_frame, text="Password", font=("Arial", 14), bg="#D1C8F0")
password_label.grid(row=3, column=0, padx=50, pady=10)

password_entry = tk.Entry(right_frame, font=("Arial", 14), width=25, show="*")
password_entry.grid(row=4, column=0, padx=50, pady=10)

login_button = tk.Button(right_frame, text="Log In", font=("Arial", 14), command=login)
login_button.grid(row=5, column=0, pady=20)

signup_label = tk.Label(right_frame, text="Sign up?", font=("Arial", 12), bg="#D1C8F0", fg="blue", cursor="hand2")
signup_label.grid(row=6, column=0, pady=10)

root.mainloop()
