#coding bat exercsie
# https://codingbat.com/prob/p124676

from tkinter import *
 
root = Tk()
 
e = Entry(root, width=35, borderwidth=15,font=("Courier", 44))
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)
 
def button_click():   
    n = e.get()
    e.delete(0,END)
    if (abs(100-int(n))<=10) or (abs(200-int(n))<=10):
        ans = "Within 10 of 100 or 200"
    else:
        ans = "Not within 10 of 100 or 200" 
    e.insert(0,ans)
       
button_equal = Button(root,text="CALCULATE",padx=91,pady=20,command=lambda: button_click())
button_equal.grid(row=5,column=0,columnspan=3)
 
root.mainloop()
