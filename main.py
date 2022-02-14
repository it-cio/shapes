from shapes import *
from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Геометрический калькулятор")
window.configure(bg='grey20')
window.overrideredirect(True)
x = 640
y = 384


def make_canvas():
    window = Tk()
    window.title("Холст")
    canvas = Canvas(window, width=1280, height=768, bg='grey20')
    canvas.pack()
    return canvas


def draw_circle():
    canvas = make_canvas()
    canvas.create_oval(220, 140, 420, 340, width=2, fill='grey20', outline='green yellow')


def draw_square():
    canvas = make_canvas()
    val = int(entry_square.get())
    x1 = x-val
    x2 = x+val
    y1 = y-val
    y2 = y+val
    canvas.create_polygon(x1, y1, x2, y1, x2, y2, x1, y2, width=2, fill='grey20', outline='green yellow')
    square = Square(val)
    messagebox.showinfo("Расчет", f"Площадь: {square.area()}\nПериметр: {square.perimetr()}")


def draw_rectangle():
    canvas = make_canvas()
    canvas.create_polygon(220, 200, 420, 200, 420, 280, 220, 280, width=2, fill='grey20', outline='green yellow')


def draw_triangle():
    canvas = make_canvas()
    canvas.create_polygon(320, 140, 220, 340, 420, 340, width=2, fill='grey20', outline='green yellow')


def draw_trapeze():
    canvas = make_canvas()
    canvas.create_polygon(270, 200, 370, 200, 420, 280, 220, 280, width=2, fill='grey20', outline='green yellow')


def draw_rhombus():
    canvas = make_canvas()
    canvas.create_polygon(320, 140, 370, 240, 320, 340, 270, 240, width=2, fill='grey20', outline='green yellow')


def draw_sphere():
    canvas = make_canvas()
    pass


def draw_cube():
    canvas = make_canvas()
    pass


def draw_parallelepiped():
    canvas = make_canvas()
    pass


def draw_pyramid():
    canvas = make_canvas()
    pass


def draw_cylinder():
    canvas = make_canvas()
    pass


def draw_cone():
    canvas = make_canvas()
    pass


# Плоские фигуры
Label(window, text="Плоские фигуры", font=('Arial Bold', 14), bg='grey20', fg='green yellow') \
    .grid(row=0, column=0, columnspan=6, pady=10, sticky='nsew')

Button(window, text="Круг", width=14, height=2, bg='grey30', fg='green yellow', command=draw_circle) \
    .grid(row=1, column=0, padx=5, pady=5, sticky='nsew')
Label(window, text="Радиус круга", font=('Arial Bold', 8), bg='grey20', fg='green') \
    .grid(row=2, column=0, padx=5, sticky=W)
Entry(window, bg='grey30', fg='green yellow') \
    .grid(row=3, column=0, padx=5, sticky='nsew')

Button(window, text="Квадрат", width=14, height=2, bg='grey30', fg='green yellow', command=draw_square) \
    .grid(row=1, column=1, padx=5, pady=5, sticky='nsew')
Label(window, text="Сторона квадрата", font=('Arial Bold', 8), bg='grey20', fg='green') \
    .grid(row=2, column=1, padx=5, sticky=W)
entry_square = Entry(window, bg='grey30', fg='green yellow')
entry_square.grid(row=3, column=1, padx=5, sticky='nsew')

Button(window, text="Прямоугольник", width=14, height=2, bg='grey30', fg='green yellow', command=draw_rectangle) \
    .grid(row=1, column=2, padx=5, pady=5, sticky='nsew')
Label(window, text="Первая сторона", font=('Arial Bold', 8), bg='grey20', fg='green') \
    .grid(row=2, column=2, padx=5, sticky=W)
Entry(window, bg='grey30', fg='green yellow') \
    .grid(row=3, column=2, padx=5, sticky='nsew')
Label(window, text="Вторая сторона", font=('Arial Bold', 8), bg='grey20', fg='green') \
    .grid(row=4, column=2, padx=5, sticky=W)
Entry(window, bg='grey30', fg='green yellow') \
    .grid(row=5, column=2, padx=5, sticky='nsew')

Button(window, text="Треугольник", width=14, height=2, bg='grey30', fg='green yellow', command=draw_triangle) \
    .grid(row=1, column=3, padx=5, pady=5, sticky='nsew')
Label(window, text="Первая сторона", font=('Arial Bold', 8), bg='grey20', fg='green') \
    .grid(row=2, column=3, padx=5, sticky=W)
Entry(window, bg='grey30', fg='green yellow') \
    .grid(row=3, column=3, padx=5, sticky='nsew')
Label(window, text="Вторая сторона", font=('Arial Bold', 8), bg='grey20', fg='green') \
    .grid(row=4, column=3, padx=5, sticky=W)
Entry(window, bg='grey30', fg='green yellow') \
    .grid(row=5, column=3, padx=5, sticky='nsew')
Label(window, text="Основание", font=('Arial Bold', 8), bg='grey20', fg='green') \
    .grid(row=6, column=3, padx=5, sticky=W)
Entry(window, bg='grey30', fg='green yellow') \
    .grid(row=7, column=3, padx=5, sticky='nsew')

Button(window, text="Трапеция", width=14, height=2, bg='grey30', fg='green yellow', command=draw_trapeze) \
    .grid(row=1, column=4, padx=5, pady=5, sticky='nsew')
Label(window, text="Первая сторона", font=('Arial Bold', 8), bg='grey20', fg='green') \
    .grid(row=2, column=4, padx=5, sticky=W)
Entry(window, bg='grey30', fg='green yellow') \
    .grid(row=3, column=4, padx=5, sticky='nsew')
Label(window, text="Вторая сторона", font=('Arial Bold', 8), bg='grey20', fg='green') \
    .grid(row=4, column=4, padx=5, sticky=W)
Entry(window, bg='grey30', fg='green yellow') \
    .grid(row=5, column=4, padx=5, sticky='nsew')
Label(window, text="Первое основание", font=('Arial Bold', 8), bg='grey20', fg='green') \
    .grid(row=6, column=4, padx=5, sticky=W)
Entry(window, bg='grey30', fg='green yellow') \
    .grid(row=7, column=4, padx=5, sticky='nsew')
Label(window, text="Второе основание", font=('Arial Bold', 8), bg='grey20', fg='green') \
    .grid(row=8, column=4, padx=5, sticky=W)
Entry(window, bg='grey30', fg='green yellow') \
    .grid(row=9, column=4, padx=5, sticky='nsew')

Button(window, text="Ромб", width=14, height=2, bg='grey30', fg='green yellow', command=draw_rhombus) \
    .grid(row=1, column=5, padx=5, pady=5, sticky='nsew')
Label(window, text="Сторона ромба", font=('Arial Bold', 8), bg='grey20', fg='green') \
    .grid(row=2, column=5, padx=5, sticky=W)
Entry(window, bg='grey30', fg='green yellow') \
    .grid(row=3, column=5, padx=5, sticky='nsew')

# Объемные фигуры
Label(window, text="Объемные фигуры", font=('Arial Bold', 14), bg='grey20', fg='green yellow') \
    .grid(row=10, column=0, columnspan=6, pady=10, sticky='nsew')

Button(window, text="Сфера", width=14, height=2, bg='grey30', fg='green yellow', command=draw_sphere) \
    .grid(row=11, column=0, padx=5, pady=5, sticky='nsew')

Button(window, text="Куб", width=14, height=2, bg='grey30', fg='green yellow', command=draw_cube) \
    .grid(row=11, column=1, padx=5, pady=5, sticky='nsew')

Button(window, text="Параллелепипед", width=14, height=2, bg='grey30', fg='green yellow', command=draw_parallelepiped) \
    .grid(row=11, column=2, padx=5, pady=5, sticky='nsew')

Button(window, text="Пирамида", width=14, height=2, bg='grey30', fg='green yellow', command=draw_pyramid) \
    .grid(row=11, column=3, padx=5, pady=5, sticky='nsew')

Button(window, text="Цилиндр", width=14, height=2, bg='grey30', fg='green yellow', command=draw_cylinder) \
    .grid(row=11, column=4, padx=5, pady=5, sticky='nsew')

Button(window, text="Конус", width=14, height=2, bg='grey30', fg='green yellow', command=draw_cone) \
    .grid(row=11, column=5, padx=5, pady=5, sticky='nsew')
#
Button(window, text="Exit", bg='grey20', fg='green yellow', command=exit) \
    .grid(row=12, column=0, columnspan=6, padx=5, pady=5, sticky='nsew')

if __name__ == '__main__':
    window.mainloop()