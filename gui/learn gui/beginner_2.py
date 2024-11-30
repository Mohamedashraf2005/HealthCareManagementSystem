import tkinter as tk

# إنشاء نافذة
window = tk.Tk()
window.title("simple interactoin ")
window.geometry("150x200")
# مربع نص
label = tk.Label(window, text="your name:")
label.pack()

entry = tk.Entry(window)
entry.pack()

# وظيفة الزر
def say_hello():
    name = entry.get()
    print(f"hello, {name}!")

# زر
button = tk.Button(window, text="click", command=say_hello)
button.pack()

# تشغيل
window.mainloop()

#? إيه اللي أضفناه؟
#! Label: نص ثابت يظهر للمستخدم.
#! Entry: مربع لإدخال النصوص.
#! say_hello(): وظيفة بتاخد النص المكتوب وتطبعه.