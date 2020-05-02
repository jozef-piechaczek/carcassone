from backend.tile.Enums import Terrains, TileIDs
from backend.tile.TileRoad import TileRoad
from backend.tile.TileMeadow import TileMeadow


class Tile22(TileMeadow, TileRoad):

    id = TileIDs.TILE22
    amount = 9

    def __init__(self):
        super().__init__()
        self.sides = [[[1, 2, 3, 4, 5, 6, 7, 12], Terrains.MEADOW, 1, None],
                      [[8, 11], Terrains.ROAD, 2, None],
                      [[9, 10], Terrains.MEADOW, 3, None]]
        self.center = [[0], Terrains.DEFAULT, 4, None]