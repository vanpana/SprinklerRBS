from src.Line import Line


class Repository:
    def __init__(self, filename):
        self.filename = filename
        self.data = {}
        self._load_from_file()

    def _load_from_file(self):
        with open(self.filename, "r") as file:
            for line in file:
                # Get the class and the number of lines
                cls, times = line.strip("\n").split(",")[0], int(line.strip("\n").split(",")[1])

                # Add an empty list of type cls to the dictionary
                self.data[cls] = []

                # Iterate through all the lines from the cls
                for _ in range(times):
                    # Get data as points and create a Line and add it to the list
                    self.data[cls].append(Line(*[int(x) for x in file.readline().strip("\n").split(",")]))
