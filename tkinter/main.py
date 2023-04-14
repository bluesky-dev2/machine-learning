import tkinter as tk
from time import strftime

root = tk.Tk()
root.geometry("1024x1024")

#bg_image = tk.PhotoImage(file="bg2.png")
#bg_label = tk.Label(root, image=bg_image)
#bg_label.place(x=0, y=0, relwidth=1, relheight=1)

caption_image = tk.PhotoImage(file="title.png").subsample(2)
caption_label = tk.Label(root, image=caption_image)
caption_label.place(relx=0.5, rely=0.1, anchor='center')



def button_click(button_name):
    print(button_name)

# load and resize images
imag_x = tk.PhotoImage(file="key.png").subsample(4)
imag_y = tk.PhotoImage(file="vol.png").subsample(4)
imag_z = tk.PhotoImage(file="bri.png").subsample(4)

# create labels with images
imag_x_label = tk.Label(root, image=imag_x, bd=0, highlightthickness=0, cursor="hand2")
imag_x_label.place(relx=0.5, rely=0.5, anchor='center')
imag_x_label.bind("<Button-1>", lambda event: button_click("Virtual Keyboard"))

imag_y_label = tk.Label(root, image=imag_y , bd=0, highlightthickness=0, cursor="hand2")
imag_y_label.place(relx=0.2, rely=0.7, anchor='center')
imag_y_label.bind("<Button-1>", lambda event: button_click("Volume"))

imag_z_label = tk.Label(root, image=imag_z , bd=0, highlightthickness=0, cursor="hand2")
imag_z_label.place(relx=0.8, rely=0.7, anchor='center')
imag_z_label.bind("<Button-1>", lambda event: button_click("Brightness"))

def time():
	string = strftime('%H:%M:%S %p')
	lbl.config(text=string)
	lbl.after(1000, time)


lbl = tk.Label(root, font=('Helvetica', 40, 'bold'),
			foreground='#17d4fe')

# root.wm_attributes('-transparentcolor','black')

lbl.place(relx=0.8, rely=0.895, anchor='center')
time()

root.mainloop()
