import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk  # استيراد المكتبة

# إنشاء نافذة التطبيق
root = tk.Tk()
root.title("Health Portal")
root.geometry("900x700")  # تحديد حجم النافذة
root.configure(bg="#d9d9d9")  # لون الخلفية
root.resizable(False, False)

# 1. شريط التنقل في الأعلى
menu_frame = tk.Frame(root, bg="#d9d9d9", height=50)
menu_frame.pack(side="top", fill="x", pady=20, padx=200)

menu_items = ["Home", "Doctors", "About Us", "Contact Us"]
active_button = tk.StringVar(value="Home")  # اسم الزر النشط (افتراضيًا "Home")

# دالة لتغيير حالة الزر النشط
def activate_button(button_name):
    active_button.set(button_name)  # تحديث اسم الزر النشط
    for widget in menu_frame.winfo_children():  # استعراض جميع الأزرار في القائمة
        if widget.cget("text") == button_name:
            widget.config(bg="#dadf4a", fg="#000000")  # الزر النشط (لون مختلف)
        else:
            widget.config(bg="#d9d9d9", fg="#000000")  # الأزرار الأخرى

# إنشاء الأزرار
for item in menu_items:
    btn = tk.Button(
        menu_frame,
        text=item,
        font=("Helvetica", 12, "bold"),
        bg="#d9d9d9",
        fg="#000000",
        borderwidth=0,
        command=lambda name=item: activate_button(name),  # تغيير الحالة عند الضغط
    )
    btn.pack(side="left", padx=20)

# 2. إضافة الصورة من المسار إلى الجهة اليسرى
image_path = "D:\Life\Media\in\MAIN.png"  # مسار الصورة
image = Image.open(image_path)  # فتح الصورة باستخدام Pillow
image = image.resize((600, 500))  # تعديل حجم الصورة (لو لزم الأمر)
image_tk = ImageTk.PhotoImage(image)  # تحويل الصورة لتنسيق Tkinter

# إضافة الصورة إلى واجهة المستخدم
image_label = tk.Label(root, image=image_tk, bg="#d9d9d9")
image_label.place(x=0, y=200)  # تحديد مكان الصورة
# image_label.place(x=0, y=270)  # تحديد مكان الصورة

# 3. النص الترحيبي
welcome_label = tk.Label(root, text="Welcome\nBooking Your Health\n Journey Starts With \na One Click!", font=("Helvetica", 22, "bold"), bg="#d9d9d9", fg="#000000", justify="center")
welcome_label.place(y=320, x=575)

# 4. زر "START"
start_button = ttk.Button(root, text="START", command=lambda: print("Start Button Clicked!"),width=20)
start_button.place(y=470, x=660)

# تفعيل الزر الافتراضي عند التشغيل
activate_button("Home")

# تشغيل التطبيق
root.mainloop()
