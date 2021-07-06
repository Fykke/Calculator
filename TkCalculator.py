from tkinter import *
#functions
def Plus():
    answ=int(a.get())+int(b.get())
    myText.set(answ)

def Minus():
    answ=int(a.get())-int(b.get())
    myText.set(answ)

def Multiplication():
    answ=int(a.get())*int(b.get())
    myText.set(answ)

def Division():
    answ=int(a.get())/int(b.get())
    myText.set(answ)

def Clear():
    a.delete(0, 'end')
    b.delete(0, 'end')
    answer.delete(0, 'end')

root = Tk()
root.title('Calc')
root.geometry('200x211')
root.resizable(width=False, height=False)
root['bg']='#DFDFDF'
myText=StringVar()

#Buttons
answer = Entry(root, text="", textvariable=myText, width=16, bg='#8C958F', font='Helvetica 14 bold')
a = Entry(root, width=31, borderwidth=5)
b = Entry(root, width=31, borderwidth=5)
plus_btn = Button(root, text="+", command=Plus, width=26)
minus_btn = Button(root, text="-", command=Minus, width=26)
mult_btn = Button(root, text="*", command=Multiplication, width=26)
div_btn = Button(root, text="/", command=Division, width=26)
clear_btn = Button(root, text="Clear", command=Clear,width=26)

#Output
a.pack()
b.pack()
plus_btn.pack()
minus_btn.pack()
mult_btn.pack()
div_btn.pack()
clear_btn.pack()
answer.pack()
mainloop()