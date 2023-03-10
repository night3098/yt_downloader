import tkinter
import customtkinter
import pytube
import pretty_errors

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.geometry("400x200")
app.title("YT video downloader")

def start():
    url = entry.get()
    youtube = pytube.YouTube(url)
    video = youtube.streams.filter(progressive=True).desc().first()
    app.title("Downloading starting...")
    video.download()
    app.title("Download done")


label = customtkinter.CTkLabel(master=app, text="Simple YT video downloader", font=("Arial", 15))
label.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)

button = customtkinter.CTkButton(master=app, text="Download", command=start, border_width=2)
button.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)

entry = customtkinter.CTkEntry(master=app, placeholder_text="URL", width=300, height=30, border_width=2, corner_radius=10)
entry.pack(padx=20, pady=60)

app.mainloop()
