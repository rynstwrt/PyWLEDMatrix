import socket
import numpy as np


class Matrix:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.ip = None
        self.port = None
        self.client = None

        self.pixels = np.zeros(shape=(self.height, self.width, 3), dtype=int)


    def connect(self, ip, port):
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


    def set_pixel(self, x, y, color):
        self.pixels[y, x] = color


    def fill(self, color):
        self.pixels = np.full(shape=(self.height, self.width, 3), fill_value=color)


    def fill_row(self, row, color):
        self.pixels[row, :] = color


    def fill_col(self, col, color):
        self.pixels[:, col] = color


    def draw_rect(self, x: int, y: int, w: int, h: int, color: list):
        x2 = x + w - 1
        y2 = y + h - 1
        print(x, y, x2, y2)

        self.pixels[x, y] = color
        self.pixels[x2, y2] = color

        for row in self.pixels:
            print(row)