import tkinter
import customtkinter

customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.geometry("1400x800")
app.title("kodehusker")
app.iconbitmap('C:\GitHub\PythonThings\kodehusker_python\lock-icon.ico')

kode = ""

def login_button():
    print("login pressed")
    print(kode)

label = customtkinter.CTkLabel(master=app, text="Kodehusker ALA Python", font=("Arial", 100), text_color=("black", "white"))
label.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)

#kodeord felt
frame = customtkinter.CTkFrame(master=app, corner_radius=10)
frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER, relwidth=0.3, height=50)

#kodeord felt
entry = customtkinter.CTkEntry(master=app, corner_radius=10, placeholder_text="Indtast Kodeord", textvariable=kode, show="*", font=("Arial", 20), text_color=("black", "white"))
entry.place(relx=0.47, rely=0.5, anchor=tkinter.CENTER, relwidth=0.23, relheight=0.05)

# Login knap
button = customtkinter.CTkButton(master=app, text="Login", command=login_button, font=("Arial", 20), text_color=("black", "white"))
button.place(relx=0.62, rely=0.5, anchor=tkinter.CENTER, relwidth=0.05, relheight=0.05)


app.mainloop()

