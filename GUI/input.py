from tkinter.messagebox import showinfo
from tkinter import *

def reply(name):
    showinfo(message=f'hello {name}!')

# construct obj
window=Tk()
window.title('input')

# set the question of input required
# the side indicates where the obj appears
# top = center and upper position for current element
Label(window,text='Enter your name: ').pack(side=TOP)
# construct entry obj to get response
ent=Entry(window)
# bottom = lowest position after all element
# the first element will be more lower than the after
ent.pack(side=BOTTOM)

# use lambda instead of the direct func
# it will direct call out the func before accept entry
btn = Button(window,text='submit',command=(lambda:reply(ent.get())))
btn.pack(side=BOTTOM)

window.mainloop()


