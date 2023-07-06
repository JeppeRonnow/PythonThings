import tkinter
import customtkinter
import os
cwd = os.getcwd()



customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.geometry("1400x800")
app.title("kodehusker")

kode = ""

info = []

obj_list = []


def login_button():
    print("login pressed")
    kode = entry.get()
    print(kode)
    main_frame.pack(fill="both", expand=1)
    login_frame.forget()

def logud_button():
    print("logud pressed")
    main_frame.pack_forget()
    login_frame.pack(fill="both", expand=1)

def create_button():
    print("create pressed")
    main_frame.pack_forget()
    login_frame.pack_forget()
    create_pass.pack(fill="both", expand=1)

def main_page():
    login_frame.pack_forget()
    create_pass.pack_forget()
    main_frame.pack(fill="both", expand=1)

def add_pass(event):
    main_page()
    for entry1 in entries:
        info.append(entry1.get())
    
    obj_list.append(passObj(info[0],info[1],info[2]))
    info.clear()

    for entry1 in entries:
        entry1.delete(0, customtkinter.END)

    for i in range(len(obj_list)):
        print(obj_list[i])
    
    
    


class passObj:
    def __init__(self, place, user, password):
        self.place = place
        self.user = user
        self.password = password

    def __str__(self):
        return f"passObj: {self.place}, {self.user}, {self.password}"



#login
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
# Opret knap
button = customtkinter.CTkButton(main_frame, text="Opret kodeord", command=create_button, font=("Arial", 20), text_color=("black", "white"))
button.place(relx=0.1, rely=0.1, anchor=tkinter.CENTER, relwidth=0.15, relheight=0.05)

for i in range(4):
    label = customtkinter.CTkLabel(main_frame, text="Kode     Pass     place", font=("Arial", 25), text_color=("black", "white"))
    label.place(relx=0.5, rely=0.25 + (i*0.1), anchor=tkinter.CENTER)



#opret side
create_pass = customtkinter.CTkFrame(app)

create_titels = ["sted", "bruger", "kodeord"]

entries = []
for i in range(3):
    entry1 = customtkinter.CTkEntry(create_pass, corner_radius=10, placeholder_text="Indtast " + create_titels[i], font=("Arial", 20), text_color=("black", "white"), bg_color="#292929")
    entry1.place(relx=0.5, rely=0.3  + (i*0.1), anchor=tkinter.CENTER, relwidth=0.23, relheight=0.05)
    entry1.bind("<Return>", add_pass)
    entries.append(entry1)

button = customtkinter.CTkButton(create_pass, text="Gå tilbage", command=main_page, font=("Arial", 20), text_color=("black", "white"))
button.place(relx=0.1, rely=0.1, anchor=tkinter.CENTER, relwidth=0.15, relheight=0.05)


app.mainloop()

