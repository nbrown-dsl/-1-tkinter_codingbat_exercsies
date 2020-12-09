# https://codingbat.com/prob/p107863

from tkinter import *
 
root = Tk()
 
e = Entry(root, width=25, borderwidth=15,font=("Courier", 44))
e.grid(row=0,column=0,columnspan=1,padx=10,pady=10)
f = Entry(root, width=25, borderwidth=15,font=("Courier", 44))
f.grid(row=1,column=0,columnspan=1,padx=10,pady=10)
g = Entry(root, width=25, borderwidth=15,font=("Courier", 44))
g.grid(row=2,column=0,columnspan=1,padx=10,pady=10)
 
def button_click():   
    a = e.get()
    e.delete(0,END)
    b = f.get()
    f.delete(0,END)
    c = g.get()
    g.delete(0,END)
    
    if a=="13":
        ans = 0
    elif b=="13":
        ans = a
    elif c=="13":
        ans = int(a)+int(b)
    else:
        ans = int(a)+int(b)+int(c)
    e.insert(0,ans)
       
button_equal = Button(root,text="CALCULATE",padx=91,pady=20,command=lambda: button_click())
button_equal.grid(row=5,column=0,columnspan=3)
 
root.mainloop()
