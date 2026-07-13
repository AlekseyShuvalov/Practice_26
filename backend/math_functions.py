class Polynom:
    def __init__(self, cfs):
        self.cfs = cfs

    def value_at_point(self, x):
        return sum(coef * (x ** i) for i, coef in enumerate(self.cfs))

    def get_bounds(self, l, r, dots = 300):
        step = (r - l) / dots
        values = [self.value_at_point(l + i * step) for i in range(dots + 1)]
        return min(values), max(values)

class StepFunc:
    def __init__(self, heights, l, r):
        self.heights = heights
        self.l = l
        self.r = r

    def value_at_point(self, x):
        length = len(self.heights)
        step_width = (self.r - self.l) / length
        id = int((x - self.l) // step_width)
        id = max(0, min(length - 1, id))
        return self.heights[id]