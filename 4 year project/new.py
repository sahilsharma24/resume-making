from Tkinter import*
import ttk
import Tix
from Tkconstants import *
import pygame
import random
import time
import os
from math import log
import coordinates,message,adjacent_matrix,cluster
#constant
RADIUS =120
SPEED=.1

#global variable
POSx=[0]*16
POSy=[0]*16
msg1=[[0 for i in range(16)] for y in range(16)]
msg2=[[0 for i in range(16)] for y in range(16)]
my=[0]*16
g=[0]*16
root=Tk()
flag=0
flagforroute=0
source=0
destination=0
show_range=0
flag_for_matrix=0
clustering=0
t=time.time()
t1=time.time()+2
turn=0
def route_the_message(screen):
    i=0
    j=-1
    smlx=100
    smly=100
    global source
    global flagforroute
    global destination
    i=0
    smli=source
    while i<15:
        if (i!=source)&(i!=j):
            if (POSy[i]>=POSy[source]-RADIUS)&(POSy[i]<=POSy[source]+RADIUS):
                if (POSx[i]>=POSx[source]-RADIUS)&(POSx[i]<=POSx[source]+RADIUS):
                    if i==destination:
                            flagforroute=0
                            smli=i
                            break
                    elif (abs(POSx[source]-POSx[i])<smlx)&(abs(POSy[source]-POSy[i])<smly):
                        smlx=abs(POSx[source]-POSx[i])
                        smly=abs(POSy[source]-POSy[i])
                        smli=i
        i+=1
        pygame.draw.line(screen,(200,200,200),(POSx[source],POSy[source]),(POSx[smli],POSy[smli]),1)
        j=source
        source=smli

def messages(a):
    global msg1,msg2,my
    if a==1:
        i=0
        while i<16:
            j=i+1
            print "node",i ,"broadcast hello message"
            while j<16:
                if (abs(POSx[i]-POSx[j])<=RADIUS)&(abs(POSy[i]-POSy[j])<=RADIUS):
                    msg1[i][j]=(POSx[i]-POSx[j])**2+(POSy[i]-POSy[j])**2
                    if msg1[i][j]>0:
                        msg1[i][j]=1/float(msg1[i][j])
                        msg1[j][i]=msg1[i][j]
                    else:
                        msg1[j][i]=msg1[i][j]=0
                else:
                    msg1[i][j]=msg1[j][i]=0
                j+=1
            i+=1
    if a==2:
        i=0
        while i<16:
            j=i+1
            while j<16:
                if (abs(POSx[i]-POSx[j])<=RADIUS)&(abs(POSy[i]-POSy[j])<=RADIUS):
                    msg2[i][j]=(POSx[i]-POSx[j])**2+(POSy[i]-POSy[j])**2
                    if (msg1[i][j]>0)&(msg2[i][j]>0):
                        msg2[i][j]=1/float(msg2[i][j])
                        msg2[i][j]=10*log(msg2[i][j]/float(msg1[i][j]),10)
                    else:
                        msg2[i][j]=0
                    msg2[j][i]=msg2[i][j]
                else:
                    msg2[i][j]=msg1[j][i]=0
                j+=1
            j=0
            s=0
            k=0
            while j<16:
                if msg2[i][j]!=0:
                    msg2[i][j]=float("%.2f" %msg2[i][j])**2
                    s+=msg2[i][j];
                    k+=1
                j+=1
            if k!=0:
                my[i]=s/k
            else:
                my[i]=0
            i+=1
class Nodes:
    def __init__(self,node_background,x):
        self.d1=1;
        self.d2=1;
        self.node=x;
        self.node_bg=node_background;
        self.X=random.randint(RADIUS,480)
        self.Y=random.randint(RADIUS,480)

    def draw8point(self,X,Y,xc,yc):
        self.node_bg.set_at((X+xc, Y+yc),(200,200,200))
        self.node_bg.set_at((X-xc, Y+yc),(200,200,200))
        self.node_bg.set_at((X+xc, Y-yc),(200,200,200))
        self.node_bg.set_at((X-xc, Y-yc),(200,200,200))
        self.node_bg.set_at((X+yc, Y+xc),(200,200,200))
        self.node_bg.set_at((X-yc, Y+xc),(200,200,200))
        self.node_bg.set_at((X+yc, Y-xc),(200,200,200))
        self.node_bg.set_at((X-yc, Y-xc),(200,200,200))

    def draw(self):
        x=0;
        y=RADIUS
        p=1-RADIUS

        #calculate coordinates
        if self.X<0 or self.X>600:
            self.d1=-self.d1
        if self.Y<0 or self.Y>600:
            self.d2=-self.d2
        self.X=self.X+random.randint(0,5)*self.d1;
        self.Y=self.Y+random.randint(0,5)*self.d2;
        POSx[self.node]=self.X;
        POSy[self.node]=self.Y;

        global turn,t,t1,flag,flagforroute,source,destination,flag_for_matrix,clustering
        global msg1,msg2,my
        #send coordinates to adjacent_matrix module
        if flag_for_matrix==1:
            adjacent_matrix.show(POSx,POSy)

        # mobility based clustring

        if (t+5<time.time())&(turn==0):
            messages(1);
            t1=time.time()
            turn=1

        if (t1+2<time.time())&(turn==1):
            messages(2)
            t=time.time()
            turn=0
        #send coordinates to coordinates module
        if flag==1:
            coordinates.show(POSx,POSy);

        if clustering==1:
            i=0
            while i<16:
                j=i+1
                sml=0
                k=i
                while j<16:
                    if abs(POSx[i]-POSx[j])<=120:
                        if abs(POSy[i]-POSy[j])<=120:
                            if my[j]<my[i]:
                                j=20;
                                g[i]=' '
                                break;
                    j+=1
                if j!=20:
                    j=0
                    g[i]=' '
                while j<16:
                    if abs(POSx[i]-POSx[j])<=120:
                        if abs(POSy[i]-POSy[j])<=120:
                            g[i]=g[i]+','+str(j)
                            pygame.draw.line(self.node_bg,(200,200,200),(POSx[i],POSy[i]),(POSx[j],POSy[j]),1)
                    j+=1
                i+=1
                cluster.show(g,my)
        #get source and destination node for sending message
        if message.flag==1:
            source=message.contents.get()
            destination=message.contentd.get()
            flagforroute=1
            message.flag=0

        if flagforroute==1:
            route_the_message(self.node_bg)
            print source
        #draw node no
        self.node_bg.set_at((self.X,self.Y),(200,200,200))
        font=pygame.font.Font(None,22);
        if (flagforroute==1)&(self.node==source):
            textimg =font.render(str(self.node), 1,(0,255,0), (100,100,100))
        elif (flagforroute==1)&(self.node==destination):
                textimg =font.render(str(self.node), 1,(255,0,0), (100,100,100))
        else:
            textimg =font.render(str(self.node), 1,(255,255,255), (100,100,100))
        self.node_bg.blit(textimg, (self.X-7,self.Y-7))

        #implement circle drawing algorithm
        global show_range
        if show_range==1:
            while x<=y:
                x=x+1;
                if p<0:
                    p=p+2*x+1;
                else:
                    y=y-1;
                    p=p+2*(x-y)+1
                self.draw8point(self.X,self.Y,x,y)

class Application(Frame):
    def __init__(self,master=None):
        self.master=master;
    def create(self):
        embed=Frame(self.master,width=600,height=600)
        embed.pack()
        os.environ['SDL_WINDOWID'] = str(embed.winfo_id())
        self.master.update()
        pygame.init()
        pygame.display.set_caption ("Launching of Sleep Deprivation Torture Attack");
        screen=pygame.display.set_mode((600,600))#,pygame.FULLSCREEN

        #surface for nodes
        node_background=pygame.Surface((600,600))
        node_background.fill((100,100,100))
        screen.blit(node_background,(0,0))
        pygame.display.flip()
        x=500

        #create nodes
        objects=[]

        for x in range (16):
            o=Nodes(node_background,x)
            objects.append(o)

        while 1:
            node_background.fill((100,100,100))
            for o in objects:
                o.draw()
            screen.blit(node_background,(0,0))
            pygame.display.flip()
            time.sleep(SPEED)

            self.master.update()


def coord():
    global flag,flag_for_matrix,clustering
    root1=Toplevel(root)
    coordinates.main(root1)
    flag=1
    flag_for_matrix=0
    clustering=0

def msg():
    message.main(root)

def show_range():
    global show_range
    show_range=1

def remove_range():
    global show_range
    show_range=0

def clust():
    global flag,flag_for_matrix,clustering
    root1=Toplevel(root)
    adjacent_matrix.main(root1)
    flag=0
    flag_for_matrix=1
    clustering=0

def clustering():
    global clustering,flag,flag_for_matrix;
    root1=Toplevel(root)
    cluster.main(root1)
    clustering=1
    flag=0
    flag_for_matrix=0
def main():
    app=Application(master=root)
    app.master.title("simulation")

    menubar=Menu(root)
    filemenu=Menu(menubar)
    filemenu.add_command(label="Coordinate",command=coord)
    filemenu.add_separator()
    filemenu.add_command(label="ADJACENT_MATRIX",command=clust)
    filemenu.add_separator()
    filemenu.add_command(label="Start Clustring",command=clustering)
    filemenu.add_separator()
    filemenu.add_command(label="Exit",command=root.destroy)

    filemenu2=Menu(menubar)
    filemenu2.add_command(label="Message",command=msg)
    filemenu2.add_separator()
    filemenu2.add_command(label="Show range",command=show_range)
    filemenu2.add_separator()
    filemenu2.add_command(label="Remove range",command=remove_range)
    filemenu2.add_separator()
    filemenu2.add_command(label="Exit")


    menubar.add_cascade(label="FILE",menu=filemenu)
    menubar.add_cascade(label="EDIT",menu=filemenu2)
    root.config(menu=menubar)
    app.create()
    app.mainloop()
    root.destroy()
if __name__ == '__main__':
     main()
