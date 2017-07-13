from Tkinter import*
import ttk
import Tix
from Tkconstants import *

cn1=[0]*16
cn2=[0]*16
def show (g,m):
    global cn2,cn1
    i=0
    while i<16:
        cn1[i].set(g[i])
        #cn2[i].set(m[i])
        i=i+1
class application(Frame):
    a=1
    def __init__(self,master=None):
        Frame.__init__(self,master,relief=RAISED,borderwidth=5,width=100,height=1000)
        self.pack()
        self.master=master
        self.create()

    def create(self):
        global cn2,cn1
        i=0
        while i<16:
            cn1[i]=IntVar()
            #cn2[i]=IntVar()
            i+=1
        self.Label1=Label(self,text="CLUSTERING AND CLUSTER HEAD ",font=("Times", 20, "bold"),bg="grey",fg="black").grid(columnspan=2)
        self.Label2=Label(self,text="CLUSTER HEAD",font=("Times", 20, "bold"),fg="black").grid(row=1,column=0,pady=10)
        self.Label3=Label(self,text="CLUSTER",font=("Times", 20, "bold"),fg="black").grid(row=1,column=1,pady=10)

        i=0;
        while (i<16):
            self.Label3=Label(self,text=str(i),font=("Times", 10, "bold"),fg="black",bg='grey',width=20).grid(row=2+i,column=0,pady=5)
            self.enter2 = Entry(self,fg="red",textvariable=cn1[i],width=40).grid(row=2+i,column=1,pady=5)
            #self.enter2 = Entry(self,fg="red",textvariable=cn2[i],width=40).grid(row=2+i,column=2,pady=5)
            i=i+1
        self.master.update()

def main(root1):
    app = application(master=root1)
    #app.mainloop()
    #app.master.maxsize(50,50)
    #root.destroy()
if __name__ == '__main__': main()
