from figures.two_d import Triangle, Rectangle, Trapeze, Parallelogram, Circle
from figures.three_d import Ball, TriangularPyramid, QuadrangularPyramid, RectangularParallelepiped, Cone, TriangularPrism

def create_figure(name, params):
    try:
        if name == "Triangle":
            return Triangle(*params[:3])
        elif name == "Rectangle":
            return Rectangle(*params[:2])
        elif name == "Trapeze":
            return Trapeze(*params[:4])
        elif name == "Parallelogram":
            return Parallelogram(*params[:3])
        elif name == "Circle":
            return Circle(params[0])
        elif name == "Ball":
            return Ball(params[0])
        elif name == "TriangularPyramid":
            return TriangularPyramid(*params[:2])
        elif name == "QuadrangularPyramid":
            return QuadrangularPyramid(*params[:3])
        elif name == "RectangularParallelepiped":
            return RectangularParallelepiped(*params[:3])
        elif name == "Cone":
            return Cone(*params[:2])
        elif name == "TriangularPrism":
            return TriangularPrism(*params[:4])
    except:
        return None
