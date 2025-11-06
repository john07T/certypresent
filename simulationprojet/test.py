import tkinter as tk
from tkinter import PhotoImage

def closeWindows(framtime):
    framtime.place_forget()
    
def menu(fen):
    frameMen=tk.Frame(fen,width=500,height=800,bg="grey")
    frameMen.place(x=-25,y=2)
    frame2=tk.Frame(frameMen,width=300,height=100,bg="purple")
    fer=PhotoImage(file="fermeture.png")
    bfermer=tk.Button(frame2,#image=fer,
                      text="fermeture",
                      font=( "Arial" ,12),
                      command=lambda: closeWindows(frameMen),
                      bd=0,
                      fg="white",
                      bg="purple",
                      )
    bfermer.pack(side="right")
    frame2.place(relx=0.003,rely=0.0,relwidth=1,relheight=0.10)
    #buttons ou option du frame
    
    butmun=tk.Button(frameMen,
                     text="Enregistrement",
                     font=("Arial-bac",14),
                     bd=0,
                     width=50,
                     command=None)
    butmun.place(relx=0.05,rely=0.11)
    
    butmun=tk.Button(frameMen,text="Execution",
                     font=("Arial-bac",14),
                     bd=0,
                    width=50,
                     command=None)
    butmun.place(relx=0.05,rely=0.15)
    
    butmun=tk.Button(frameMen,text="Base de donne",font=("Arial-bac",14),
                     bd=0,
                    width=50,
                     command=None
                     )
    butmun.place(relx=0.05,rely=0.19)
    return frameMen