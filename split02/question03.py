import re
from math import sqrt


def figure_perimetr(points_data: str) -> float:
    def line_length(x1, y1, x2, y2):
        return sqrt((int(x2) - int(x1))**2 + (int(y2) - int(y1))**2)

    pattern = '[0-9]'
    points = re.findall(pattern, points_data)
    lines = []
    for i in range(0, len(points), 4):
        lines.append(line_length(points[i], points[i+1], points[i+2], points[i+3]))
    for i in range(0, len(points) - 4, 2):
        lines.append(line_length(points[i], points[i+1], points[i+4], points[i+5]))
    
    return round(sum(lines), 14)
