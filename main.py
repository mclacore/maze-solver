from tkinter import Tk, BOTH, Canvas
import time


class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.root = Tk()
        self.root.title("Maze Solver")
        self.root.protocol("WM_DELETE_WINDOW", self.close)

        self.canvas = Canvas(self.root, width=self.width, height=self.height)
        self.canvas.pack(fill=BOTH, expand=True)

        self.win_running = False


    def redraw(self):
        self.root.update_idletasks()
        self.root.update()


    def wait_for_close(self):
        self.win_running = True
        while self.win_running:
            self.redraw()
            time.sleep(0.01)


    def draw_line(self, line, fill_color):
        line.draw(self.canvas, fill_color)


    def close(self):
        self.win_running = False


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:
    def __init__(self, start_point, end_point):
        self.start_point = start_point
        self.end_point = end_point


    def draw(self, canvas, fill_color):
        canvas.create_line(
            self.start_point.x,
            self.start_point.y,
            self.end_point.x,
            self.end_point.y,
            fill=fill_color,
            width=2
        )


class Cell:
    def __init__(self, _x1, _x2, _y1, _y2, _win, has_left_wall=True, has_right_wall=True, has_top_wall=True, has_bottom_wall=True):
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall
        self._x1 = _x1
        self._x2 = _x2
        self._y1 = _y1
        self._y2 = _y2
        self._win = _win


    def draw(self, fill_color, canvas):
        if self.has_left_wall:
            canvas.create_line(
                self._x1,
                self._y1,
                self._x1,
                self._y2,
                fill=fill_color,
                width=2
            )
        if self.has_right_wall:
            canvas.create_line(
                self._x2,
                self._y1,
                self._x2,
                self._y2,
                fill=fill_color,
                width=2
            )
        if self.has_top_wall:
            canvas.create_line(
                self._x1,
                self._y1,
                self._x2,
                self._y1,
                fill=fill_color,
                width=2
            )
        if self.has_bottom_wall:
            canvas.create_line(
                self._x1,
                self._y2,
                self._x2,
                self._y2,
                fill=fill_color,
                width=2
            )


    def draw_move(self, to_cell, undo=False):
        



def main():
    win = Window(800, 600)

    canvas = win.canvas

    cell1 = Cell(100, 200, 100, 200, win)
    cell2 = Cell(200, 300, 100, 200, win, has_top_wall=False)
    cell3 = Cell(100, 200, 200, 300, win, has_left_wall=False, has_bottom_wall=False)

    cell1.draw("black", canvas)
    cell2.draw("red", canvas)
    cell3.draw("blue", canvas)

    win.wait_for_close()


main()
