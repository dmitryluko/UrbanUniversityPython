from math import inf


def divide(numerator: int, denominator: int) -> float:
    try:
        return numerator / denominator

    except ZeroDivisionError:
        return inf
