from tkinter import *
import random

fontsize=30
colors = ['orange','purple','red','blue','yellow','green','cyan']

def ran_color():
    # construct a win at top level(fix position)
    pop=Toplevel()
    ran_color=random.choice(colors)
    # fill = Both indicates filling the whole section
    Label(pop,bg='black',text='Popup',fg=ran_color).pack(fill=BOTH)
    mainlabel.config(fg=ran_color)

def flip():
    mainlabel.config(fg=random.choice(colors))
    # call func after 250ms, meaning a loop
    main.after(250,flip)

def grow():
    global fontsize
    fontsize+=5
    mainlabel.config(font=('arial',fontsize,'italic')) 
    main.after(100,grow)

main=Tk()
mainlabel=Label(main,text='fun')
# fg=foreground=fore_color bg=background_color
mainlabel.config(font=('arial',fontsize,'italic'),fg='cyan',bg='navy')
mainlabel.pack(side=TOP)
Button(main,text='spam',command=ran_color).pack(fill=X)
Button(main,text='flip',command=flip).pack(fill=X)
# pack(fill=x) indicates how the button filling
Button(main,text='grow',command=grow).pack(fill=X)
main.mainloop()