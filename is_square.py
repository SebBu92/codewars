def is_square(n):
    if n >= 0:
        wurzel = n ** 0.5
        if (wurzel * wurzel) == n:
            return True
    return False