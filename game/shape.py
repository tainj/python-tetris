from game.utils import get_color, tuples_to_lists


class Shape:
    def __init__(self, coordinates: list[tuple[int, int]], center: tuple[int, int]=None):
        self.coordinates = tuples_to_lists(coordinates)
        self.color: tuple[int, int, int] = get_color()
        if center:
            self.center = list(center)
        else:
            self.center = center


class OShape(Shape):
    def __init__(self):
        super().__init__(
            coordinates=[(4, 0), (5, 0), (4, 1), (5, 1)],
            center=None
        )


class ZShape(Shape):
    def __init__(self):
        super().__init__(
            coordinates=[(3, 0), (4, 0), (4, 1), (5, 1)],
            center=(4, 1)
        )


class SShape(Shape):
    def __init__(self):
        super().__init__(
            coordinates=[(3, 1), (4, 1), (4, 0), (5, 0)],
            center=(4, 1)
        )


class TShape(Shape):
    def __init__(self):
        super().__init__(
            coordinates=[(3, 0), (4, 0), (5, 0), (4, 1)],
            center=(4, 0)
        )


class LShape(Shape):
    def __init__(self):
        super().__init__(
            coordinates=[(3, 0), (4, 0), (5, 0), (3, 1)],
            center=(4, 0)
        )


class IShape(Shape):
    def __init__(self):
        super().__init__(
            coordinates=[(3, 0), (4, 0), (5, 0), (6, 0)],
            center=(5, 0)
        )


class JShape(Shape):
    def __init__(self):
        super().__init__(
            coordinates=[(3, 0), (4, 0), (5, 0), (5, 1)],
            center=(4, 0)
        )