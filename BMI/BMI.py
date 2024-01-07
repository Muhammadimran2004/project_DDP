import tkinter as tk
from tkinter import ttk
from ttkbootstrap import Style
from PIL import Image, ImageTk

def center_window(root, width, height):
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)

    root.geometry(f"{width}x{height}+{x}+{y}")

def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())
        bmi = weight / ((height / 100) ** 2)  # Konversi tinggi ke meter
        bmi_label.config(text=f"BMI: {bmi:.2f}")
        if bmi < 18.5:
            result_label.config(text="Underweight")
        elif 18.5 <= bmi < 24.9:
            result_label.config(text="Normal weight")
        elif 25 <= bmi < 29.9:
            result_label.config(text="Overweight")
        else:
            result_label.config(text="Obesity")
    except ValueError:
        bmi_label.config(text="Invalid input")

# Create main window
root = tk.Tk()
root.title("BMI Calculator")
root.geometry("400x300")
center_window(root, 400, 300)

# Create style using ttkbootstrap
style = Style(theme="vapor")

# Load background image
bg_image = Image.open("D:\\DDP\\BMI\\image\\BMI 2.jpg")
bg_image = bg_image.resize((1550, 800))  # Sesuaikan dengan ukuran jendela Anda
bg_image = ImageTk.PhotoImage(bg_image)

# Create a label for the background image
background_label = tk.Label(root, image=bg_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Create widgets
frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

weight_label = ttk.Label(frame, text="Berat badan (kg):")
weight_label.grid(row=0, column=0, pady=5, sticky=tk.W)

weight_entry = ttk.Entry(frame)
weight_entry.grid(row=0, column=1, pady=5, padx=5, sticky=tk.W)

height_label = ttk.Label(frame, text="Tinggi badan (cm):")
height_label.grid(row=1, column=0, pady=5, sticky=tk.W)

height_entry = ttk.Entry(frame)
height_entry.grid(row=1, column=1, pady=5, padx=5, sticky=tk.W)

calculate_button = ttk.Button(frame, text="Hitung BMI", command=calculate_bmi, style="warning")
calculate_button.grid(row=2, column=0, columnspan=2, pady=10)

bmi_label = ttk.Label(frame, text="BMI: ")
bmi_label.grid(row=3, column=0, columnspan=2, pady=5)

result_label = ttk.Label(frame, text="")
result_label.grid(row=4, column=0, columnspan=2, pady=5)

# Run the main loop
root.mainloop()
