from arrays import Array2D
class GrayscaleImage:
    def __init__(self,  nrows, ncols):
        self._elements = Array2D(nrows, ncols)
        self.clear(0)

    def __getitem__(self, i, j):
        return self._elements[(i, j)]

    def __setitem__(self, t, value):
        self._elements[(t[0], t[1])] = value

    def clear(self, value):
        self._elements.clear(value)

    def width(self):
        return self._elements.num_cols()

    def height(self):
        return self._elements.num_rows()

    def __str__(self):
        s = ""
        for i in range(self.height()):
            for j in range(self.width()):
                s += str(self._elements[(i, j)]) + " "
            s += "\n"
        return s[:-1]

"""
photo = GrayscaleImage(5, 5)
photo[(2, 2)] = 3
print(str(photo))
photo.clear(18)
print(str(photo))
"""