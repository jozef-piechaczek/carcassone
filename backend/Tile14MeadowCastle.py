from Enums import Terrains
from TileCastle import TileCastle
from TileMeadow import TileMeadow


class Tile14(TileCastle, TileMeadow):

    def __init__(self):
        super().__init__()
        self.sides = [[[1, 2, 3], Terrains.CASTLE, 1, None],
                      [[10, 11, 12], Terrains.CASTLE, 2, None],
                      [[4, 5, 6, 7, 8, 9], Terrains.MEADOW, 3, None]]
        self.center = [[0], Terrains.DEFAULT, 4, None]
        self.amount = 2