#coding bat exercise
# https://codingbat.com/prob/p179078

from tkinter import *
 
root = Tk()
 
e = Entry(root, width=35, borderwidth=15,font=("Courier", 44))
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)
 
def button_click():   
    n = e.get()
    e.delete(0,END)
    
    if n[0] == n[len(n)-1]:
            ans = "first and last the same"
    else:
         ans = "first and last not the same" 
    e.insert(0,ans)
       
button_equal = Button(root,text="CALCULATE",padx=91,pady=20,command=lambda: button_click())
button_equal.grid(row=5,column=0,columnspan=3)
 
root.mainloop()
