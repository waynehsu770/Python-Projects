

import tkinter as tk
from tkinter import *
import webbrowser



class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master.title("Web Page Generator")
        self.btn = Button(self.master, text="Default HTML Page", width=30, height=2, command=self.defaultHTML)
        self.btn.grid(row=2, column=2, padx=(10,10), pady=(10,10))
        self.btn = Button(self.master, text="Submit Custom Text", width=30, height=2, command=self.entryHTML)
        self.btn.grid(row=2, column=3, padx=(10,10), pady=(10,10))
        self.lbl_entry = tk.Label(self.master, text='Enter custom text or click the Default HTML page button')
        self.lbl_entry.grid(row=0, column=0, padx=(27,0), pady=(10,0), sticky=N+W)
        self.text_entry = tk.Entry(self.master, text='Enter Here')
        self.text_entry.grid(row=1, column=0, rowspan=1, columnspan=4, padx=(30,40), pady=(0,0), sticky=N+E+W)


    def defaultHTML(self):
        htmlText = "Stay tuned for our amazing summer sale!"
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText +  "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")

    def entryHTML(self):
        entryText = self.text_entry.get()
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + entryText +  "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")

    


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
