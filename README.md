# PyWLEDMatrix
A Python library for controlling WLED matrices!


## Example
```python
from pywledmatrix import Matrix

matrix = Matrix(5, 3)

matrix.connect("10.10.77.4", 21324)

matrix.fill([255, 255, 0])
matrix.fill_row(1, [255, 255, 255])

matrix.show()
```

## Drawing Methods
- `set_pixel(x, y, color)`
- `fill(color)`
- `fill_row(row, color)`
- `fill_col(col, color)`
- `draw_rect(x1, y1, x2, y2, color)`