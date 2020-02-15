# Create a Monte Carlo simulation to calculate PI
import math
import sys


def main(args):
    # throwing sand on a 1 X 1 square. A quarter of circle with radius as 1
    # will sit inside the square.

    radius = int(args[0])
    inside_circle = 0
    for x in range(radius):
        print("Completing {0:.2f}%".format(x / float(radius) * 100))
        for y in range(radius):
            d = math.sqrt(x*x + y*y)
            #print(x, y, d)
            if d < radius:
                inside_circle = inside_circle + 1

    print("Total: {} / {} = {}".format(inside_circle, radius*radius, float(inside_circle) / (radius*radius)))
    print("PI = ", 4 * float(inside_circle) / (radius*radius))
    pass


if __name__ == '__main__':
    main(sys.argv[1:])


