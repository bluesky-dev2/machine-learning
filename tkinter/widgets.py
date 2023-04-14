from tkinter import *
from tkinter.ttk import *

root = Tk()
root.title('Widgets')
root.geometry('500x500')

style = Style()
style.configure('TButton', font=('TimesNewRoman', 10, 'bold'))
style.configure('Horizontal.TScale', foreground=[('active', 'green')])

button = Button(root, text='Hit me', command=root.bell)
button.grid(row=0, column=0, padx=200, pady=5)

label = Label(root, text='Hit the Label')
label.grid(row=1, column=0, pady=20)

checkbox = Combobox(root, values=["Option1", "Option2", "Option3 "])
checkbox.grid(row=2, column=0,  pady=20)
checkbox.set("Select")

radiobutton1 = Radiobutton(root, text='Option1', command=root.bell)
radiobutton2 = Radiobutton(root, text='Option2')
radiobutton3 = Radiobutton(root, text='Option3')
radiobutton1.grid(row=3, column=0, pady=2)
radiobutton2.grid(row=4, column=0, pady=2)
radiobutton3.grid(row=5, column=0, pady=2)

checkbutton = Checkbutton(root, text="Option1")
checkbutton2 = Checkbutton(root, text="Option2")
checkbutton.grid(row=6, column=0, pady=2)
checkbutton2.grid(row=7, column=0, pady=2)

scale = Scale(root, from_=0, to=10)
scale.grid(row=8, column=0, pady=20)

e1 = Entry(root)
e1.grid(pady=5)
e1 = Entry(root)
e1.grid(pady=2)

root.mainloop()
