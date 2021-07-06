from tkinter import *
#kalkulators
root = Tk()
root.title('Kalkulators')
root['bg']='#E7EEFF'
root.geometry('274x270')
root.resizable(width=False, height=False)
atb = Entry(root, width=30, borderwidth=5)
atb.grid(row=0, column=1, columnspan=4, padx=8, pady=10)

#funkcijas

def poga_click(skaitlis):
    current = atb.get()
    atb.delete(0, END)
    atb.insert(0, str(current) + str(skaitlis))

def poga_plus():
    pirmais_skaitlis = atb.get()
    global p_sk
    global math
    math = "skaitishana"
    p_sk = float(pirmais_skaitlis)
    atb.delete(0, END)

def poga_minus():
    pirmais_skaitlis = atb.get()
    global p_sk
    global math
    math='atnemshana'
    p_sk = float(pirmais_skaitlis)
    atb.delete(0, END)

def poga_dalit():
    pirmais_skaitlis = atb.get()
    global p_sk
    global math
    math='dalishana'
    p_sk = float(pirmais_skaitlis)
    atb.delete(0, END)
    
def poga_reiz():
    pirmais_skaitlis = atb.get()
    global p_sk
    global math
    math='reizinashana'
    p_sk = float(pirmais_skaitlis)
    atb.delete(0, END)

def poga_vienad():
    otr_sk = atb.get()
    atb.delete(0, END)

    if math == "skaitishana":
        atb.insert(0, p_sk + float(otr_sk))

    if math == "atnemshana":
        atb.insert(0, p_sk - float(otr_sk))

    if math == "dalishana":
        atb.insert(0, p_sk / float(otr_sk))

    if math == "reizinashana":
        atb.insert(0, p_sk * float(otr_sk))

def poga_clear():
    atb.delete(0, END)



#pogas 

poga_1 = Button(root, text='1', padx=25, pady=15, borderwidth=3, command=lambda: poga_click(1))
poga_2 = Button(root, text='2', padx=25, pady=15, borderwidth=3, command=lambda: poga_click(2))
poga_3 = Button(root, text='3', padx=26, pady=15, borderwidth=3, command=lambda: poga_click(3))

poga_4 = Button(root, text='4', padx=25, pady=15, borderwidth=3, command=lambda: poga_click(4))
poga_5 = Button(root, text='5', padx=25, pady=15, borderwidth=3, command=lambda: poga_click(5))
poga_6 = Button(root, text='6', padx=26, pady=15, borderwidth=3, command=lambda: poga_click(6))

poga_7 = Button(root, text='7', padx=25, pady=15, borderwidth=3, command=lambda: poga_click(7))
poga_8 = Button(root, text='8', padx=25, pady=15, borderwidth=3, command=lambda: poga_click(8))
poga_9 = Button(root, text='9', padx=26, pady=15, borderwidth=3, command=lambda: poga_click(9))

poga_0 = Button(root, text='0', padx=25, pady=15, borderwidth=3, command=lambda: poga_click(0))
poga_vienad = Button(root, text='=', padx=25, pady=15, borderwidth=3, command=poga_vienad)
poga_clear = Button(root, text='C', padx=25, pady=15, borderwidth=3, command=poga_clear)

poga_punkts = Button(root, text='.', padx=27, pady=10, borderwidth=3, bg="#BDC9CE", command=lambda: poga_click('.'))

#Darbības pogas
poga_plus = Button(root, text='+', padx=24, pady=15, borderwidth=3, command=poga_plus)
poga_minus = Button(root, text='-', padx=25, pady=15, borderwidth=3, command=poga_minus)
poga_dalit = Button(root, text='/', padx=25, pady=15, borderwidth=3, command=poga_dalit)
poga_reiz = Button(root, text='*', padx=25, pady=15, borderwidth=3, command=poga_reiz)

#izvade

poga_0.grid(row=4, column=0)
poga_clear.grid(row=4, column=2)
poga_vienad.grid(row=4, column=1)
poga_plus.grid(row=4, column=3)

poga_1.grid(row=3, column=0)
poga_2.grid(row=3, column=1)
poga_3.grid(row=3, column=2)
poga_minus.grid(row=3, column=3)

poga_4.grid(row=2, column=0)
poga_5.grid(row=2, column=1)
poga_6.grid(row=2, column=2)
poga_reiz.grid(row=2, column=3)

poga_7.grid(row=1, column=0)
poga_8.grid(row=1, column=1)
poga_9.grid(row=1, column=2)
poga_dalit.grid(row=1, column=3)

poga_punkts.grid(row=0, column=0)

#Rādīt programmu
mainloop()