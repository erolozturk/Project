import numpy as np
import cv2
import Tkinter as tk
import Image
from ImageTk import PhotoImage
import time

window = tk.Tk()  
window.wm_title("Erol Mehmet EDTL Odev")
window.config(background="#FFFFFF")


imageFrame = tk.Frame(window, width=640, height=480)
imageFrame.grid(row=0, column=0, padx=10, pady=2)

a=0
b=0	
c=0

name="resim"
tur=".png"
def buttoncommand():
	global a
	a+=1

def buttoncommand2():
	global b
	global out
	b+=1


lmain = tk.Label(imageFrame)
lmain.grid(row=0, column=0)
cap = cv2.VideoCapture(0)

def show_frame(): 
	global frame2	
	global c
	global b
	ret, frame = cap.read()
	yedekframe=frame		
	if a%2==0:
		frame2 = cv2.flip(frame,1)
	if b > c:
		fname=name+str(b)+tur
		cv2.imwrite(fname,frame2)
		c=b
	cv2image = cv2.cvtColor(frame2, cv2.COLOR_BGR2RGB)	
	img = Image.fromarray(cv2image)
	imgtk = PhotoImage(image=img)
	lmain.imgtk = imgtk
	lmain.configure(image=imgtk)
	lmain.after(10, show_frame)  		

buttonFrame = tk.Frame(window)
buttonFrame.grid(row=200, column=0, padx=10, pady=2)
button1=tk.Button(buttonFrame,text="Start-Stop",fg="red",command=buttoncommand)
button1.pack()
button2=tk.Button(buttonFrame,text="Resim kaydet",fg="green",command=buttoncommand2)
button2.pack()
		

show_frame()  
window.mainloop()  
