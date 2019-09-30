from tkinter import *
window=Tk()
window.title("TODO-LIST APP")
content=Listbox(window,font="ariel 25 italic")
task=StringVar()
e=Entry(window,textvariable=task,font="Ariel 20")
#lamda func used so that no need to define any function elsewhere
add=Button(window,text="ADD",font="Ariel 20",bg="chartreuse1",command=lambda content=content,task=task:content.insert(END,task.get()))
delete=Button(window,text="DELETE",font="Ariel 20",bg="#FF6103",command=lambda content=content: content.delete(ANCHOR))
#anchor used so comp. knows that selected text need to be deleted

content.grid(row=0,column=0,columnspan=2,padx=5,pady=10)
e.grid(row=2,column=0,columnspan=2,padx=5,pady=10)
labeluser=Label(window,text="Enter Task Below",fg="firebrick1")
labeluser.grid(row=1)
add.grid(row=3,column=0,padx=35,pady=20)
delete.grid(row=3,column=1,padx=35,pady=20) 
window.mainloop() 
