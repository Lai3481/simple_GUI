from tkinter import *
from OOP import MyGui
from tkinter.messagebox import showinfo

class customGui(MyGui):
    def reply(self):
        # use if extends from the parent class
        # return super().reply()
        showinfo(title='pop',message='bye')

if __name__=='__main__':
    custom=customGui()
    custom.pack()
    custom.mainloop()