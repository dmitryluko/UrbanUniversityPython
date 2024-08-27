def divide(numerator: int, denominator: int) -> float | str:

    try:
        return numerator / denominator

    except ZeroDivisionError:
        return 'Error'


