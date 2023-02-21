import tkinter as tk
from tkinter import filedialog
import cv2
from PIL import Image, ImageTk

class App:
    def __init__(self, window, window_title):
        self.window = window
        self.window.title(window_title)

        self.window.geometry("400x400")

        self.labelinput = tk.Label(self.window, text="Masukkan Gambar")
        self.labelinput.place(x=50, y=10)

        # Create a button to select the image file
        self.button = tk.Button(window, text="Pilih Gambar", command=self.select_image)
        self.button.place(x=180, y=10)

        # Create a label to display the selected image
        self.label = tk.Label(window)
        self.label.place(x=0, y=80, width=300, height=300)

        # Start the event loop
        self.window.mainloop()

    def select_image(self):
        # Open a file dialog to select the image file
        file_path = filedialog.askopenfilename()

        if file_path:
            # Load the image using OpenCV
            cv_image = cv2.imread(file_path)
            
            # Convert the image to RGB format
            cv_image = cv2.cvtColor(cv_image, cv2.COLOR_BGR2RGB)

            # Create a PIL Image from the OpenCV image
            pil_image = Image.fromarray(cv_image)

            # Create a Tkinter PhotoImage from the PIL Image
            tk_image = ImageTk.PhotoImage(pil_image)

            # Update the label with the new image
            self.label.config(image=tk_image)
            self.label.image = tk_image
            self.label.place(x=0, y=80, width=1000, height=1000)

            # Create a button to convert the image to grayscale
            self.buttontogray = tk.Button(self.window, text="Ubah ke Grayscale")
            self.buttontogray.place(x=140, y=50)
            # if clicked, run the convert_to_gray function
            self.buttontogray.config(command=lambda: self.convert_to_gray(file_path))

            # Create a button to convert the image to canny
            self.buttontocanny = tk.Button(self.window, text="Ubah ke Canny")
            self.buttontocanny.place(x=250, y=50)
            # if clicked, run the convert_to_canny function
            self.buttontocanny.config(command=lambda: self.convert_to_canny(file_path))

    def convert_to_gray(self,file_path):
        # convert to grayscale by image loaded
        if(file_path):
            cv_image = cv2.imread(file_path)

            # Create a PIL Image from the OpenCV image
            pil_image = Image.fromarray(cv_image)

            # Create a Tkinter PhotoImage from the PIL Image
            tk_image = ImageTk.PhotoImage(pil_image)

            # Update the label with the new image
            self.label.config(image=tk_image)
            self.label.image = tk_image


    def convert_to_canny(self,file_path):
        if file_path:
            # Load the image using OpenCV
            cv_image = cv2.imread(file_path)
            
            # Convert the image to RGB format
            cv_image = cv2.Canny(cv_image, 100, 200)

            # Create a PIL Image from the OpenCV image
            pil_image = Image.fromarray(cv_image)

            # Create a Tkinter PhotoImage from the PIL Image
            tk_image = ImageTk.PhotoImage(pil_image)

            # Update the label with the new image
            self.label.config(image=tk_image)
            self.label.image = tk_image

# Create a window and pass it to the Application object
App(tk.Tk(), "Image Input Form")