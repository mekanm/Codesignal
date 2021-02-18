def shapeArea(n):
    n_num = int(n)
    outer_square = n * n
    inner_square = (n-1) * (n-1)
    total_area = outer_square + inner_square
    return total_area
