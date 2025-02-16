from tkinter import*

root=Tk()
root.title("Demo")                   

def Click():
    myLabel=Label(root,text="Hello Shakil!")
    myLabel.pack()



#state=DISABLED
#mybutton=Button(root,text="Click me!",padx=20,pady=14)
mybutton=Button(root,text="Click me!",padx=20,pady=14,command=Click,bg="green",fg="red")
mybutton.pack()

root.mainloop()