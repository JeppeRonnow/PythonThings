from ctypes import resize
import tkinter as tk
from tkinter import Text,ttk
import os
from tkinter import *

root = tk.Tk()

root.geometry("810x400")
root.title('Agent instalock')
root.resizable(0, 0)

bg = PhotoImage(file = "billed.png")

pic = Label( root, image = bg)
pic.place(x = 0, y = 100)


def tabel():
   boxH = 40
   boxW = 40

   root.columnconfigure(0, weight=9)
   root.columnconfigure(1, weight=9)

   nr1 = ttk.Label(root, text="1")
   nr1.grid(column=0, row=0, sticky=tk.W, padx=boxW, pady=boxH)

   nr2 = ttk.Label(root, text="2")
   nr2.grid(column=1, row=0, sticky=tk.W, padx=boxW, pady=boxH)
   
   nr3 = ttk.Label(root, text="3")
   nr3.grid(column=2, row=0, sticky=tk.W, padx=boxW, pady=boxH)
   
   nr4 = ttk.Label(root, text="4")
   nr4.grid(column=3, row=0, sticky=tk.W, padx=boxW, pady=boxH)
    
   nr5 = ttk.Label(root, text="5")
   nr5.grid(column=4, row=0, sticky=tk.W, padx=boxW, pady=boxH)
    
   nr6 = ttk.Label(root, text="6")
   nr6.grid(column=5, row=0, sticky=tk.W, padx=boxW, pady=boxH)
    
   nr7 = ttk.Label(root, text="7")
   nr7.grid(column=6, row=0, sticky=tk.W, padx=boxW, pady=boxH)
   
   nr8 = ttk.Label(root, text="8")
   nr8.grid(column=7, row=0, sticky=tk.W, padx=boxW, pady=boxH)

   nr9 = ttk.Label(root, text="9")
   nr9.grid(column=8, row=0, sticky=tk.W, padx=boxW, pady=boxH)

   nr10 = ttk.Label(root, text="1")
   nr10.grid(column=0, row=1, sticky=tk.W, padx=boxW, pady=boxH)

   nr11 = ttk.Label(root, text="2")
   nr11.grid(column=1, row=1, sticky=tk.W, padx=boxW, pady=boxH)
   
   nr12 = ttk.Label(root, text="3")
   nr12.grid(column=2, row=1, sticky=tk.W, padx=boxW, pady=boxH)
   
   nr13 = ttk.Label(root, text="4")
   nr13.grid(column=3, row=1, sticky=tk.W, padx=boxW, pady=boxH)
    
   nr14 = ttk.Label(root, text="5")
   nr14.grid(column=4, row=1, sticky=tk.W, padx=boxW, pady=boxH)
    
   nr15 = ttk.Label(root, text="6")
   nr15.grid(column=5, row=1, sticky=tk.W, padx=boxW, pady=boxH)
    
   nr16 = ttk.Label(root, text="7")
   nr16.grid(column=6, row=1, sticky=tk.W, padx=boxW, pady=boxH)
   
   nr17 = ttk.Label(root, text="8")
   nr17.grid(column=7, row=1, sticky=tk.W, padx=boxW, pady=boxH)

   nr18 = ttk.Label(root, text="9")
   nr18.grid(column=8, row=1, sticky=tk.W, padx=boxW, pady=boxH)

def tabelFor():   
   boxH = 37
   boxW = 37

   for r in range(3):
      for c in range(9):
         num = ""
         if r == 0:
            num = num
         elif r == 1:
            num = c+1
         elif r == 2:
            num = c+10

         tabelLabel = ttk.Label(root, text=num)
         tabelLabel.grid(column=c, row=r, sticky=tk.W, padx=boxW, pady=boxH)

tabelFor()

if __name__ == "__main__":
   root.mainloop()

