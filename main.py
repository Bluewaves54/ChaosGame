import matplotlib.pyplot as plt
import random as rd
import math


class Line:
    def __init__(self, slope, coord):
        self.slope = slope
        self.y_intercept = slope*(-1*coord[0])+coord[1]

    def f(self, x):
        return x*self.slope + self.y_intercept


def get_polygon_coords(l, n):
    x = [l/2]
    y = [0]
    a = math.radians(360/n)

    for count in range(n):
        x.append(l*math.cos((count+1) * a) + x[-1])
        y.append(l*math.sin((count+1) * a) + y[-1])

    return x, y

def get_slope(coord1, coord2):
    x1, y1 = coord1
    x2, y2 = coord2

    return (y2 - y1) / (x2 - x1)

def get_next_coord(coord1, coord2):
    slope = get_slope(coord1, coord2)

    next_x = coord1[0] + ((coord2[0] - coord1[0]) * 1/2)
    next_y = Line(slope, coord1).f(next_x)

    return next_x, next_y


def main():
    # sides = int(input("Enter number of sides: "))
    # iters = int(input("Enter number of iterations: "))
    #
    sides = 3
    iters = 1000000

    final_x, final_y = list(), list()
    xs, ys = get_polygon_coords(10, sides)
    final_x += xs
    final_y += ys

    start_coord = (final_x[0], final_y[0])
    for i in range(iters):
        num = rd.randint(1, sides)
        vertex = (xs[num], ys[num])
        try:
            new_coord = get_next_coord(start_coord, vertex)
            final_x.append(new_coord[0])
            final_y.append(new_coord[1])
            start_coord = new_coord
        except ZeroDivisionError:
            continue

    plt.figure(figsize=(5, 5))
    plt.plot(final_x, final_y, 'r.', markersize=0.01)
    plt.show()


if __name__ == "__main__":
    main()
