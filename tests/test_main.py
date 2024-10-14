import unittest
import logging


class Coord:
    def __init__(self, x, y):
        if isinstance(x, int) and isinstance(y, int):
            self.x = x
            self.y = y
        else:
            raise TypeError('x, y must be integers!')


class TestCoord(unittest.TestCase):
    logger = logging.getLogger(__name__)
    logging.basicConfig(level=logging.DEBUG)

    def test_coord_init(self):
        try:
            self.assertTrue(isinstance(Coord(1, 2), Coord), True)
            self.assertTrue(isinstance(Coord(1, '2'), Coord), True)

        except TypeError as e:
            self.logger.exception(e)
            print(f'Type error: {e}')
            assert False


if __name__ == "__main__":
    unittest.main()
