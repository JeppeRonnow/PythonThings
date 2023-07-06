import tkinter as tk

def save_inputs(event):
    for entry in entries:
        inputs.append(entry.get())
    print(inputs)  # Just for demonstration purposes

inputs = []
root = tk.Tk()

entries = []
for i in range(3):
    entry = tk.Entry(root)
    entry.bind("<Return>", save_inputs)
    entries.append(entry)

root.mainloop()