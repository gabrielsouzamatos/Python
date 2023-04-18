class view:
    def __init__(self, controller):
        self.controller = controller

    def run(self):
        while True:
            input()
            self.controller.click()

    def update_UI(self, value):
        print(value())