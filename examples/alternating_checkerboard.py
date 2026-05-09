from pywledmatrix import Color, Matrix
from time import sleep


if __name__ == "__main__":
    matrix = Matrix(32, 8)
    matrix.connect("10.10.77.6")

    offset = False
    while True:
        matrix.clear()
        matrix.draw_checkerboard(Color.ORANGE, offset)
        matrix.show()

        offset = not offset

        sleep(0.1)