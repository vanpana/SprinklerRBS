class Line:
    def __init__(self, start_x, start_y, end_x, end_y):
        self.start_x = start_x
        self.start_y = start_y
        self.end_x = end_x
        self.end_y = end_y

    def y_of_a_point(self, x):
        intersection = self.function(x)
        if intersection < 0 or intersection > 1:
            return None
        return intersection

    def x_of_a_point(self, y):
        intersection = self.reverse(y)
        if intersection < 0:
            return None
        return intersection

    def slope(self):
        return (self.end_y - self.start_y) / (self.end_x - self.start_x)

    def function(self, x):
        return self.slope() * x + self.end_y

    def reverse(self, y):
        return (y - self.start_y) / self.slope()
