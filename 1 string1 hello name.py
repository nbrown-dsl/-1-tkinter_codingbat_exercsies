#coding bat exercsie
# https://codingbat.com/prob/p115413

from tkinter import *
import webbrowser
 
root = Tk()
 
e = Entry(root, width=25, borderwidth=15,font=("Courier", 44))
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)

#create link to problem
link1 = Label(root, text="codingbat exercise", fg="blue", cursor="hand2")
link1.bind("<Button-1>", lambda e: webbrowser.open_new(r"https://codingbat.com/prob/p115413"))
link1.grid(row=6,column=0,columnspan=3)

 
def button_click():
   
    name1 = e.get()       
    answer = "Hello "+name1 + "!"
    e.delete(0,END)
    e.insert(0,answer)
    
button_equal = Button(root,text="SUBMIT",padx=91,pady=20,command=lambda: button_click())
button_equal.grid(row=5,column=0,columnspan=3)
root.mainloop()
