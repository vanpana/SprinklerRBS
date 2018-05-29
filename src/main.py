from src.Controller import Controller
from src.Repository import Repository
from src.View import View

temperature_filename = "../data/temperature.dat"
humidity_filename = "../data/humidity.dat"
time_filename = "../data/time.dat"
table_filename = "../data/table.dat"

if __name__ == '__main__':
    temperature_repository = Repository(temperature_filename)

    controller = Controller(Repository(temperature_filename), Repository(humidity_filename), Repository(time_filename),
                            table_filename)

    view = View(controller)

    view.run()
