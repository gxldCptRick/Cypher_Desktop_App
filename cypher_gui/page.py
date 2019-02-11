class Page(object):
    def __init__(self, root):
        super(Page, self).__init__()
        self.root = root

    def pack(self, **kwargs):
        self.root.pack()

    def forget(self, **kwargs):
        self.root.pack_forget()
