import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells[0]),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells),
            num_rows,
        )
        x1 = m1._cells[0][0]._x1
        x2 = m1._cells[0][0]._x2
        y1 = m1._cells[0][0]._y1
        y2 = m1._cells[0][0]._y2
        self.assertEqual(
            x1,
            0,
        )
        self.assertEqual(
            y1,
            0,
        )
        self.assertEqual(
            x2,
            10,
        )
        self.assertEqual(
            y2,
            10,
        )
        x1 = m1._cells[num_rows-1][num_cols-1]._x1
        x2 = m1._cells[num_rows-1][num_cols-1]._x2
        y1 = m1._cells[num_rows-1][num_cols-1]._y1
        y2 = m1._cells[num_rows-1][num_cols-1]._y2
        self.assertEqual(
            x1,
            (num_cols-1)*10,
        )
        self.assertEqual(
            y1,
            (num_rows-1)*10,
        )
        self.assertEqual(
            x2,
            num_cols*10,
        )
        self.assertEqual(
            y2,
            num_rows*10,
        )
        self.assertEqual(
            m1._cells[0][0].has_top_wall,
            False,
        )
        self.assertEqual(
            m1._cells[num_rows-1][num_cols-1].has_bottom_wall,
            False,
        )
        self.assertEqual(
            m1._cells[0][0].visited,
            False,
        )
        self.assertEqual(
            m1._cells[num_rows-1][num_cols-1].visited,
            False,
        )


if __name__ == "__main__":
    unittest.main()