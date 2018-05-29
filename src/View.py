class View:
    def __init__(self, controller):
        self.controller = controller

    def run(self):
        while True:
            print(self.controller.run())
