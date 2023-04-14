# a tkinter python program to understand grid
from tkinter import *
from tkinter.ttk import *

root = Tk()
root.geometry('500x300')
root.title('Grid')

"""
Widget      Style Configure Name
------      ------
Button	    TButton
Checkbutton	TCheckbutton
Combobox	TCombobox
Entry	    TEntry
Frame	    TFrame
Label	    TLabel
LabelFrame	TLabelFrame
Menubutton	TMenubutton
Notebook	TNotebook
PanedWindow	TPanedwindow 
Progressbar	Horizontal.TProgressbar / Vertical.TProgressbar
Radiobutton	TRadiobutton
Scale	    Horizontal.TScale / Vertical.TScale
Scrollbar	Horizontal.TScrollbar / Vertical.TScrollbar
Separator	TSeparator
Sizegrip	TSizegrip
Treeview	Treeview 
"""

style = Style()
style.configure('TCheckbutton', font=('TimesNewRoman', 10, 'bold'))
style.configure('TButton', font=('TimesNewRoman', 10, 'bold'))

l1 = Label(root, text='Height', font=('TimesNewRoman', 10, 'bold'))
l2 = Label(root, text='weight', font=('TimesNewRoman', 10, 'bold'))

l1.grid(row=0, column=0, sticky=E, pady=2, padx=5)
l2.grid(row=1, column=0, sticky=W, pady=2, padx=5)

e1 = Entry(root)
e2 = Entry(root)

e1.grid(row=0, column=1, pady=2, padx=5)
e2.grid(row=1, column=1, pady=2, padx=5)

c1 = Checkbutton(root, text="Preserve")
c1.grid(row=2, column=0, sticky=W, columnspan=2, pady=10, padx=10)

# img = PhotoImage(
#     file=r"E:\Pheonix\programing\Visual_studio_codes\Pythonpg\CV\tkinter\spidey.png")
# img1 = img.subsample(2, 2)
# root.create_image(0, 0, anchor=NW, image=img1)
img = PhotoImage(
    file=r"E:\Pheonix\programing\Visual_studio_codes\Pythonpg\CV\tkinter\spidey.png")
img1 = img.subsample(2, 2)

# setting image with the help of label
Label(root, image=img1).grid(row=0, column=2,
                             columnspan=2, rowspan=2, padx=50, pady=5)

b1 = Button(root, text='Zoom In')
b2 = Button(root, text='Zoom Out')

b1.grid(row=3, column=2, padx=10)
b2.grid(row=3, column=3)

root.mainloop()
