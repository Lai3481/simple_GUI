from tkinter import *
from tkinter.messagebox import showinfo

# window with label only
Label(text='haha').pack()

# make a message
# using function to avoid inlogical move
# direct use reply = showinfo() will appear itself in other window
def reply():
    showinfo(message='hello')

# construct a window with button
window=Tk()
button=Button(window,text='press',command=reply)
button.pack()
# run
window.mainloop()