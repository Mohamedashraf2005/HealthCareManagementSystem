from tkinter import *
from PIL import ImageTk, Image
import os
from welcome_page import WelcomePage

def get_resource_path(*path_parts):
    """Get the absolute path for resource files."""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, *path_parts)

class SplashScreen:
    def __init__(self, container, app, width=1200, height=750):
        # Store container and app references
        self.container = container
        self.app = app
        self.animation_index = 0  # Track animation step
        self.total_duration = 450  # Total splash screen duration in milliseconds
        self.frame_interval = self.total_duration // 20  # Number of animation frames

        # Names for the animation sequence
        self.names = [
            "Anas Elgezawy", "Ali Elbahrawy",
            "Eman Hekal", "Mariam Ahmed",
            "Mohamed Ahmed", "Mohamed Ashraf"
        ]
        self.header_texts = ["Welcome to DocHub", "Your Health, Simplified", "Management Made Easy"]
        self.bio_text = ("")
        #"DocHub: A streamlined health clinic management system, empowering  your workflow with ease and efficiency."

        # Configure main frame
        self.frame = Frame(container, width=width, height=height, bg='#b5b9f1')
        self.frame.grid(row=0, column=0, sticky="nsew")

        # Load images for the animation and splash icon
        self.image_a = ImageTk.PhotoImage(Image.open(get_resource_path("PHOTO", "c1.png")))
        self.image_b = ImageTk.PhotoImage(Image.open(get_resource_path("PHOTO", "c2.png")))
        self.splashicon = ImageTk.PhotoImage(Image.open(get_resource_path("PHOTO", "splashicon.png")))  # Assuming the image is in the "PHOTO" folder

        # Create widgets
        self.create_widgets()

        # Start the animation
        self.animate_splash()

    def create_widgets(self):
        """Create the static and dynamic widgets for the splash screen."""
        # Splash icon above the header
        self.icon_frame = Frame(self.frame, bg='#b5b9f1')  # Create a frame for the icon
        self.icon_frame.place(x=600, y=200, anchor="center")  # Position it above the header
        self.icon_label = Label(self.icon_frame, image=self.splashicon, bg='#b5b9f1')
        self.icon_label.pack()

        # Header label
        self.header_label = Label(self.frame, text="", fg='#3269ab', bg='#b5b9f1', font=("Arial", 24, "bold"))
        self.header_label.place(x=600, y=275, anchor="center")

        # Bio label
        self.bio_label = Label(self.frame, text=self.bio_text, wraplength=800, fg='#000000', bg='#b5b9f1',
                               font=("Arial", 14))
        self.bio_label.place(x=600, y=250, anchor="center")

        # Name label
        self.name_label = Label(self.frame, text="", fg="#ee3e54", bg="#b5b9f1", font=("Arial", 20, "bold"))
        self.name_label.place(x=600, y=350, anchor="center")

        # Image labels (for animation)
        self.image_label_a = Label(self.frame, image=self.image_a, bg="#b5b9f1")
        self.image_label_a.place(x=580, y=400, anchor="center")
        self.image_label_b = Label(self.frame, image=self.image_b, bg="#b5b9f1")
        self.image_label_b.place(x=600, y=400, anchor="center")

    def update_labels(self, img_a, img_b):
        """Update the images on the splash screen."""
        self.image_label_a.configure(image=img_a)
        self.image_label_b.configure(image=img_b)

    def animate_splash(self):
        """Run the splash screen animation."""
        animation_sequence = [
            (self.image_a, self.image_b),
            (self.image_b, self.image_a),
            (self.image_a, self.image_b),
            (self.image_b, self.image_a),
        ]
        
        # Calculate the time passed and update animation based on the sequence
        if self.animation_index < len(self.names) * len(animation_sequence):  # Repeat for all names
            current_name_index = self.animation_index // len(animation_sequence)
            current_frame_index = self.animation_index % len(animation_sequence)

            # Update images
            frame_images = animation_sequence[current_frame_index]
            self.update_labels(*frame_images)  # Pass only two images

            # Update name
            self.name_label.configure(text=self.names[current_name_index])

            # Update header text based on time
            current_time = self.animation_index * self.frame_interval
            if current_time < self.total_duration // 3:
                self.header_label.configure(text=self.header_texts[0])
            elif current_time < 2 * self.total_duration // 3:
                self.header_label.configure(text=self.header_texts[1])
            else:
                self.header_label.configure(text=self.header_texts[2])

            # Update animation index
            self.animation_index += 1
            self.container.after(130, self.animate_splash)  # Schedule next frame (0.2-second delay)
        else:
            self.finish_splash()

    def finish_splash(self):
        """Handle finishing the splash screen."""
        self.frame.destroy()  # Remove the splash screen frame
        self.app.show_frame(WelcomePage)  # Call the show_frame method to navigate

class App(Tk):
    def __init__(self):
        super().__init__()
        self.title("Application")
        self.geometry("1200x750")

        # Container to hold frames
        self.container = Frame(self)
        self.container.pack(side="top", fill="both", expand=True)

        self.frames = {}

        # Initialize WelcomePage
        for F in (WelcomePage,):
            frame = F(parent=self.container, controller=self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # Show splash screen
        SplashScreen(container=self, app=self, width=1200, height=750)

    def show_frame(self, page_class):
        """Display the specified frame."""
        frame = self.frames[page_class]
        frame.tkraise()


# Test block for standalone execution
if __name__ == "__main__":
    app = App()
    app.mainloop()
