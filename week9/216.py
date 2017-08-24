from sys import stdin


class Matrix:
    def __init__(self, m):
        self.rows = len(m)
        self.colums = len(m[0])
        self.matrix = []
        for i in range(self.rows):
            a = []
            for j in range(self.colums):
                a.append(m[i][j])
            self.matrix.append(a)

    def __str__(self):
        s = ""
        for i in range(self.rows):
            for j in range(self.colums):
                if j != self.colums - 1:
                    s += str(self.matrix[i][j]) + "\t"
                else:
                    s += str(self.matrix[i][j])
            if i != self.rows - 1:
                s += "\n"
        return s

    def size(self):
        return (self.rows, self.colums)

    def __add__(self, other):
        res_i = []
        for i in range(self.rows):
            res_j = []
            for j in range(self.colums):
                result = self.matrix[i][j] + other.matrix[i][j]
                res_j.append(result)
            res_i.append(res_j)
        return Matrix(res_i)

    def __mul__(self, other):
        res_i = []
        for i in range(self.rows):
            res_j = []
            for j in range(self.colums):
                result = self.matrix[i][j] * other
                res_j.append(result)
            res_i.append(res_j)
        return Matrix(res_i)

    def __rmul__(self, other):
        res_i = []
        for i in range(self.rows):
            res_j = []
            for j in range(self.colums):
                result = other * self.matrix[i][j]
                res_j.append(result)
            res_i.append(res_j)
        return Matrix(res_i)

exec(stdin.read())
