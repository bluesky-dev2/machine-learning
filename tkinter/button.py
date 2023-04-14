import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk()
root.title("company")

root.geometry("500x500")

style = ttk.Style()
style.configure('W.TButton', font=(
    'calibri', 10, 'bold', 'underline'), foreground='red')

btn1 = tk.Button(root, bg='black', fg='blue', text='Quit X',
                 bd='5', command=root.destroy)
# ------------------------------
# root - master window, # bg - background, # fg - textcolor
# text - for placeholder, # bd - border, #command - onClick
# ------------------------------
button = tk.Button(root, bg='red', fg='yellow',
                   text='Bell', bd='5', command=root.bell)

button.grid(row=0, column=5, pady=100, padx=250)
btn1.grid(row=1, column=5)


root.mainloop()
