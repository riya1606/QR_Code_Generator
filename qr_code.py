# We import all the necessary modules in the application.
from tkinter import *
from tkinter import messagebox
import pyqrcode

# Here ws is the main workspace for the qr generator and variable for Tk() class method.
ws = Tk()
# QR Code Generator in the title
ws.title("QR Code Generator")
# Setting the background color for the workspace
ws.config(bg='#ffff00')


# Function to generate QR Code

def generate_QR():
    # If the user has given some input URL or Message then we generate the QR Code using the pyqrcode module in python.
    if len(user_input.get())!=0 :
        global qr,img
        qr = pyqrcode.create(user_input.get())
        # We render the QR Code in XBM format
        img = BitmapImage(data = qr.xbm(scale=8))
    else:
        # If there is no input then we show a warning message
        messagebox.showwarning('warning', 'All Fields are Required!')
    # The try block lets you test a block of code for errors. The except block lets you handle the error.
    try:
        display_code()
    except:
        pass
# This function displays the code in the workspace
def display_code():
    img_lbl.config(image = img)
    output.config(text="QR code of " + user_input.get())


lbl = Label(ws, text="Enter message or URL",bg='#ffff00')
lbl.pack()

user_input = StringVar()
entry = Entry(
    ws,
    textvariable = user_input
    )
entry.pack(padx=10)


button = Button(
    ws,
    text = "Generate QR",
    width=15,
    command = generate_QR
    )
button.pack(pady=10)

img_lbl = Label(
    ws,
    bg='#ffff00')
img_lbl.pack()
output = Label(
    ws,
    text="",
    bg='#ffff00'
    )
output.pack() 
ws.mainloop()