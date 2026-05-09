from pywledmatrix import Matrix


IP_ADDR = "10.10.77.4"
UDP_PORT = 21324


matrix = Matrix(5, 3)

# matrix.fill([255, 255, 0])
# matrix.set_pixel(4, 1, [255, 0, 255])
# matrix.set_pixel(0, 2, [255, 0, 0])

matrix.fill_row(1, [255, 255, 255])
# matrix.fill_col(1, [255, 255, 255])
# matrix.draw_rect(0, 0, 2, 2, [255, 255, 255])

matrix.print_pixels()

