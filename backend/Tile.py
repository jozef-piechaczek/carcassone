# ekserymentalna klasa reprezentacji płytek
class Tile:
    # constants
    DEFAULT = 0
    MEADOW = 1
    CASTLE = 2
    MONASTERY = 3

    #    1 2 3
    # 12       4
    # 11   0   5
    # 10       6
    #    9 8 7

    def __init__(self):
        # each member of the tuple containing connected edges type of terrain, id (internal), and player's pawn
        self.sides = [([1, 3, 4, 6, 7, 9, 10, 11, 12], Tile.MEADOW, 1, None), ([2, 5, 8], Tile.CASTLE, 2, None)]
        self.center = [([0], Tile.MONASTERY, 2, None)]

    def turn_clockwise(self):
        for i in self.sides:
            for j in range(len(i[0])):
                i[0][j] = (i[0][j] + 2) % 12 + 1

    def turn_counterclockwise(self):
        for i in self.sides:
            for j in range(len(i[0])):
                i[0][j] = (i[0][j] - 4) % 12 + 1

    def find_side(self, terrain):
        for i in self.sides:
            if terrain in i[0]:
                return i[1]
        return None

    def find_side_internal(self, terrain):
        for i in self.sides:
            if terrain in i[0]:
                return i[2]
        return None

    def fit_up(self, other):  # can I place the other tile on top of this one?
        if (
                self.find_side(1) == other.find_side(9)
                and self.find_side(2) == other.find_side(8)
                and self.find_side(3) == other.find_side(7)
        ):
            return True
        return False

    def fit_right(self, other):  # can I place the other tile on top of this one?
        if (
                self.find_side(4) == other.find_side(12)
                and self.find_side(5) == other.find_side(11)
                and self.find_side(6) == other.find_side(10)
        ):
            return True
        return False

    def fit_down(self, other):  # can I place the other tile on top of this one?
        if (
                self.find_side(9) == other.find_side(1)
                and self.find_side(8) == other.find_side(2)
                and self.find_side(7) == other.find_side(3)
        ):
            return True
        return False

    def fit_left(self, other):  # can I place the other tile on top of this one?
        if (
                self.find_side(12) == other.find_side(4)
                and self.find_side(11) == other.find_side(5)
                and self.find_side(10) == other.find_side(6)
        ):
            return True
        return False
