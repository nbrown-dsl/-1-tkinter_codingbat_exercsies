# from coding bat exercise
# https://codingbat.com/prob/p149524

from tkinter import *
 
root = Tk()
 
e = Entry(root, width=25, borderwidth=15,font=("Courier", 44))
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)
 
f = Entry(root, width=5, borderwidth=15,font=("Courier", 44))
f.grid(row=1,column=0,columnspan=1,padx=10,pady=10)
 
def button_click():  
    name1 = e.get()
    e.delete(0,END)
    n = f.get()
    f.delete(0,END)
    front = name1[:int(n)]   # up to but not including n
    back = name1[int(n)+1:]  # n+1 through end of string
  
    e.insert(0,front + back)
    
button_equal = Button(root,text="CALCULATE",padx=91,pady=20,command=lambda: button_click())
button_equal.grid(row=5,column=0,columnspan=3)
 
root.mainloop()
