import numpy as np
from enum import Enum
import collections


class Animal(Enum):
    BEAR = 0
    ELK = 1
    FOX = 2
    EAGLE = 3
    SALMON = 4


_Hex = collections.namedtuple("Hex", ["q", "r", "s"])
def Hex(q, r, s):
    assert not (round(q + r + s) != 0), "q + r + s must be 0"
    return _Hex(q, r, s)


def hex_add(a, b):
    return Hex(a.q + b.q, a.r + b.r, a.s + b.s)


hex_directions = [Hex(1, 0, -1), Hex(1, -1, 0), Hex(0, -1, 1), Hex(-1, 0, 1), Hex(-1, 1, 0), Hex(0, 1, -1)]
def hex_direction(direction):
    return hex_directions[direction]

def hex_neighbor(hex, direction):
    return hex_add(hex, hex_direction(direction))


class Tile:
    def __init__(self, pos: Hex, list_pos_anim: list[Animal], occ_anim: Animal = None):
        self.list_pos_anim = list_pos_anim
        self.occ_anim = occ_anim
        self.pos = pos


    def __repr__(self):
        return f"Tile(pos={self.pos}, list_pos_anim={self.list_pos_anim}, occ_anim={self.occ_anim})"


class Board():
    def __init__(self, starting_tile_top, starting_tile_left, starting_tile_right):
        self.board = [starting_tile_top, starting_tile_left, starting_tile_right]


    def compute_placeable_coords(self):
        for i in range(6):
            print(hex_neighbor(self.board[0].pos, i))


class StartingTile():
    KEYSTONE_BEAR = Board(Tile(Hex(0, 0, 0), [Animal.BEAR]), Tile(Hex(-1, 1, 0), [Animal.EAGLE, Animal.ELK, Animal.FOX]), Tile(Hex(0, 1, -1), [Animal.SALMON, Animal.BEAR]))
    KEYSTONE_ELK = Board(Tile(Hex(0, 0, 0), [Animal.ELK]), Tile(Hex(-1, 1, 0), [Animal.EAGLE, Animal.ELK, Animal.BEAR]), Tile(Hex(0, 1, -1), [Animal.FOX, Animal.SALMON]))
    KEYSTONE_FOX = Board(Tile(Hex(0, 0, 0), [Animal.FOX]), Tile(Hex(-1, 1, 0), [Animal.SALMON, Animal.FOX, Animal.EAGLE]), Tile(Hex(0, 1, -1), [Animal.BEAR, Animal.ELK]))
    KEYSTONE_EAGLE = Board(Tile(Hex(0, 0, 0), [Animal.EAGLE]), Tile(Hex(-1, 1, 0), [Animal.SALMON, Animal.ELK, Animal.EAGLE]), Tile(Hex(0, 1, -1), [Animal.BEAR, Animal.FOX]))
    KEYSTONE_SALMON = Board(Tile(Hex(0, 0, 0), [Animal.SALMON]), Tile(Hex(-1, 1, 0), [Animal.SALMON, Animal.BEAR, Animal.ELK]), Tile(Hex(0, 1, -1), [Animal.FOX, Animal.EAGLE]))


    def place_tile(self, tile: Tile, x: int, y: int):
        pass


class ScoringCard():
    def bear_A(board):
        pass


    def elk_A(board):
        pass


    def fox_A(board):
        pass


    def eagle_A(board):
        pass


    def salmon_A(board):
        pass


class Cascadia:
    def __init__(self, list_scoring_cards: list, starting_tile: StartingTile):
        self.list_scoring_cards = list_scoring_cards
        self.board = Board(starting_tile)





