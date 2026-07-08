# Функции для мат. вычислений

def poly_value_at_point(cfs, x):
    return sum(coef * (x ** i) for i, coef in enumerate(cfs))

def step_func_value_at_point(heights, l, r, x):
    length = len(heights)
    step_width = (r - l) / length
    id = int((x - l) // step_width)
    id = max(0, min(length - 1, id))
    return heights[id]

def bounds_of_polynom(cfs, l, r, dots = 300):
    step = (r - l) / dots
    values = [poly_value_at_point(cfs, l + i * step) for i in range(dots + 1)]
    return min(values), max(values)