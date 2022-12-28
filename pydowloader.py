import tkinter
import tkinter.filedialog
from pytube import YouTube

def Download(link,sciezka):
  youtubeObject = YouTube(link)
  youtubeObject = youtubeObject.streams.get_highest_resolution()
  try:
    youtubeObject.download(sciezka)
  except:
    print("Error")
  print("Pobrano film Yay")

def choose_file():
  global filepath
  filepath = tkinter.filedialog.askdirectory()
  print(f"Wybrano katalog: {filepath}")

def get_value():
  global link
  link=input_field.get()
  Download(link,filepath)

root = tkinter.Tk()
root.wm_title("PyDownloader") #tytuł okna programu
#root.geometry("750x250")
root.config(bg="#1C2333") #0E1525


label = tkinter.Label(root, text="Witaj w programie służącym do pobierania filmów z YouTube", font=("Arial", 16), bg="#1C2333", fg="white")
label.pack()

string = tkinter.StringVar()
string.set("Podaj folder, do którego zapiszesz pobrany film:")

label = tkinter.Label(root, textvariable=string, bg="#1C2333", fg="white")
label.pack()

button = tkinter.Button(root, text="Wybierz folder", command=choose_file, bg="#1C2333", fg="white")
button.pack()

label = tkinter.Label(root, text="Podaj link do filmu na YouTube:", bg="#1C2333", fg="white")
label.pack()

input_field = tkinter.Entry(root, text="Domyślny tekst", width="80")
input_field.pack()

button1 = tkinter.Button(root, text="Pobierz film!", background='#ff0000', command=get_value) #przycisk kopńcowy
button1.pack()

root.mainloop()