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


#Lai pogām pievienotu dažādas krāsas

def on_enter1(e):
    poga_1['background'] = 'SystemButtonFace'
def on_leave1(e):
    poga_1['background'] = '#BDC9CE'
def on_enter2(e):
    poga_2['background'] = 'SystemButtonFace'
def on_leave2(e):
    poga_2['background'] = '#BDC9CE'
def on_enter3(e):
    poga_3['background'] = 'SystemButtonFace'
def on_leave3(e):
    poga_3['background'] = '#BDC9CE'
def on_enter4(e):
    poga_4['background'] = 'SystemButtonFace'
def on_leave4(e):
    poga_4['background'] = '#BDC9CE'
def on_enter5(e):
    poga_5['background'] = 'SystemButtonFace'
def on_leave5(e):
    poga_5['background'] = '#BDC9CE'
def on_enter6(e):
    poga_6['background'] = 'SystemButtonFace'
def on_leave6(e):
    poga_6['background'] = '#BDC9CE'
def on_enter7(e):
    poga_7['background'] = 'SystemButtonFace'
def on_leave7(e):
    poga_7['background'] = '#BDC9CE'
def on_enter8(e):
    poga_8['background'] = 'SystemButtonFace'
def on_leave8(e):
    poga_8['background'] = '#BDC9CE'
def on_enter9(e):
    poga_9['background'] = 'SystemButtonFace'
def on_leave9(e):
    poga_9['background'] = '#BDC9CE'
def on_enter0(e):
    poga_0['background'] = 'SystemButtonFace'
def on_leave0(e):
    poga_0['background'] = '#BDC9CE'

def on_enterv(e):
    poga_vienad['background'] = 'SystemButtonFace'
def on_leavev(e):
    poga_vienad['background'] = '#BDC9CE'

def on_enterc(e):
    poga_clear['background'] = 'SystemButtonFace'
def on_leavec(e):
    poga_clear['background'] = '#BDC9CE'

def on_enterpt(e):
    poga_punkts['background'] = 'SystemButtonFace'
def on_leavept(e):
    poga_punkts['background'] = '#BDC9CE'

def on_enterp(e):
    poga_plus['background'] = 'SystemButtonFace'
def on_leavep(e):
    poga_plus['background'] = '#BDC9CE'

def on_enterm(e):
    poga_minus['background'] = 'SystemButtonFace'
def on_leavem(e):
    poga_minus['background'] = '#BDC9CE'
    
def on_enterd(e):
    poga_dalit['background'] = 'SystemButtonFace'
def on_leaved(e):
    poga_dalit['background'] = '#BDC9CE'
    
def on_enterr(e):
    poga_reiz['background'] = 'SystemButtonFace'
def on_leaver(e):
    poga_reiz['background'] = '#BDC9CE'

#pogas

poga_1 = Button(root, text='1', padx=25, pady=15, borderwidth=3, bg='#BDC9CE', command=lambda: poga_click(1))
poga_2 = Button(root, text='2', padx=25, pady=15, borderwidth=3, bg='#BDC9CE', command=lambda: poga_click(2))
poga_3 = Button(root, text='3', padx=26, pady=15, borderwidth=3, bg='#BDC9CE', command=lambda: poga_click(3))

poga_4 = Button(root, text='4', padx=25, pady=15, borderwidth=3, bg='#BDC9CE', command=lambda: poga_click(4))
poga_5 = Button(root, text='5', padx=25, pady=15, borderwidth=3, bg='#BDC9CE', command=lambda: poga_click(5))
poga_6 = Button(root, text='6', padx=26, pady=15, borderwidth=3, bg='#BDC9CE', command=lambda: poga_click(6))

poga_7 = Button(root, text='7', padx=25, pady=15, borderwidth=3, bg='#BDC9CE', command=lambda: poga_click(7))
poga_8 = Button(root, text='8', padx=25, pady=15, borderwidth=3, bg='#BDC9CE', command=lambda: poga_click(8))
poga_9 = Button(root, text='9', padx=26, pady=15, borderwidth=3, bg='#BDC9CE', command=lambda: poga_click(9))

poga_0 = Button(root, text='0', padx=25, pady=15, borderwidth=3, bg='#BDC9CE', command=lambda: poga_click(0))
poga_vienad = Button(root, text='=', padx=25, pady=15, borderwidth=3, bg='#BDC9CE', command=poga_vienad)
poga_clear = Button(root, text='C', padx=25, pady=15, borderwidth=3, bg='#BDC9CE', command=poga_clear)

poga_punkts = Button(root, text='.', padx=27, pady=10, borderwidth=3, bg="#BDC9CE", command=lambda: poga_click('.'))

#Darbības pogas
poga_plus = Button(root, text='+', padx=24, pady=15, borderwidth=3, bg='#BDC9CE', command=poga_plus)
poga_minus = Button(root, text='-', padx=25, pady=15, borderwidth=3, bg='#BDC9CE', command=poga_minus)
poga_dalit = Button(root, text='/', padx=25, pady=15, borderwidth=3, bg='#BDC9CE', command=poga_dalit)
poga_reiz = Button(root, text='*', padx=25, pady=15, borderwidth=3, bg='#BDC9CE', command=poga_reiz)

#Lai pogām pievienotu dažādas krāsas
poga_1.bind('<Enter>', on_enter1)
poga_1.bind('<Leave>', on_leave1)
poga_2.bind('<Enter>', on_enter2)
poga_2.bind('<Leave>', on_leave2)
poga_3.bind('<Enter>', on_enter3)
poga_3.bind('<Leave>', on_leave3)
poga_4.bind('<Enter>', on_enter4)
poga_4.bind('<Leave>', on_leave4)
poga_5.bind('<Enter>', on_enter5)
poga_5.bind('<Leave>', on_leave5)
poga_6.bind('<Enter>', on_enter6)
poga_6.bind('<Leave>', on_leave6)
poga_7.bind('<Enter>', on_enter7)
poga_7.bind('<Leave>', on_leave7)
poga_8.bind('<Enter>', on_enter8)
poga_8.bind('<Leave>', on_leave8)
poga_9.bind('<Enter>', on_enter9)
poga_9.bind('<Leave>', on_leave9)
poga_0.bind('<Enter>', on_enter0)
poga_0.bind('<Leave>', on_leave0)
poga_vienad.bind('<Enter>', on_enterv)
poga_vienad.bind('<Leave>', on_leavev)
poga_clear.bind('<Enter>', on_enterc)
poga_clear.bind('<Leave>', on_leavec)
poga_punkts.bind('<Enter>', on_enterpt)
poga_punkts.bind('<Leave>', on_leavept)
poga_plus.bind('<Enter>', on_enterp)
poga_plus.bind('<Leave>', on_leavep)
poga_minus.bind('<Enter>', on_enterm)
poga_minus.bind('<Leave>', on_leavem)
poga_dalit.bind('<Enter>', on_enterd)
poga_dalit.bind('<Leave>', on_leaved)
poga_reiz.bind('<Enter>', on_enterr)
poga_reiz.bind('<Leave>', on_leaver)

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