"""Module with Cell class for Minesweeper."""

import os

import pygame
from pygame.sprite import Sprite


class Cell(Sprite):
    """Class to represent a cell."""

    def __init__(self, minesweeper):
        "Initialize cell attributes."
        super().__init__()
        self.screen = minesweeper.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = minesweeper.settings

        self.image = pygame.image.load(os.path.join(
            minesweeper.my_path, "images/cell_closed.bmp"))
        self.image = pygame.transform.scale(
            self.image, (self.settings.cell_size, self.settings.cell_size))
        self.rect = self.image.get_rect()
