import tkinter as tk

class view_GUI:
    def __init__(self, controller):
        self.root = tk.Tk()
        self.controller = controller

        self.btn = tk.Button(self.root, text='0', command=self.controller.click)

        self.btn.pack()

    def update_UI(self, value):
        self.btn['text'] = str(value())

    def run(self):
        self.root.mainloop()