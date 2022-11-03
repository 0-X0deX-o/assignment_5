import tkinter as tk

window = tk.Tk()
window.geometry("600x400")

name_var = tk.StringVar()
passw_var = tk.StringVar()

# defining a function that will
# get the name and password and
# print them on the screen

def submit():
    
    name = name_var.get()
    password = passw_var.get()

    print('The name is : ' + name)
    print('The password is: ' + password)

    name_var.set('')
    passw_var.set('')
    

    name_label  = tk.Label(
            window,
            text = "Username",
            font = ('calibre', 10, 'bold'),
            )

    name_entry = tk.Entry(
            window,
            textvariable = name_var, font = ('calibre',10,'normal'),
            )

    # creating a label for password
    passw_label = tk.Label(
            window,
            text =  'Password',
            font = ('calibre',10,'bold'),
            )

    # creating an entry for password
    passw_entry = tk.Entry(
            window, 
            textvariable = passw_var,
            font = ('calibre',10,'normal'),
            show = '*'
            )
    

    sub_btn = tk.Button(
            window,
            text = 'Submit', 
            command = submit
            )

   # placing the label and entry in the required position using grid method

    name_label.grid(row = 0,column = 0)
    name_entry.grid(row = 0,column = 1)
    passw_label.grid(row = 1,column = 0)
    passw_entry.grid(row = 1,column = 1)
    sub_btn.grid(row = 2,column = 1)

    window.mainloop()

submit()
# use html color code names, or RGB hex value
#  vim hotkey for finding a certain character in a file
# what all colors can be used in tkinter?
# This is an entry field, are their input validations?
# Where is input data stored?

