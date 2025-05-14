from tkinter import Tk, BOTH, Canvas

class Window:
	def __init__(self, width, height):
		self.__root = Tk()
		self.__root.title = "Maze Solver"
		self.__root.protocol("WM_DELETE_WINDOW", self.close)
		self.canvas = Canvas(self.__root, width=width, height=height)
		self.canvas.pack()
		self.__running = False

	def redraw(self):
		self.__root.update_idletasks()
		self.__root.update()

	def wait_for_close(self):
		self.__running = True
		while self.__running:
			self.redraw()

	def close(self):
		self.__running = False

	def draw_line(self, line, fill_color):
		line.draw(self.canvas, fill_color)
