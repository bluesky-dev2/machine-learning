from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

root = Tk()
root.title("Facebook")
root.geometry("800x600")
root.configure(bg="#f0f2f5")

# Profile information
fb_name = ""
fb_picture = ImageTk.PhotoImage(Image.open("facebook.png"))

# Set Segoe UI as the default font
default_font = ("Segoe UI", 10)
root.option_add("*Font", default_font)

# Profile information
profile_name = "Batman"
profile_picture = ImageTk.PhotoImage(Image.open("a.jpg").resize((50, 50)).convert("RGB"))

# Post information
post_dates = ["12 Feb 2020", "3 June 2020", "1 April 2022"]
post_images = ["a.jpg", "b.jpg", "c.jpeg"]
post_captions = ["eat", "hbd", "messi"]

# Create a frame for the profile information
profile_frame = Frame(root, bg="#3b5998", height=80)
profile_frame.pack(side=TOP, fill=X)

# Create a label for the profile picture
fb_label = Label(profile_frame, image=fb_picture, bg="#3b5998", bd=0)
fb_label.place(relx=0.5, rely=0.5, anchor=CENTER)

# Create a frame for the profile name
profile_name_frame = Frame(profile_frame, bg="#3b5998")
profile_name_frame.pack(side=LEFT, padx=20, pady=10)

# Create a label for the profile name
profile_name_label = Label(profile_name_frame, text=profile_name, font=("Segoe UI", 16), fg="white", bg="#3b5998")
profile_name_label.pack(side=TOP)

# Create a label for the posts section
posts_label = Label(root, text="Posts", font=("Segoe UI", 16), padx=20, pady=10)
posts_label.pack(side=TOP)

# Create a frame for the posts
posts_frame = Frame(root, bg="#f0f2f5")
posts_frame.pack(side=TOP, fill=BOTH, expand=1)

# Create a canvas for the posts
posts_canvas = Canvas(posts_frame, bg="#f0f2f5", highlightthickness=0)
posts_canvas.pack(side=LEFT, fill=BOTH, expand=1)

# Add a scrollbar to the canvas
posts_scrollbar = ttk.Scrollbar(posts_frame, orient=VERTICAL, command=posts_canvas.yview)
posts_scrollbar.pack(side=RIGHT, fill=Y)
posts_canvas.configure(yscrollcommand=posts_scrollbar.set)

# Create a frame for the posts inside the canvas
posts_frame_canvas = Frame(posts_canvas, bg="#f0f2f5")
posts_canvas.create_window((0, 0), window=posts_frame_canvas, anchor=NW)


for i in range(3):
    # Create a frame for the post
    post_frame = Frame(posts_frame_canvas, padx=20, pady=10, bg="white", highlightbackground="#ddd", highlightthickness=1)
    post_frame.pack(side=TOP, fill=X)

    # Create a sub-frame for the post image
    post_image_frame = Frame(post_frame, bg="white")
    post_image_frame.pack(side=LEFT)

    # Read the post image file
    post_image = ImageTk.PhotoImage(Image.open(post_images[i]).convert("RGB"))

    # Create a label for the post image
    post_image_label = Label(post_image_frame, image=post_image, bg="white")
    post_image_label.image = post_image
    post_image_label.pack(side=TOP)

    # Create a label for the profile picture
    profile_picture_label = Label(post_image_frame, image=profile_picture, bg="white")
    profile_picture_label.pack(side=LEFT, padx=10)

    # Create a sub-frame for the post caption and buttons
    post_caption_frame = Frame(post_frame, bg="white")
    post_caption_frame.pack(side=LEFT, fill=BOTH, expand=1)

    # Create a label for the post caption
    post_caption_label = Label(post_caption_frame, text=post_captions[i], font=("Segoe UI", 12), fg="#333", bg="white",
                               wraplength=600)
    post_caption_label.pack(side=TOP, anchor=W, padx=10, pady=10)

    # Create a frame for the like and comment buttons
    post_buttons_frame = Frame(post_caption_frame, bg="white")
    post_buttons_frame.pack(side=BOTTOM, fill=X, padx=10)

    # Create a like button
    like_button = Button(post_buttons_frame, text="Like", font=("Segoe UI", 10), fg="#808080", bg="white", bd=0)
    like_button.pack(side=LEFT)

    # Create a comment button
    comment_button = Button(post_buttons_frame, text="Comment", font=("Segoe UI", 10), fg="#808080", bg="white", bd=0)
    comment_button.pack(side=LEFT, padx=10)

# Update the canvas to show the posts
posts_frame_canvas.update_idletasks()
posts_canvas.configure(scrollregion=posts_canvas.bbox("all"))

root.mainloop()
