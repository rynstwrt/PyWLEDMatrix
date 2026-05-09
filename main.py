from pywledmatrix import Matrix, Color


IP_ADDR = "10.10.77.6"
UDP_PORT = 21324


def main():
    # matrix = Matrix(5, 3)
    matrix = Matrix(32, 8)
    matrix.connect(IP_ADDR, UDP_PORT)


    # matrix.fill([255, 255, 0])
    matrix.fill(Color.PURPLE)

    # matrix.set_pixel(4, 1, [255, 0, 255])
    # matrix.set_pixel(0, 2, [255, 0, 0])

    # matrix.fill_row(2, [255, 255, 255])
    # matrix.fill_col(1, [255, 255, 255])
    # matrix.draw_rect(0, 0, 31, 7, [255, 255, 255], False)
    matrix.show()

    # matrix.print_pixels()

    # offset = False
    # while True:
    #     matrix.clear()
    #     matrix.draw_checkerboard([255, 255, 255], offset)
    #     matrix.show()
    #     offset = not offset
    #     sleep(0.1)


if __name__ == "__main__":
    main()
