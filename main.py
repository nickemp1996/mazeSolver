from window import Window
from maze import Maze

win = Window(800, 600)
m = Maze(10, 10, 15, 15, 20, 20, win)
m.solve()
win.wait_for_close()