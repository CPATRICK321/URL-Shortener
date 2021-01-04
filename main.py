import pyshorteners
from tkinter import *

root = Tk()
root.geometry("300x120")
root.title("URL Shortener")
urlInp = StringVar()
urlOut = StringVar()


def urlshortener():
    urlOut.set(pyshorteners.Shortener().tinyurl.short(urlInp.get()))


Label(root, text="Enter URL").pack()
Entry(root, textvariable=urlInp).pack()
Button(root, text="Submit", command=urlshortener).pack()
Entry(root, textvariable=urlOut).pack()

root.mainloop()
