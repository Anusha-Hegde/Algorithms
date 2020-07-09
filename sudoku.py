from math import sqrt
class Sudoku:
        
        def __init__(self, N = 3):
            self.N = N
            self.count = 0
            self.n = int(sqrt(N))
            self.matrix = []
            for i in range(self.N):
                self.matrix.append([0 for j in range(self.N)])

        def possible(self, row, col, num) -> bool:
            x = int(row/self.n)*self.n
            y = int(col/self.n)*self.n
            def sub(x, y, num):
                for i in range(x, x+self.n):
                    for j in range(y, y+self.n):
                        if i == row and j == col: return True
                        if self.matrix[i][j] == num: return False
            if not sub(x, y, num) : return False
            i = row-1
            while i >= 0:
                if self.matrix[i][col] == num: return False
                i -= 1
            i = col-1
            while i >= 0:                
                if self.matrix[row][i] == num: return False
                i -= 1
            return True
            


        def sudoku(self, row = 0, col = 0):
            if col == self.N: 
                self.sudoku(row+1, 0)
                return
            if row == self.N:
                for i in range(self.N):
                    print(self.matrix[i])
                exit()
            for j in range(1, self.N + 1):
                if self.possible(row, col, j):
                    self.matrix[row][col] = j
                    self.sudoku(row, col+1)
                                


def main():
    sud = Sudoku(9)
    sud.sudoku()
    


if __name__ == "__main__": main()