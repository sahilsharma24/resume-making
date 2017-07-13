from Tkinter import*
import ttk
import Tix
from Tkconstants import *
contents=0
contentd=0
flag=0
def fun():
    global contents
    global contentd
    global flag
    flag=1
class application(Frame):
    a=1
    def __init__(self,master=None):
        Frame.__init__(self,master,relief=RAISED,borderwidth=5,width=100,height=1000)
        self.pack()
        self.master=master
        self.create()

    def create(self):
        global contents
        global contentd
        contents=IntVar()
        contentd=IntVar()

        self.Label1=Label(self,text="NODES PARAMETERS",font=("Times", 20, "bold"),bg="grey",fg="black").grid(row=0,column=1)
        self.Label2=Label(self,text="SOURCE",font=("Times", 20, "bold"),fg="black").grid(row=1,column=0,pady=10)
        self.Label3=Label(self,text="DESTINATION",font=("Times", 20, "bold"),fg="black").grid(row=2,column=0,pady=10)

        self.enter1 = Entry(self,fg="green",textvariable=contents).grid(row=1,column=2)
        self.enter2 = Entry(self,fg="red",textvariable=contentd).grid(row=2,column=2)

        self.button=Button(self,text="SUBMIT",command=fun).grid(row=3,column=1)
        self.master.update()
def main(root):
    root1=Toplevel(root)
    app = application(master=root1)
    #app.mainloop()
    #app.master.maxsize(50,50)
    #root.destroy()
if __name__ == '__main__': main()
