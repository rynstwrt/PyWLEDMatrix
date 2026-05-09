import asyncio
from pywledmatrix import Matrix, Color
from time import sleep


DELAY = 0.02
COLOR = Color.CYAN


async def scan_x():
    for x in range(matrix.width):
        matrix.clear()
        matrix.fill_col(x, COLOR)
        matrix.show()
        await asyncio.sleep(DELAY)

    for x in range(matrix.width - 1, 0, -1):
        matrix.clear()
        matrix.fill_col(x, COLOR)
        matrix.show()
        await asyncio.sleep(DELAY)


async def scan_y():
    for y in range(matrix.height):
        matrix.clear()
        matrix.fill_row(y, COLOR)
        matrix.show()
        await asyncio.sleep(DELAY)

    for y in range(matrix.height - 1, 0, -1):
        matrix.clear()
        matrix.fill_row(y, COLOR)
        matrix.show()
        await asyncio.sleep(DELAY)


async def main():
    while True:
        await scan_x()
        await scan_y()


if __name__ == "__main__":
    matrix = Matrix(32, 8)
    matrix.connect("10.10.77.6")

    asyncio.run(main())
