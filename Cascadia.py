import numpy as np
from enum import Enum


class Animal(Enum):
    BEAR = 0
    ELK = 1
    FOX = 2
    EAGLE = 3
    SALMON = 4


class Tile:
    def __init__(self, list_pos_anim: list[Animal], occ_anim: Animal = None):
        self.list_pos_anim = list_pos_anim
        self.occ_anim = occ_anim


    def __repr__(self):
        return f"Tile(list_pos_anim={self.list_pos_anim}, occ_anim={self.occ_anim})"


class StartingTile():
    KEYSTONE_BEAR = np.array([[Tile([Animal.BEAR]), None], [Tile([Animal.EAGLE, Animal.ELK, Animal.FOX]), Tile([Animal.SALMON, Animal.BEAR])]])
    KEYSTONE_ELK = np.array([[Tile([Animal.ELK]), None], [Tile([Animal.EAGLE, Animal.ELK, Animal.BEAR]), Tile([Animal.FOX, Animal.SALMON])]])
    KEYSTONE_FOX = np.array([[Tile([Animal.FOX]), None], [Tile([Animal.SALMON, Animal.FOX, Animal.EAGLE]), Tile([Animal.BEAR, Animal.ELK])]])
    KEYSTONE_EAGLE = np.array([[Tile([Animal.EAGLE]), None], [Tile([Animal.SALMON, Animal.ELK, Animal.EAGLE]), Tile([Animal.BEAR, Animal.FOX])]])
    KEYSTONE_SALMON = np.array([[Tile([Animal.SALMON]), None], [Tile([Animal.SALMON, Animal.BEAR, Animal.ELK]), Tile([Animal.FOX, Animal.EAGLE])]])


class Board():
    def __init__(self, starting_tile: StartingTile):
        self.board = starting_tile


    def compute_placeable_coords(self):
        tup_row_col_occ_ind = np.nonzero(self.board)
        arr_occ_coords = np.array(list(zip(*tup_row_col_occ_ind)))

        list_pos_coords = []




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





