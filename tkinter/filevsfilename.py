from tkinter import *
from tkinter.filedialog import askopenfile,askopenfilename

root = Tk()
root.geometry('300x300')
root.title('testing')

def open_file():
    file1 = askopenfile(mode='r')
    print(file1)
def open_filename():
    file = askopenfilename()
    print(file)

btn = Button(root, text='hit it', command=lambda:open_file())
btn.grid(row=0,column=0)
btn1 = Button(root, text='hit it', command=lambda:open_filename())
btn1.grid(row=1,column=0)
root.mainloop()