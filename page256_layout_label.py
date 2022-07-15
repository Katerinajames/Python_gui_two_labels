
import tkinter as tk
from tkinter import *
m=Tk()
m.title("Two windows")
Label(text="I am in the first window").pack() 

second=Toplevel()
Label(second ,text="I am in the second  window").pack() 
m.geometry('300x300')
m.mainloop()
