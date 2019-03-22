# coding: utf-8
# author: 88IO
# date: 2019-03-22

import numpy as np


class BezierCurve:
    def __init__(self, points):
        self.points = points
        self.bezier_points = []

    def getBezierPoints(self, step=100):
        def getPartOfBPoints(points, t):
            bezier_parts = []
            for p1, p2 in zip(points, points[1:]):
                bezier_parts.append(
                    [p1[0] * (1 - t) + p2[0] * t, p1[1] * (1 - t) + p2[1] * t])
            # ココ汚い
            if len(bezier_parts) == 1:
                return [round(bezier_parts[0][0]), round(bezier_parts[0][1])]
            else:
                return getPartOfBPoints(bezier_parts, t)

        for t in np.arange(0, 1, 1 / step):
            self.bezier_points.append(getPartOfBPoints(self.points, t))

        self.bezier_points.append(self.points[-1])

        return self.bezier_points

    def drawBezier(self, canvas, **args):
        canvas.create_line(*np.array(self.bezier_points).flatten(), args)

    def drawOriginLines(self, canvas, **args):
        canvas.create_line(*np.array(self.points).flatten(), args)
