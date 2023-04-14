from tkinter import *
from tkinter.ttk import *

root = Tk()

root.title("Button Style")
root.geometry('500x500')

style = Style()
style.configure('TButton', font=('calibri', 45, 'bold'), borderwidth='5')
# -------------------------
# map() is for dynamically change the appearance of a widget based on its specific state.
# active - when mouse pointer is in a widget specific action occurs
# disabled - to disable a function
# --------------------------
style.map('TButton', foreground=[('active', '!disabled', 'green')],
          background=[('active', 'black')])

btn1 = Button(root, command=root.bell, text='Ring')
btn1.grid(row=0, column=0, padx=80, pady=100)

btn2 = Button(root, command=root.destroy, text='Quit X')
btn2.grid(row=1, column=0)

root.mainloop()
