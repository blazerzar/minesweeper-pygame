"""Module with Cell class for Minesweeper."""

import os

import pygame


class Cell:
    """Class to represent a cell."""

    def __init__(self, minesweeper):
        "Initialize cell attributes."
        super().__init__()
        self.screen = minesweeper.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = minesweeper.settings

        # Create image of a closed cell
        self.image = pygame.image.load(os.path.join(
            minesweeper.my_path, "images/cell_closed.bmp"))
        self.image = pygame.transform.scale(
            self.image, (self.settings.cell_size, self.settings.cell_size))
        self.rect = self.image.get_rect()

        # Create images of open cells
        self.image_mine = pygame.image.load(os.path.join(
            minesweeper.my_path, "images/mine_open.bmp"))

        # Status -1 means mine, 0 is empty, number refers to number of
        # adjesent mines.
        self.status = 0

    def blitme(self):
        """Draw cell to the screen."""
        self.screen.blit(self.image, self.rect)