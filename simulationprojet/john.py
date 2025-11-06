import tkinter as tk
from tkinter import PhotoImage
import test 
def fenetre():
    windows=tk.Tk()
    windows.geometry("300x100")
    tet="Application de john".upper()
    tetfebe=tk.Label(windows,text=tet,font=("arial-black",16),bg="purple",fg="lightblue")
    tetfebe.place(relx=0.25,rely=0.9,relheight=0.1,relwidth=0.5)
    #windows.iconbitmap("logoo.ico")
    Image = tk.PhotoImage(file="app1.png")
    canavas=tk.Canvas(windows,width=50,height=100)
    canavas.pack(expand=True,fill="both",side="bottom")
    imgm0ve=canavas.create_image(0,150,image=Image)
    windows.config()
    
    #definition d un top bar
    part=tk.Frame(windows,bg="purple",width=2000,height=100)
    part.pack(side="top",fill="both")
    Text="certyPresent".upper()
    labframe=tk.Label(part,text= Text,fg="white",bg="purple",font=("Arial-black",26))
    labframe.pack(side="right")
    def animer():
      canavas.move(imgm0ve,5,0)
      x1,y1=canavas.coords(imgm0ve)
      if x1<650:
         windows.after(50,animer)
    animer()
    bottonImage=PhotoImage(file="men.png")
    boutton=tk.Button(part,image=bottonImage,
                      bg="purple",
                      height=30,
                      bd=0,
                      fg="purple",
                      command=lambda: test.menu(windows)
                      )
    boutton.place(x=-23)
    windows.mainloop()