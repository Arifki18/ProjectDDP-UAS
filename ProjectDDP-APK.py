from tkinter import *
# from tkinter import tkk

import ttkbootstrap as ttk

# buat object root dari class tk
root= ttk.Window(themename='superhero')
def convert():
    temp = float(entry.get())
    converted_temp = (temp - 32) * 5/9
    result_label.config(text=f"{converted_temp:.2f} Celsius")

window = Tk()
window.title("Konversi Suhu")

entry = Entry(window, width=25, font=("times new roman", 20))
entry.pack(pady=200)

button = Button(window, text="Konversi", command=convert, font=("ARIAL", 20))
button.pack()

result_label = Label(window, text="klik tombol konversi", font=("times new roman ", 30))
result_label.pack(pady=10)


window.mainloop()