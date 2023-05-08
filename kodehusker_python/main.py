import tkinter
import customtkinter
import os
cwd = os.getcwd()



customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.geometry("1400x800")
app.title("kodehusker")
app.iconbitmap(cwd + '\kodehusker_python\img\lock-icon.ico')

kode = ""

def login_button():
    print("login pressed")
    print(entry.get())
    main_frame.pack(fill="both", expand=1)
    login_frame.forget()

def logud_button():
    print("logud pressed")
    main_frame.pack_forget()
    login_frame.pack(fill="both", expand=1)

login_frame = customtkinter.CTkFrame(app)


label = customtkinter.CTkLabel(login_frame, text="Kodehusker ALA Python", font=("Arial", 100), text_color=("black", "white"))
label.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)

#kodeord felt
frame = customtkinter.CTkFrame(login_frame, corner_radius=10)
frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER, relwidth=0.315, height=80)

#kodeord felt
entry = customtkinter.CTkEntry(login_frame, corner_radius=10, placeholder_text="Indtast Kodeord", textvariable=kode, show="*", font=("Arial", 20), text_color=("black", "white"), bg_color="#292929")
entry.place(relx=0.47, rely=0.5, anchor=tkinter.CENTER, relwidth=0.23, relheight=0.05)
entry.bind("<Return>", (lambda event: login_button()))

# Login knap
button = customtkinter.CTkButton(login_frame, text="Login", command=login_button, font=("Arial", 20), text_color=("black", "white"), bg_color="#292929")
button.place(relx=0.62, rely=0.5, anchor=tkinter.CENTER, relwidth=0.05, relheight=0.05)

login_frame.pack(fill="both", expand=1)


# main side
main_frame = customtkinter.CTkFrame(app)

label = customtkinter.CTkLabel(main_frame, text="Mine kodeord", font=("Arial", 50), text_color=("black", "white"))
label.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)
# Logud knap
button = customtkinter.CTkButton(main_frame, text="Logud", command=logud_button, font=("Arial", 20), text_color=("black", "white"), fg_color="red", hover_color="red4")
button.place(relx=0.95, rely=0.05, anchor=tkinter.CENTER, relwidth=0.05, relheight=0.05)

button = customtkinter.CTkButton(main_frame, text="Opret kodeord", font=("Arial", 20), text_color=("black", "white"))
button.place(relx=0.1, rely=0.1, anchor=tkinter.CENTER, relwidth=0.15, relheight=0.05)


    

app.mainloop()
