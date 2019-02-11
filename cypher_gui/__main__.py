from tkinter import Tk
from tkinter import *
from tkinter import filedialog


# root = Tk()

# # root = Tk()
# # root.title("Tk dropdown example")

# # # Add a grid
# # mainframe = Frame(root)
# # mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
# # mainframe.columnconfigure(0, weight=1)
# # mainframe.rowconfigure(0, weight=1)
# # mainframe.pack(pady=100, padx=100)

# # # Create a Tkinter variable
# # tkvar = StringVar(root)

# # # Dictionary with options
# # choices = {'Pizza', 'Lasagne', 'Fries', 'Fish', 'Potatoe'}
# # tkvar.set('Pizza')  # set the default option

# # # popupMenu = OptionMenu(mainframe, tkvar, *choices)
# # Label(mainframe, text="Choose a dish").grid(row=1, column=1)
# # popupMenu.grid(row=2, column=1)

# # # on change dropdown value


# # def change_dropdown(*args):
# #     print(tkvar.get())


# # # link function to change dropdown
# # tkvar.trace('w', change_dropdown)

# # root.mainloop()


import cypher_app
from cypher_gui.main_page import MainPage
from cypher_gui.rsa_page import RSAPage
app = Tk()


class App(object):
    def __init__(self, root):
        super(App, self).__init__()
        self.frame = Frame(root, width=600, height=300,
                           background="#c001af")
        self.frame.pack()
        self.main_frame = MainPage(self.frame, width=600, height=300)
        self.rsa_frame = RSAPage(self.frame, width=600, height=300)  


App(app)
#filedialog.askopenfilename(initialdir='/', )
# tk example scollbarview
# scrollbar = Scrollbar(app)
# scrollbar.pack(side=RIGHT, fill=Y)
# listbox = Text(app, yscrollcommand=scrollbar.set)
# scrollbar.config(command=listbox.yview)
# listbox.pack()
app.mainloop()
