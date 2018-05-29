class View:
    def __init__(self, controller):
        self.controller = controller

    def run(self):
        print(self.controller.run())
