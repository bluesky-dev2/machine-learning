from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image , ImageDraw
import numpy as np

root = Tk()
root.title("Facebook")
root.geometry("800x600")
root.configure(bg="#f0f2f5")

# Set Segoe UI as the default font
default_font = ("Segoe UI", 10)
root.option_add("*Font", default_font)

# Profile information
profile_name = "Batman"
profile_picture = ImageTk.PhotoImage(file=r"facebook.png")

# Post information
post_dates = ["12 Feb 2022", "1 March 2022", "19 December 2022"]
post_images = ["a.jpg", "b.jpg", "c.jpeg"]
post_captions = ["Who doesn't like having burgers..", "Happy Birthday , My Rival.. ", "Congratulations messi , My Amigo.. "]
button_images = ["like button.png", "comment button.png", "profileimage.png"]

# Create a frame for the profile information
# Create the blue top bar for facebook interface 
profile_frame = Frame(root, bg="#3b5998", height=80)
profile_frame.pack(side=TOP, fill=X)

# Create a label for the profile picture 
# Create the facebook logo at the top bar
profile_picture_label = Label(profile_frame, image=profile_picture, bg="#3b5998")
profile_picture_label.pack(side=LEFT, padx=20, pady=10)


# Create a label for the heading "posts" section
# Create a bar showing the text posts under the blue bar
posts_label = Label(root, text="Posts", font=("bold", 25), padx=10, pady=10)
posts_label.pack(side=TOP)

# Create a frame for the posts
posts_frame = Frame(root, bg="#f0f2f5")
posts_frame.pack(side=TOP, fill=BOTH, expand=1)

# Create a canvas for the posts
posts_canvas = Canvas(posts_frame, bg="#f0f2f5", width=800, highlightthickness=0)
posts_canvas.pack(side=LEFT, fill=BOTH, expand=1)

# Add a scrollbar to the canvas
posts_scrollbar = ttk.Scrollbar(posts_frame, orient=VERTICAL, command=posts_canvas.yview)
posts_scrollbar.pack(side=RIGHT, fill=Y)
posts_canvas.configure(yscrollcommand=posts_scrollbar.set)
#posts_canvas.bind('<Configure>', lambda e: posts_canvas.configure(scrollregion=posts_canvas.bbox("all")))

# Create a frame for the posts inside the canvas
posts_frame_canvas = Frame(posts_canvas, bg="#f0f2f5")
posts_canvas.create_window((0, 0), window=posts_frame_canvas, anchor=NW)


img1 = Image.open("profileimage.png")
bigsize = (img1.size[0] * 3, img1.size[1] * 3)
mask = Image.new('L', bigsize, 0)
draw = ImageDraw.Draw(mask) 
draw.ellipse((0, 0) + bigsize, fill=255)
mask = mask.resize(img1.size, Image.ANTIALIAS)
img1.putalpha(mask)
img1.resize((100,100))
user_profile = ImageTk.PhotoImage(img1)

img2 = Image.open("like button.png")
bigsize = (img2.size[0] * 3, img2.size[1] * 3)
mask = Image.new('L', bigsize, 0)
draw = ImageDraw.Draw(mask) 
draw.ellipse((0, 0) + bigsize, fill=255)
mask = mask.resize(img2.size, Image.ANTIALIAS)
img2.putalpha(mask)
img2.resize((100,100))
like_button_image = ImageTk.PhotoImage(img2)

img3 = Image.open("comment button.png")
bigsize = (img3.size[0] * 3, img3.size[1] * 3)
mask = Image.new('L', bigsize, 0)
draw = ImageDraw.Draw(mask) 
draw.ellipse((0, 0) + bigsize, fill=255)
mask = mask.resize(img3.size, Image.ANTIALIAS)
img3.putalpha(mask)
img3.resize((100,100))
comment_button_image = ImageTk.PhotoImage(img3)

img4 = Image.open("like fill.png")
bigsize = (img4.size[0] * 3, img4.size[1] * 3)
mask = Image.new('L', bigsize, 0)
draw = ImageDraw.Draw(mask) 
draw.ellipse((0, 0) + bigsize, fill=255)
mask = mask.resize(img4.size, Image.ANTIALIAS)
img4.putalpha(mask)
img4.resize((100,100))
like_fill_button = ImageTk.PhotoImage(img4)

bell_button = ImageTk.PhotoImage(Image.open("Notification_Bell_icon.png"))

img6 = Image.open("joker.png")
bigsize = (img6.size[0] * 3, img6.size[1] * 3)
mask = Image.new('L', bigsize, 0)
draw = ImageDraw.Draw(mask) 
draw.ellipse((0, 0) + bigsize, fill=255)
mask = mask.resize(img6.size, Image.ANTIALIAS)
img6.putalpha(mask)
img6.resize((100,100))
joker_image = ImageTk.PhotoImage(img6)

img7 = Image.open("Messenger_icon_image.jpg")
bigsize = (img7.size[0] * 3, img7.size[1] * 3)
mask = Image.new('L', bigsize, 0)
draw = ImageDraw.Draw(mask) 
draw.ellipse((0, 0) + bigsize, fill=255)
mask = mask.resize(img7.size, Image.ANTIALIAS)
img7.putalpha(mask)
img7.resize((100,100))
messenger_image = ImageTk.PhotoImage(img7)

joker_photo_label = Label(profile_frame, image=joker_image, bg="#3b5998")
joker_photo_label.pack(side=RIGHT, padx=5, pady=5)

bell_photo_label = Label(profile_frame, image=bell_button, bg="#3b5998")
bell_photo_label.pack(side=RIGHT, padx=5, pady=5)

messenger_photo_label = Label(profile_frame, image=messenger_image, bg="#3b5998")
messenger_photo_label.pack(side=RIGHT, padx=5, pady=5)

search_bar_image = ImageTk.PhotoImage(Image.open("search_bar.png"))
search_bar_label = Label(profile_frame, image=search_bar_image, bg="#3b5998")
search_bar_label.pack(padx=5,pady=35)

# Define a function to check if a string is palindrome or not
def is_palindrome(s):
    return s == s[::-1]

comments = []
new_comment_entry = None
comments_text = None

def open_comment_window():
    # create a new window for the comment section
    comment_window = Toplevel(posts_frame_canvas)
    comment_window.title("Comments")

    # create a text widget to display the comments
    comments_text = Text(comment_window, width=200, height=25)
    comments_text.pack()

    # display all the comments in the text widget
    for comment in comments:
        comments_text.insert(END, comment + "\n")

    # create an entry widget for new comments
    new_comment_entry = Entry(comment_window, width=180)
    new_comment_entry.pack()

    # create a button to submit comments
    submit_button = Button(comment_window, text="COMMENT", command=lambda: submit_comment(comment_window, comments_text, new_comment_entry))
    submit_button.pack()

def submit_comment(comment_window, comments_text, new_comment_entry):
    # get the text entered in the entry widget
    new_comment = new_comment_entry.get()

    # check if the new comment is not empty
    if new_comment.strip():
        # check if the new comment is a palindrome
        is_palindrome_flag = is_palindrome(new_comment)

        # display a message if the new comment is a palindrome
        if is_palindrome_flag:
            messagebox.showerror("Error", "The entered comment is a palindrome!")

        else:
            # append the new comment to the list of comments
            comments.append(new_comment)

            # clear the entry widget
            new_comment_entry.delete(0, END)

            # update the comments text widget with the new comment
            comments_text.insert(END, new_comment + "\n")

    else:
        # display an error message if the new comment is empty
        messagebox.showerror("Error", "Please enter a comment.")

    # close the comment window
    comment_window.destroy()

# Define a function to change Image
def change_img():
    new_image = like_fill_button
    like_image_label.configure(image=new_image)
    like_image_label.image = new_image

def change_img(like_image_label, like_button_image):
    new_image = like_fill_button
    like_image_label.configure(image=new_image)
    like_image_label.image = new_image

# Add the posts to the frame
for i in range(3):

    # Create a frame for the user photo and user name and date
    #profile_frame = Frame(posts_frame_canvas, padx=20, pady=10, bg="white", highlightbackground="#ddd", highlightthickness=1)
    profile_frame = Frame(posts_frame_canvas, bg="white", height=20)
    profile_frame.pack(side=TOP,fill=X)

    user_photo_label = Label(profile_frame, image=user_profile, bg="white")
    user_photo_label.pack(side=LEFT, padx=5, pady=5)

    user_name_date_frame = Frame(profile_frame, bg="white")
    user_name_date_frame.pack(side=LEFT, padx=20, pady=10)

    user_name_label = Label(user_name_date_frame, text=profile_name, font=("bold", 30), fg="black", bg="white")
    user_name_label.pack(side=TOP)

    date_label = Label(user_name_date_frame, text=post_dates[i], font=("Segoe UI", 20), fg="grey", bg="white")
    date_label.pack(side=TOP)

     # Create a frame for the like and comment buttons
    post_caption_frame = Frame(posts_frame_canvas, bg="white", height=100)
    post_caption_frame.pack(side=TOP, fill=X)

    # Create a like button
    post_caption_label = Label(post_caption_frame, text=post_captions[i], font=("Segoe UI", 25), fg="black", bg="white", bd=0, padx=5)
    post_caption_label.pack(side=LEFT)

    # Create a frame for the post image
    post_image_frame = Frame(posts_frame_canvas, bg="white")
    post_image_frame.pack(side=TOP, fill=X)

    image = Image.open(post_images[i]).convert("RGB")
    resized_image = image.resize((1928,1080))

    post_image = ImageTk.PhotoImage(resized_image)

    # Create a label for the post image
    post_image_label = Label(post_image_frame, image=post_image, bg="white")
    post_image_label.image = post_image
    post_image_label.pack(side=LEFT)

    # Create a frame for the like and comment buttons
    post_buttons_frame = Frame(posts_frame_canvas, bg="white", height=100)
    post_buttons_frame.pack(side=TOP, fill=X)

    # Create a thumbs up image for like button
    like_image_label = Label(post_buttons_frame, image=like_button_image, bg="white")
    like_image_label.pack(side=LEFT, padx=5, pady=5)

    # Create a like button
    #like_button = Button(post_buttons_frame, text="Like", font=("Segoe UI", 14), fg="#FF0800", bg="white", bd=0, command=change_img)
    #like_button = Button(post_buttons_frame, text="Like", font=("Segoe UI", 14), fg="#FF0800", bg="white", bd=0, command=lambda post_index=i: change_img(post_index))
    like_button = Button(post_buttons_frame, text="Like", font=("Segoe UI", 14), fg="#FF0800", bg="white", bd=0, command=lambda: change_img(like_image_label, like_button_image))
    like_button.pack(side=LEFT)

    comment_image_label = Label(post_buttons_frame, image=comment_button_image, bg="white")
    comment_image_label.pack(side=LEFT, padx=5, pady=5)


    # Create a comment button
    comment_button = Button(post_buttons_frame, text="Comment", font=("Segoe UI", 14), fg="#19BDFF", bg="white", bd=0 , command=open_comment_window)
    comment_button.pack(side=LEFT, padx=5)

    comment_count = Label(post_buttons_frame, text="comments")

    posts_gap_label = Label(posts_frame_canvas, text="", font=("Segoe UI", 16), padx=20, pady=10)
    posts_gap_label.pack(side=TOP)

# Update the canvas to show the posts
posts_frame_canvas.update_idletasks()
posts_canvas.configure(scrollregion=posts_canvas.bbox("all"))

root.mainloop()