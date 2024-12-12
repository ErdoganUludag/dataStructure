class matrix:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.data = [[0 for colm in range(columns)] for row in range(rows)]

    def additionMatrix(self, other):
        if self.rows != other.rows or self.columns != other.columns:
            raise ValueError("these matrices cannot multiply")
        result = matrix(self.data, self.columns)
        for i in range(self.rows):
            for j in range(self.columns):
                result.data[i][j] = self.data[i][j] + other.data[i][j]
            return result
