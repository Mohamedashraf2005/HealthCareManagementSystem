import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk
from welcome_page import WelcomePage
from SignIN import LogIn
from SignUP import SignUp

class MainApplication:
    def __init__(self, root):
        self.root = root
        self.root.geometry('1200x750+150+25')
        self.root.title('DocHub Application')
        self.root.resizable(False, False)
        
        # Create container frame to hold all pages
        self.container = tk.Frame(root)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)
        self.frames = {}
        self.frames[WelcomePage] = WelcomePage(self.container, self)
        self.frames[LogIn] = LogIn(self.container, self)
        self.frames[SignUp] = SignUp(self.container, self)
        
        # Hena 3shan yStart B welcome page
        self.show_frame(WelcomePage)
    
    def show_frame(self, cont):
        """Raise the specified frame to the top"""
        #Hena 3shan nshoof men s9alllll
        print(self.frames.keys())
        frame = self.frames[cont]
        frame.frame.tkraise()

def main():
    root = tk.Tk()
    app = MainApplication(root)
    root.mainloop()

if __name__ == "__main__":
    main()