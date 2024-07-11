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
    def __init__(self, has_left_wall, has_right_wall, has_top_wall, has_bottom_wall, _x1, _x2, _y1, _y2, _win):
        foo
        # ]M



def main():
    win = Window(800, 600)
    start_point = Point(100, 100)
    end_point = Point(400, 300)
    line = Line(start_point, end_point)
    win.draw_line(line, "red")
    win.wait_for_close()


main()
