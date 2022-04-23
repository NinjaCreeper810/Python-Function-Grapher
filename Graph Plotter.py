import tkinter as tk

# Scale of Graph
Scale = 3
# Max amount of points calculated inbetween each line
Detail = 100000
# Function for display **Make sure to also put in line 14 below using py syntax**
function = "(2 * (2 ** x_value)) / ((x_value ** 2) - 9)"


def calculate(x_value):
    try:
        """***Enter Function here - Cannot take a negative number to the power of a non-whole number***"""
        return (2 * (2 ** x_value)) / ((x_value ** 2) - 9)
    except ZeroDivisionError:
        return 100000000


root = tk.Tk()
root.title("Graphing Calculator")

canvas = tk.Canvas(root, height=1000, width=1000, bg="White")
canvas.pack()

labels = tk.Label(text="Function: " + function, fg="black")
labels.place(x=20, y=20)
labels1 = tk.Label(text="Scale " + str(Scale) + ":1", fg="black")
labels1.place(x=20, y=40)
labels2 = tk.Label(text="Detail Level: " + str(Detail), fg="black")
labels2.place(x=20, y=60)

line = tk.Frame(root, bg="black")
line.place(width=1005, height=5, y=498)


line2 = tk.Frame(root, bg="black")
line2.place(width=5, height=1005, x=498)

for x_val in range(0, 19):
    if x_val != 9:
        marker_line = tk.Frame(root, bg="black")
        marker_line.place(width=5, height=20, x=(50 + (x_val * 50)), y=491)

for x_val in range(0, 19):
    if x_val != 9:
        marker_line1 = tk.Frame(root, bg="black")
        marker_line1.place(width=20, height=5, y=(50 + (x_val * 50)), x=491)

last_point_x = 0
last_point_y = 0
total_x = int(Detail) * 20
for x in range(1, (total_x + 1)):
    x_position = (-10 * Scale) + ((1/Detail * Scale) * x)
    x_location = (((x_position/Scale) + 10)/20) * 1000
    y_position = calculate(x_position)
    try:
        if y_position > (Scale * -10):
            if y_position < (Scale * 10):
                y_location = (((y_position/Scale) + 10)/20) * 1000
                if round(y_location) != round(last_point_y) or round(x_location) != round(last_point_x):
                    Point = tk.Frame(root, bg="red")
                    Point.place(width=2, height=2, y=round(1000 - y_location), x=round(x_location))
                    print("(", round(y_location), ",", round(x_location), ")")
                    last_point_y = y_location
                    last_point_x = x_location
    except TypeError:
        print("Complex number not plotted")
root.mainloop()

# Check documentation at top
