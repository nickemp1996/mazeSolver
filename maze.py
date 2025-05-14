import time
import random
from cell import Point, Cell

class Maze:
	def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None,
        seed=None
    ):
	    self.x1 = x1
	    self.y1 = y1
	    self.num_rows = num_rows
	    self.num_cols = num_cols
	    self.cell_size_x = cell_size_x
	    self.cell_size_y = cell_size_y
	    self._win = win
	    if seed:
	    	random.seed(seed)
	    self._create_cells()

	def _create_cells(self):
	    self._cells = []
	    for i in range(self.num_rows):
	        row = []
	        for j in range(self.num_cols):
	            cell = Cell(Point(0, 0), Point(0, 0), self._win)
	            row.append(cell)
	        self._cells.append(row)
	        
	    # Now that all cells exist in the structure, draw them
	    for i in range(self.num_rows):
	        for j in range(self.num_cols):
	            self._draw_cell(i, j)

	    self._break_entrance_and_exit()

	def _draw_cell(self, i, j):
		# Calculate top-left corner
		x1 = self.x1 + (j * self.cell_size_x)
		y1 = self.y1 + (i * self.cell_size_y)

		# Calculate bottom-right corner
		x2 = x1 + self.cell_size_x
		y2 = y1 + self.cell_size_y

		self._cells[i][j].update_coordinates(x1, x2, y1, y2)

		if self._win:
			self._cells[i][j].draw()

			self._animate()

	def _animate(self):
		self._win.redraw()
		time.sleep(0.05)

	def _break_entrance_and_exit(self):
		self._cells[0][0].has_top_wall = False
		self._draw_cell(0, 0)
		self._cells[self.num_rows-1][self.num_cols-1].has_bottom_wall = False
		self._draw_cell(self.num_rows-1, self.num_cols-1)
		self._break_walls_r(0, 0)
		self._reset_cells_visited()

	def _break_walls_r(self, i, j):
		self._cells[i][j].visited = True
		while 1:
			adjacent_cells = []
			if i > 0:
				if not self._cells[i-1][j].visited:
					adjacent_cells.append((i-1, j, "north"))
			if j < self.num_cols - 1:
				if not self._cells[i][j+1].visited:
					adjacent_cells.append((i, j+1, "east"))
			if i < self.num_rows - 1:
				if not self._cells[i+1][j].visited:
					adjacent_cells.append((i+1, j, "south"))
			if j > 0:
				if not self._cells[i][j-1].visited:
					adjacent_cells.append((i, j-1, "west"))
			if len(adjacent_cells) == 0:
				self._draw_cell(i, j)
				return
			adjacent_cell = adjacent_cells[random.randrange(len(adjacent_cells))]
			adjacent_i = adjacent_cell[0]
			adjacent_j = adjacent_cell[1]
			direction = adjacent_cell[2]
			if direction == "north":
				self._cells[i][j].has_top_wall = False
				self._cells[adjacent_i][adjacent_j].has_bottom_wall = False
			if direction == "east":
				self._cells[i][j].has_right_wall = False
				self._cells[adjacent_i][adjacent_j].has_left_wall = False
			if direction == "south":
				self._cells[i][j].has_bottom_wall = False
				self._cells[adjacent_i][adjacent_j].has_top_wall = False
			if direction == "west":
				self._cells[i][j].has_left_wall = False
				self._cells[adjacent_i][adjacent_j].has_right_wall = False
			self._break_walls_r(adjacent_i, adjacent_j)

	def _reset_cells_visited(self):
		for i in range(self.num_rows):
			for j in range(self.num_cols):
				self._cells[i][j].visited = False

	def solve(self):
		return self._solve_r(0, 0)

	def _solve_r(self, i, j):
		self._animate()
		self._cells[i][j].visited = True
		if i == self.num_rows - 1 and j == self.num_cols - 1:
			return True
		if i > 0:
			#North
			if not self._cells[i-1][j].has_bottom_wall and not self._cells[i-1][j].visited:
				self._cells[i][j].draw_move(self._cells[i-1][j])
				solved = self._solve_r(i-1, j)
				if solved:
					return True
				else:
					self._cells[i][j].draw_move(self._cells[i-1][j], undo=True)
		if j < self.num_cols - 1:
			#East
			if not self._cells[i][j+1].has_left_wall and not self._cells[i][j+1].visited:
				self._cells[i][j].draw_move(self._cells[i][j+1])
				solved = self._solve_r(i, j+1)
				if solved:
					return True
				else:
					self._cells[i][j].draw_move(self._cells[i][j+1], undo=True)
		if i < self.num_rows - 1:
			#South
			if not self._cells[i+1][j].has_top_wall and not self._cells[i+1][j].visited:
				self._cells[i][j].draw_move(self._cells[i+1][j])
				solved = self._solve_r(i+1, j)
				if solved:
					return True
				else:
					self._cells[i][j].draw_move(self._cells[i+1][j], undo=True)
		if j > 0:
			#West
			if not self._cells[i][j-1].has_right_wall and not self._cells[i][j-1].visited:
				self._cells[i][j].draw_move(self._cells[i][j-1])
				solved = self._solve_r(i, j-1)
				if solved:
					return True
				else:
					self._cells[i][j].draw_move(self._cells[i][j-1], undo=True)
		return False
