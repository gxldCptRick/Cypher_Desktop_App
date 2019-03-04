from tkinter import *
from cypher_gui.page import Page
import cypher_gui.components as components
import cypher_app


class RSAPage(Page):
    def __init__(self, parent, width=600, height=300):
        frame = Frame(parent, width=width, height=height)
        super(RSAPage, self).__init__(frame)
        self.last_active = None
        self.rsa_key_frame = Frame(parent)
        self.initialize_rsa_frame()
        self.rsa_key_generator()

    def initialize_rsa_frame(self):
        public_key_frame = components.generate_button_file_button(
            self.rsa_key_frame, "Public Key", self.update_something_with_key_file_name, [("Key Files", "*.txt *.rsa")])
        message_file_frame = components.generate_button_file_button(
            self.rsa_key_frame, "Message File", self.update_list_box_with_content, [("Word Docx And Text Files", "*.docx *.txt")])
        public_key_frame.pack(side=TOP)
        message_file_frame.pack(side=TOP)
        (list_box_frame, list_box) = components.generate_list_box(self.rsa_key_frame)
        self.list_box = list_box
        self.list_box.bind("<<ListboxSelect>>", self.update_showcase_text)
        self.text = "No Message Selected..."
        (label_frame, label) = components.create_wrapped_component(
            self.rsa_key_frame, Text)
        label.insert(END, self.text)
        label.config(state=DISABLED)
        self.label = label

        list_box_frame.pack()
        label_frame.pack()
        self.submit_button = Button(
            self.rsa_key_frame, text="Encrypt Message", command=self.save_mesage_to_file)
        self.submit_button.pack()

    def save_mesage_to_file(self):
        save = filedialog.asksaveasfilename(
            initialdir=".", filetypes=[("text file", "*.txt")])
        if(not save.endswith('.txt')):
            save += ".txt"
        with open(save, 'w') as file:
            inputed_text = self.text
            out_text = cypher_app.cyphers.rsa.encrypt(
                self.key_file, inputed_text)
            file.write(out_text)

    def update_showcase_text(self, evt):
        selected = self.list_box.get(self.list_box.curselection())
        self.text = selected
        self.label.config(state=NORMAL)
        self.label.delete('1.0', END)
        self.label.insert(END, self.text)
        self.label.config(state=DISABLED)

    def update_something_with_key_file_name(self, file_name):
        self.key_file = file_name

    def update_list_box_with_content(self, file_name):
        self.list_box.delete('0', END)
        oscars = cypher_app.command_line.tools.read_in_file(file_name)
        for oscar in oscars:
            self.list_box.insert(END, oscar)

    def navigate_frame(self, frame):
        if(self.last_active):
            self.last_active.pack_forget()
        self.last_active = frame
        self.last_active.pack()

    def rsa_key_generator(self):
        self.navigate_frame(self.rsa_key_frame)
