from cypher_gui.page import Page
from tkinter import *


class MainPage(Page):
    def __init__(self, parent, width=600, height=300):
        frame = Frame(parent, width=width, height=height)
        super(MainPage, self).__init__(frame)
