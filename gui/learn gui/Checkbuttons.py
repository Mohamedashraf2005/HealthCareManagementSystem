import tkinter as tk

# إنشاء نافذة
window = tk.Tk()
window.title("Checkbuttons مثال")
window.geometry("500x250")
# متغيرات تخزين القيم
option1 = tk.BooleanVar()
option2 = tk.BooleanVar()

# إضافة مربعات اختيار
check1 = tk.Checkbutton(window, text="one", variable=option1)
check1.pack()

check2 = tk.Checkbutton(window, text="two", variable=option2)
check2.pack()

# زر لتأكيد الخيارات
def show_selections():
    print(f"one: {option1.get()}")
    print(f"two: {option2.get()}")

button = tk.Button(window, text="show slected", command=show_selections)
button.pack()

# تشغيل التطبيق
window.mainloop()

#? إيه اللي بيحصل؟  
#! BooleanVar: متغير بيخزن حالة الاختيار (True أو False).
#! check1 & check2: مربعات اختيار مرتبطة بالمتغيرات.