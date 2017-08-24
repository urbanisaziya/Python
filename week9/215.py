from sys import stdin


class Matrix:
    def __init__(self, m):
        self.matrix = []
        for i in range(len(m)):
            a = []
            for j in range(len(m[0])):
                a.append(m[i][j])
            self.matrix.append(a)

    def __str__(self):
        s = ""
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                if j != len(self.matrix[0]) - 1:
                    s += str(self.matrix[i][j]) + "\t"
                else:
                    s += str(self.matrix[i][j])
            if i != len(self.matrix) - 1:
                s += "\n"
        return s

    def size(self):
        return (len(self.matrix), len(self.matrix[0]))

exec(stdin.read())
