from tkinter import *
from tkinter.messagebox import showinfo

# include Frame to make the class as gui object
class MyGui(Frame):
    # base definition
    # structure and corresponding func
    def __init__(self): #self indicating an instance of the class
        Frame.__init__(self)
        button = Button(self,text='press',command=self.reply)
        button.pack()
    # some other defining func
    def reply(self):  #self included as indicator to use the func
        showinfo(title='button pressed',message='hello')

# indentifier of the running progress
if __name__=='__main__':
    # make a object from the class
    window=MyGui()
    window.pack()
    window.mainloop()



