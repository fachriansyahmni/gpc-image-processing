import tkinter as tk
from tkinter import filedialog
import cv2
from PIL import Image, ImageTk

class App:
    def __init__(self, window, window_title):
        self.window = window
        self.window.title(window_title)

        self.window.geometry("400x400")

        self.window.attributes("-fullscreen", True)

        self.labelinput = tk.Label(self.window, text="Masukkan Gambar")
        self.labelinput.place(x=50, y=10)

        # close button
        self.buttonclose = tk.Button(self.window, text="Keluar", command=self.window.destroy)
        self.buttonclose.place(x=300, y=10)

        # Create a button to select the image file
        self.button = tk.Button(window, text="Pilih Gambar", command=self.select_image)
        self.button.place(x=180, y=10)

        self.labelerror = tk.Label(self.window, text="")
        self.labelerror.place(x=50, y=30)

        # Create a original to display the original image
        self.imageoriginal = tk.Label(window)
        self.imageoriginal.place(x=0, y=90, width=500, height=500)
        self.textimageoriginal = tk.Label(self.window, text="")
        self.textimageoriginal.place(x=100, y=70)    
        
        # Create a label to display the selected image
        self.result = tk.Label(window)
        self.result.place(x=510, y=90, width=500, height=500)
        self.textimageresult = tk.Label(self.window, text="")
        self.textimageresult.place(x=220, y=70)

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

            # Update the result with the new image
            self.imageoriginal.config(image=tk_image)
            self.imageoriginal.image = tk_image
            self.imageoriginal.place(x=0, y=90)
            self.textimageoriginal.text = "Gambar Asli"

            
            # destroy result image
            self.result.config(image="")
            self.result.image = ""

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

            # Convert the image to grayscale
            pil_image = pil_image.convert('L')

            # Create a Tkinter PhotoImage from the PIL Image
            tk_image = ImageTk.PhotoImage(pil_image)

            # Update the result with the new image
            self.result.config(image=tk_image)
            self.result.image = tk_image
            self.textimageresult = tk.Label(self.window, text="Hasil Grayscale")

    def convert_to_canny(self,file_path):
        # insert treshold value
        # open window to insert treshold value
        newWindow = tk.Toplevel(self.window)
        newWindow.title("Treshold Value")
        newWindow.geometry("400x150")

        # input value min
        self.labelmin = tk.Label(newWindow, text="Masukkan Nilai Minimum")
        self.labelmin.place(x=50, y=10)

        self.entrymin = tk.Entry(newWindow)
        self.entrymin.place(x=250, y=10)

        # input value max
        self.labelmax = tk.Label(newWindow, text="Masukkan Nilai Maksimum")
        self.labelmax.place(x=50, y=50)

        self.entrymax = tk.Entry(newWindow)
        self.entrymax.place(x=250, y=50)

        # create button process
        self.buttonprocess = tk.Button(newWindow, text="Proses")
        self.buttonprocess.place(x=180, y=100)
        
        # if clicked, run the process function
        self.buttonprocess.config(command=lambda: self.process(file_path, self.entrymin.get(), self.entrymax.get()))
    
    def process(self, file_path, minV, maxV):
        minValue = int(minV)
        maxValue = int(maxV)

        if maxValue < minValue:
            # show window error message
            self.labelerror.config(text="Nilai Maksimum harus lebih besar dari Nilai Minimum")
        else:
            self.labelerror.config(text="")
            if file_path:
                # Load the image using OpenCV
                cv_image = cv2.imread(file_path)
                
                # Convert the image to RGB format
                cv_image = cv2.Canny(cv_image, minValue, maxValue)

                # Create a PIL Image from the OpenCV image
                pil_image = Image.fromarray(cv_image)

                # Create a Tkinter PhotoImage from the PIL Image
                tk_image = ImageTk.PhotoImage(pil_image)

                # Update the label with the new image
                self.result.config(image=tk_image)
                self.result.image = tk_image
                self.textimageresult = tk.Label(self.window, text="Hasil Canny")

# Create a window and pass it to the Application object
App(tk.Tk(), "Image processing")