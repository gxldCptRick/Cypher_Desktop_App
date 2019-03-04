from tkinter import *


def generate_button_file_button(parent, label_text, file_callback, file_types=[]):
    frame = Frame(parent)
    frame.pack()
    string_var = StringVar()
    string_var.set("Nothing Selected...")

    def callback_variable():
        file_name = filedialog.askopenfilename(
            initialdir=".", filetypes=file_types)
        if(file_name != "" and file_name != None):
            string_var.set(file_name)
            file_callback(file_name)

    title = Label(frame, text=label_text)
    title.pack(side=TOP)
    btn = Button(frame, text="Select File", command=callback_variable)
    btn.pack(side=LEFT)
    label = Label(frame, textvariable=string_var)
    label.pack(side=LEFT)
    return frame


def generate_list_box(parent):
    return create_wrapped_component(parent, Listbox)


def create_wrapped_component(parent, component):
    frame = Frame(parent)
    scrollbar = Scrollbar(frame)
    instance = component(frame, yscrollcommand=scrollbar.set)
    instance.pack(side=LEFT)
    scrollbar.pack(side=RIGHT, fill=Y)
    scrollbar.config(command=instance.yview)
    return (frame, instance)
