import tkinter
# Use `Bezier` Class
from tk_bezier import BezierCurve

# Tk Initialize
root = tkinter.Tk()
root.title("Bezier Construction")
root.geometry("600x600")

# Make Canvas
canvas = tkinter.Canvas(root, width=600, height=600)

# Sample Points
points = [[20, 20], [450, 200], [550, 400], [70, 480], [120, 550]]

# < My Bezier Library >
# Bezier Initialize
bezier = BezierCurve(points=points)
# the larger `step` is, the more smooth bezier curve is
bezier.getBezierPoints(step=300)
# canvas is a place where lines draw.
# you can use `create_line` function's option
bezier.drawOriginLines(canvas=canvas)
bezier.drawBezier(canvas=canvas, width=3, fill="blue")


# Pack Canvas to your window
canvas.pack()

# Main Loop
root.mainloop()
