from tkinter import *
import tkinter.messagebox
root = Tk() 
menu = Menu(root) 
frame = Frame(root) 
frame.pack() 
root.config(menu=menu) 
filemenu = Menu(menu) 
def red():
   tkinter.messagebox.showinfo("Red Button is Clicked...","RED")
def brown():
   tkinter.messagebox.showinfo("Brown Button is Clicked...","BROWN")
def blue():
   tkinter.messagebox.showinfo("Blue Button is Clicked...","BLUE")
def black():
   tkinter.messagebox.showinfo("Black Button is Clicked...","BLACK")

menu.add_cascade(label='File', menu=filemenu) 
filemenu.add_command(label='New') 
filemenu.add_command(label='Open...') 
filemenu.add_separator() 
filemenu.add_command(label='Exit', command=root.quit) 
helpmenu = Menu(menu) 
menu.add_cascade(label='Help', menu=helpmenu) 
helpmenu.add_command(label='About') 
bottomframe = Frame(root) 
bottomframe.pack( side = BOTTOM ) 
redbutton = Button(frame, text = 'Red', fg ='red',command=red) 
redbutton.pack( side = LEFT) 
greenbutton = Button(frame, text = 'Brown', fg='brown',command=brown) 
greenbutton.pack( side = LEFT ) 
bluebutton = Button(frame, text ='Blue', fg ='blue',command=blue) 
bluebutton.pack( side = LEFT ) 
blackbutton = Button(bottomframe, text ='Black', fg ='black',command=black) 
blackbutton.pack( side = BOTTOM) 
mainloop() 


