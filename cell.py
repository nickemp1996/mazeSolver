class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y

class Line:
	def __init__(self, point1, point2):
		self.point1 = point1
		self.point2 = point2

	def draw(self, canvas, fill_color):
		x1 = self.point1.x
		x2 = self.point2.x
		y1 = self.point1.y
		y2 = self.point2.y
		canvas.create_line(x1, y1, x2, y2, fill=fill_color, width=2)

class Cell:
	def __init__(self, top_left, bottom_right, window=None):
		self.has_left_wall = True
		self.has_right_wall = True
		self.has_top_wall = True
		self.has_bottom_wall = True
		self.visited = False
		self._x1 = top_left.x
		self._x2 = bottom_right.x
		self._y1 = top_left.y
		self._y2 = bottom_right.y
		self._win = window

	def draw(self):
		bg = self._win.canvas.cget("bg")
		left_fill_color = bg
		right_fill_color = bg
		top_fill_color = bg
		bottom_fill_color = bg

		if self.has_left_wall:
			left_fill_color = "white"
		if self.has_right_wall:
			right_fill_color = "white"
		if self.has_top_wall:
			top_fill_color = "white"
		if self.has_bottom_wall:
			bottom_fill_color = "white"

		left_top_point = Point(self._x1, self._y1)
		left_bottom_point = Point(self._x1, self._y2)
		left_wall = Line(left_top_point, left_bottom_point)
		self._win.draw_line(left_wall, left_fill_color)

		right_top_point = Point(self._x2, self._y1)
		right_bottom_point = Point(self._x2, self._y2)
		right_wall = Line(right_top_point, right_bottom_point)
		self._win.draw_line(right_wall, right_fill_color)

		top_left_point = Point(self._x1, self._y1)
		top_right_point = Point(self._x2, self._y1)
		top_wall = Line(top_left_point, top_right_point)
		self._win.draw_line(top_wall, top_fill_color)

		bottom_left_point = Point(self._x1, self._y2)
		bottom_right_point = Point(self._x2, self._y2)
		bottom_wall = Line(bottom_left_point, bottom_right_point)
		self._win.draw_line(bottom_wall, bottom_fill_color)

	def draw_move(self, to_cell, undo=False):
		mid_x = ((self._x2 - self._x1) / 2) + self._x1
		mid_y = ((self._y2 - self._y1) / 2) + self._y1
		mid_point1 = Point(mid_x, mid_y)
		mid_x = ((to_cell._x2 - to_cell._x1) / 2) + to_cell._x1
		mid_y = ((to_cell._y2 - to_cell._y1) / 2) + to_cell._y1
		mid_point2 = Point(mid_x, mid_y)
		line = Line(mid_point1, mid_point2)
		if undo:
			fill_color = "gray"
		else:
			fill_color = "red"
		self._win.draw_line(line, fill_color)

	def update_coordinates(self, x1, x2, y1, y2):
		self._x1 = x1
		self._x2 = x2
		self._y1 = y1
		self._y2 = y2