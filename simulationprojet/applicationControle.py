import serial
import tkinter as tk
import time
def electro():
   value= Entre.get()
   if value.strip()=='john':
        ser.write(b'1')
   else:
       ser.write(b'0')
       
   ser.close()
       
ser=serial.Serial('/dev/ttyUSB0',9600)
Fusion=tk.Tk()
Fusion.config(bg='black')
fram=tk.Frame(Fusion,width=2000,height=50,bg='red')
fram.pack()
ld=tk.Label(Fusion,text="Bienvenu dans l'application test de john fusionner avec de l'electronique",bg='black',fg='white',font=("Arial-black",12,"bold"))
ld.pack(pady=120,padx=123,anchor="w")

ld=tk.Label(Fusion,text="tkinter est limite en terme de devellopement d'application5",bg='black',fg='white',font=("Arial-black",11))
ld.pack(anchor="w",padx=123)
frame2=tk.Frame(Fusion,width=1100,height=100,bg='white')
frame2.pack()
frame2.pack_propagate(False)
Text=tk.Label(frame2,text="Entrer le contenant qui doit etre entre")
Text.pack(anchor="w")
Entre=tk.Entry(frame2,width=123)
Entre.pack(padx=5,side="left")
boutton1=tk.Button(frame2,text="envoyer le texte",bg='red',command=electro)
boutton1.pack(padx=5, side="left")
Fusion.mainloop()
