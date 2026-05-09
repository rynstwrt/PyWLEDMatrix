import socket
import numpy as np


class Color:
    BLACK = [0, 0, 0]
    RED = [255, 0, 0]
    ORANGE = [255, 96, 0]
    YELLOW = [255, 255, 0]
    GREEN = [0, 255, 0]
    BLUE = [0, 0, 255]
    CYAN = [15, 223, 255]
    PURPLE = [255, 0, 255]


class Matrix:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

        self.ip = None
        self.port = None
        self.client = None

        self.pixels = np.zeros(shape=(self.height, self.width, 3), dtype=int)


    def connect(self, ip: str, port: int = 21324):
        self.ip = ip
        self.port = port
        self.client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


    def show(self):
        message = [2, 2, *self.pixels.ravel().tolist()]
        self.client.sendto(bytearray(message), (self.ip, self.port))


    def print_pixels(self):
        for row in self.pixels:
            for col in row:
                print(col, end=" ")
            print()


    def clear(self):
        self.fill([0, 0, 0])


    def set_pixel(self, x: int, y: int, color: list):
        self.pixels[y, x] = color


    def fill(self, color: list | Color):
        self.pixels = np.full(shape=(self.height, self.width, 3), fill_value=color)


    def fill_row(self, row: int, color: list):
        self.pixels[row, :] = color


    def fill_col(self, col: int, color: list):
        self.pixels[:, col] = color


    def draw_rect(self, x1: int, y1: int, x2: int, y2: int, color: list, solid: bool = False):
        for y in range(y1, y2 + 1):
            for x in range(x1, x2 + 1):
                if solid:
                    self.pixels[y, x] = color
                else:
                    if y == y1 or y == y2 or x == x1 or x == x2:
                        self.pixels[y, x] = color


    def draw_checkerboard(self, color: list | Color, offset: bool = False):
        for y in range(self.height):
            for x in range(self.width):
                if (x + 1 if offset else x) % 2 == y % 2:
                    self.pixels[y, x] = color
