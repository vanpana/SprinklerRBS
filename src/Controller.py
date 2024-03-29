def _get_table(table_filename):
    with open(table_filename, "r") as file:
        return [[value for value in line.strip("\n").split(" ")] for line in file]


def get_cls_from_x(repo, x):
    classes = []
    for cls in repo.data:
        for line in repo.data[cls]:
            intersection = line.y_of_a_point(x)
            if intersection is not None and cls not in [c[0] for c in classes]:
                classes.append((cls, intersection))

    return classes


def get_cls_pos_from_name(cls_group, cls_name):
    if cls_group == "temperature":
        if cls_name == "very_cold":
            return 0

        if cls_name == "cold":
            return 1

        if cls_name == "normal":
            return 2

        if cls_name == "warm":
            return 3

        if cls_name == "hot":
            return 4

    elif cls_group == "humidity":
        if cls_name == "wet":
            return 0

        if cls_name == "normal":
            return 1

        if cls_name == "dry":
            return 2


class Controller:
    def __init__(self, temperature_repository, humidity_repository, time_repository, table_filename):
        self.temperature_repository = temperature_repository
        self.humidity_repository = humidity_repository
        self.time_repository = time_repository
        self.table = _get_table(table_filename)
        self.filled_table = [[0 for _ in range(len(self.temperature_repository.data))]
                             for _ in range(len(self.humidity_repository.data))]

    def run(self):
        # Read temperature from user
        temperature_value = int(input("Temperature: "))

        # Read humidity from user
        humidity_value = int(input("Humidity: "))

        # Get temperature classes
        temperature_classes = get_cls_from_x(self.temperature_repository, temperature_value)

        # Get humidity classes
        humidity_classes = get_cls_from_x(self.humidity_repository, humidity_value)

        # Fill the table
        self.fill_table(temperature_classes, humidity_classes)

        # Get short, medium, long
        s, m, l = self.get_max_values()

        # Get the time
        return self.get_time(s, m, l)

    def fill_table(self, temperature_classes, humidity_classes):
        for h_cls in humidity_classes:
            h_pos = get_cls_pos_from_name("humidity", h_cls[0])
            for t_cls in temperature_classes:
                t_pos = get_cls_pos_from_name("temperature", t_cls[0])
                self.filled_table[h_pos][t_pos] = min(t_cls[1], h_cls[1])

    def get_max_values(self):
        short = []
        medium = []
        long = []

        for i in range(len(self.table)):
            for j in range(len(self.table[0])):
                if self.table[i][j] == "s":
                    short.append(self.filled_table[i][j])
                elif self.table[i][j] == "m":
                    medium.append(self.filled_table[i][j])
                else:
                    long.append(self.filled_table[i][j])

        return max(short), max(medium), max(long)

    def get_time(self, s, m, l):
        small = []
        medium = []
        long = []

        for cls in self.time_repository.data:
            for line in self.time_repository.data[cls]:
                if cls == "short" and s > 0:
                    intersection = line.x_of_a_point(s)
                    small.append((intersection, s))
                elif cls == "medium" and m > 0:
                    intersection = line.x_of_a_point(m)
                    medium.append((intersection, m))
                elif cls == "long" and l > 0:
                    intersection = line.x_of_a_point(l)
                    long.append((intersection, l))

        small_sum = 0
        medium_sum = 0
        long_sum = 0

        if len(small) > 0:
            small_sum = sum([s[0] * s[1] for s in small]) / sum([s[1] for s in small])

        if len(medium) > 0:
            medium_sum = sum([m[0] * m[1] for m in medium]) / sum([m[1] for m in medium])

        if len(long) > 0:
            long_sum = sum([l[0] * l[1] for l in long]) / sum([l[1] for l in long])

        return small_sum + medium_sum + long_sum
