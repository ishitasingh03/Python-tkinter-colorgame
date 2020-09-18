
import tkinter as tk
import random
color=['Red','Blue','Green','Orange','Yellow','Purple','Brown','Black']

score=0
timeleft=30

def startgame(event):
    if timeleft==30:
        countdown()
    showcolor()

def countdown():
    global timeleft
    if timeleft>0:
        timeleft-=1
        tl.config(text="Time left: "+str(timeleft))
        tl.after(1000,countdown)
    else:
        sl.config(text="Times Up ")
        tl.config(text="Final Score is  "+str(score))
        l1.config(text=" ")
        l2.pack_forget()
        e1.pack_forget()
        
        
        
def showcolor():
    global score
    global timeleft
    if(timeleft>0):
        if(e1.get().lower()==color[1].lower()):
            score=score+1
            sl.config(text="Score: "+str(score))
            l2.config(text=" ")
            e1.delete(0,tk.END)
            random.shuffle(color)
            l1.config(fg=color[1],text=color[0])
        else:
            l2.config(text="Wrong answer")
            
            
            
            
    
root=tk.Tk()
root.title("Colour Game")

tk.Label(root,text="Lets begin the game\nEnter the colour of the word",fg='purple',font=('Helvetica',20)).pack()
sl=tk.Label(root,text="Score: "+str(score),font=('Helvetica',20))
sl.pack()
tl=tk.Label(root,text="Time left: "+str(timeleft),font=('Helvetica',20))
tl.pack()
l1=tk.Label(root,text="",font=('Helvetica',60))
l1.config(fg=color[1],text=str(color[0]))
l1.pack()
l2=tk.Label(root,text=" ")
l2.pack()
e1=tk.Entry(root)
root.bind('<Return>',startgame)
e1.pack()
tk.mainloop()
