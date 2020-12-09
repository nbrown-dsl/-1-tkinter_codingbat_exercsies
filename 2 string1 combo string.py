#coding bat exercise
# https://codingbat.com/prob/p194053

from tkinter import *
 
root = Tk()
 
e = Entry(root, width=25, borderwidth=15,font=("Courier", 44))
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)
 
f = Entry(root, width=25, borderwidth=15,font=("Courier", 44))
f.grid(row=1,column=0,columnspan=3,padx=10,pady=10)
 
def button_click():
   
    name1 = e.get()
    e.delete(0,END)
    name2 = f.get()
    f.delete(0,END)
    if len(name1) < len(name2):
        answer = name1+name2+name1
    else:
        answer = name2+name1+name2
    e.insert(0,answer)
    
button_equal = Button(root,text="=",padx=91,pady=20,command=lambda: button_click())
button_equal.grid(row=5,column=0,columnspan=3)
root.mainloop()
