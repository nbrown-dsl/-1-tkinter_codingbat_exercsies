#coding bat exercsie
# https://codingbat.com/prob/p115413

from tkinter import *
 
root = Tk()
 
e = Entry(root, width=25, borderwidth=15,font=("Courier", 44))
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)
 
def button_click():
   
    name1 = e.get()       
    answer = "Hello "+name1 + "!"
    e.delete(0,END)
    e.insert(0,answer)
    
button_equal = Button(root,text="SUBMIT",padx=91,pady=20,command=lambda: button_click())
button_equal.grid(row=5,column=0,columnspan=3)
root.mainloop()
