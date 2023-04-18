class controller:
    def __init__(self):
        pass

    def set(self, view, model):
        self.view = view
        self.model = model

    def click(self):
        value = self.model.click
        self.view.update_UI(value)

controller()