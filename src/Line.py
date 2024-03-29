import math

import numpy


class Line:
    def __init__(self, start_x, end_x, start_y, end_y):
        self.start_x = start_x
        self.start_y = start_y
        self.end_x = end_x
        self.end_y = end_y

    def y_of_a_point(self, x):
        if x > self.end_x or x < self.start_x:
            return None

        if self.start_y == self.end_y:
            return self.start_y

        if self.start_y < self.end_y:
            return (x - self.start_x) / (self.end_x - self.start_x)
        else:
            return 1 - (x - self.start_x) / (self.end_x - self.start_x)

    def x_of_a_point(self, y):
        return y * (self.end_x - self.start_x) + self.start_x

        if self.start_y < self.end_y:
            return y * (self.end_x - self.start_x) + self.start_x
        else:
            return 1 - y * (self.end_x - self.start_x) + self.start_x
