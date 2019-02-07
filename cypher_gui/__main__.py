from tkinter import Tk
from tkinter import *
from tkinter import filedialog
app = Tk()


class App(object):
    def __init__(self, root):
        super(App, self).__init__()
        self.root = root
        frame = Frame(root)
        frame.pack()
        scrollbar_decypher_text = Scrollbar(frame)
        self.text = Text(frame, yscrollcommand=scrollbar_decypher_text.set)
        scrollbar_decypher_text.config(command=self.text.yview)
        self.text.pack(side=LEFT)
        scrollbar_decypher_text.pack(side=LEFT, fill=Y)
        text = StringVar()
        text.set("Git Gud")
        button = Button(frame, textvariable=text,
                        command=lambda: frame.pack_forget())
        self.file_thign()
        button.pack(side=LEFT)

    def file_thign(self):
        datto = None
        with filedialog.askopenfile('r', initialdir='.', filetypes=(("text files or documents", "*.txt *.docx"), ("all files", "*.*"))) as file:
            print(file.name.endswith(".docx"))
        print(datto)


App(app)
# filedialog.askopenfile()
#filedialog.askopenfilename(initialdir='/', )
# tk example scollbarview
# scrollbar = Scrollbar(app)
# scrollbar.pack(side=RIGHT, fill=Y)
# listbox = Text(app, yscrollcommand=scrollbar.set)
# scrollbar.config(command=listbox.yview)
# listbox.pack()
app.mainloop()
