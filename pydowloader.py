import tkinter
import tkinter.filedialog
from pytube import YouTube

def Download(link,path):
  global output
  youtubeObject = YouTube(link)
  youtubeObject = youtubeObject.streams.get_highest_resolution()
  try:
    youtubeObject.download(path)
  except:
    labelError = tkinter.Label(root, text="Error", bg="#1C2333", fg="white")
    labelError.pack()
    print("Error")
  labelSuccess = tkinter.Label(root, text="Successfully downloaded!", bg="#1C2333", fg="white")
  labelSuccess.pack()
  print("Successfully downloaded!")

def choose_file():
  global filepath
  filepath = tkinter.filedialog.askdirectory()
  print(f"Selected directory: {filepath}")

def get_value():
  global link
  link=input_field.get()
  Download(link,filepath)

root = tkinter.Tk()
root.geometry('600x200')
root.wm_title("PyDownloader")
root.config(bg="#1C2333")


label = tkinter.Label(root, text="pyDownloader", font=("Arial", 20), bg="#1C2333", fg="white", pady=20)
label.pack()

label = tkinter.Label(root, text="Paste YouTube video url:", bg="#1C2333", fg="white")
label.pack()

buttonFrame = tkinter.Frame(root)
buttonFrame.rowconfigure(0,weight=2)
buttonFrame.rowconfigure(1,weight=1)
buttonFrame.columnconfigure(0,weight=1)
buttonFrame.columnconfigure(1,weight=1)

input_field = tkinter.Entry(buttonFrame, width="80")
input_field.grid(row=0,columnspan=2,sticky=tkinter.W+tkinter.E)

btn0 = tkinter.Button(buttonFrame, text="Choose save path", command=choose_file, bg="#3e3e3e", fg="white")
btn0.grid(row=1,column=0,sticky=tkinter.W+tkinter.E)

btn1 = tkinter.Button(buttonFrame, text="Download!", background='#ff0000', command=get_value)
btn1.grid(row=1,column=1,sticky=tkinter.W+tkinter.E)

buttonFrame.pack()

root.mainloop()