from tkinter import *
from tkinter import messagebox
import numpy as np
import random
class App:
    def __init__(self):
        self.root=Tk()
        self.root.title("Tic Tak Toc")
        self.root.geometry("300x300+300+50")
        self.l=[]
        self.l1=[0,0,0,0,0,0,0,0,0]
        self.array=np.zeros(9).reshape(3,3)
        c=0
        self.flag=True
        
        self.root.configure(bg="white")
        for i in range(3):
            for j in range(3):
                self.l.append(Label(self.root,height=5,width=10,bg="white",relief=GROOVE))
                self.l[c].grid(row=i,column=j,padx=12,pady=6)
                self.l[c].bind( "<Button>", self.mouseClick )
                c+=1
        
        self.root.mainloop()
        
    def mouseClick( self,event ): 
        if len(event.widget.cget("text")) == 0:
            index=(str(event.widget))[-1]
            if index== 'l':
                n=1
            else:
                n=int(index)
            self.l1[n-1]=n
            if self.flag==True: 
                
                event.widget.config(text="X",font=("arial",23),fg="red",height=2,width=4)
                i=(n-1)//3
                j=n-(3*i)-1
                self.array[i][j]=1
                self.check()
                #self.flag=False
                n1=self.generateNumber()
                print(n1)
                self.l1[n1-1]=n1
                self.computer(n1)        
        else:
            messagebox.showwarning(" Tic Tak Toe", "Invalid Move !")
            return
    def check(self):
        if np.all(self.array[0]==1) or np.all(self.array[1]==1) or np.all(self.array[2]==1):
            messagebox.showinfo("   Tic Tak Toe", "You Win")
            self.reset()
        elif np.all(self.array[:,[0]]==1) or np.all(self.array[:,[1]]==1) or  np.all(self.array[:,[2]]==1):
            messagebox.showinfo("   Tic Tak Toe", "You Win")
            self.reset()
        elif (self.array[0][0]==1 and self.array[1][1]==1 and self.array[2][2]==1) or (self.array[0][2]==1 and self.array[1][1]==1 and self.array[2][0]==1) :
            messagebox.showinfo("   Tic Tak Toe", "You Win")
            self.reset()
        
        elif np.all(self.array[0]==2) or np.all(self.array[1]==2) or np.all(self.array[2]==2):
            messagebox.showinfo("   Tic Tak Toe", "Computer Win")
            self.reset()
        elif np.all(self.array[:,[0]]==2) or np.all(self.array[:,[1]]==2) or  np.all(self.array[:,[2]]==2):
            messagebox.showinfo("   Tic Tak Toe", "Computer Win")
            self.reset()
        elif (self.array[0][0]==2 and self.array[1][1]==2 and self.array[2][2]==2) or (self.array[0][2]==2 and self.array[1][1]==2 and self.array[2][0]==2) :
            messagebox.showinfo("   Tic Tak Toe", "Computer Win")
            self.reset()
        
        if  0 not in self.array:
            messagebox.showinfo("showinfo", "Draw")
            self.reset()
    def generateNumber(self):
        c=[i for i in range(1,10)]
        d=list(set(c)-set(self.l1))
        n1=random.choice(d)
        return n1
    def computer(self,n1):
        self.l[n1-1].config(text="O",font=("arial",23),fg="blue",height=2,width=4)
        i=(n1-1)//3
        j=n1-(3*i)-1
        self.array[i][j]=2
        self.check()
        print(self.array)

            
                    
    def style(self,e1,e2,e3):
        e1.config(bg="light green") 
        e2.config(bg="light green") 
        e3.config(bg="light green") 
    def reset(self):
        for i in self.l:
            i.config(text="")
        self.array=np.zeros(9).reshape(3,3)
        self.l1=[0 for i in range(0,9)]
        
App()