

class Queen():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def return_possible_cells(self, x_restriction, y_restriction):
        cells = [[self.x, self.y]]
        dirrections = [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]]
        for dir in dirrections:
            len = 1
            while x_restriction[0] <= self.x + dir[0] * len < x_restriction[1] and \
                y_restriction[0] <= self.y + dir[1] * len < y_restriction[1]:
                cells.append([self.x + dir[0] * len, self.y + dir[1] * len])
                len += 1
        return cells
                  
class Board:
    def __init__(self, m, n):
        self.m = m
        self.n = n
        self.queens = []
        
    def put_new_queen(self, x, y):
        queen = Queen(x, y) 
        hit_cells = queen.return_possible_cells([0, self.m], [0, self.n])
        for hit_cell in hit_cells:
            for queen_pos in self.queens:
                if hit_cell == queen_pos:
                    return False
        self.queens.append([x, y])
        return True

    def get_queen(self):
        if len(self.queens) > 0:
            self.queens.pop(len(self.queens) - 1)


class ArrangeFigures:
    def __init__(self):
        self.board_size = 8
        self.board = Board(self.board_size, self.board_size)
    
    def solve_problem(self):
        return self.board.queens if self.try_put_figure(0) else None
     
    def try_put_figure(self, step):
        if step == self.board_size:
            return True
        for x in range(self.board_size):
            for y in range(self.board_size):
                if self.board.put_new_queen(x, y):
                    if self.try_put_figure(step + 1):
                        return True
                    self.board.get_queen()
        return False


af = ArrangeFigures()
print(af.solve_problem())