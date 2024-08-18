import math

class dis:
    def __init__(self):
        pass

    def distance(x1, y1, x2, y2):
        dist = math.sqrt(math.fabs(x2-x1)**2 + math.fabs(y2-y1)**2)
        return dist