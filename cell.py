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
        self.image_open = pygame.image.load(os.path.join(
            minesweeper.my_path, "images/cell_open.bmp"))
        self.image_open = pygame.transform.scale(
            self.image_open, (self.settings.cell_size, self.settings.cell_size))
        self.image_mine = pygame.image.load(os.path.join(
            minesweeper.my_path, "images/mine_open.bmp"))
        self.image_mine = pygame.transform.scale(
            self.image_mine, (self.settings.cell_size, self.settings.cell_size))
        self.image_cell_1 = pygame.image.load(os.path.join(
            minesweeper.my_path, "images/cell_1.bmp"))
        self.image_cell_1 = pygame.transform.scale(
            self.image_cell_1, (self.settings.cell_size, self.settings.cell_size))
        self.image_cell_2 = pygame.image.load(os.path.join(
            minesweeper.my_path, "images/cell_2.bmp"))
        self.image_cell_2 = pygame.transform.scale(
            self.image_cell_2, (self.settings.cell_size, self.settings.cell_size))
        self.image_cell_3 = pygame.image.load(os.path.join(
            minesweeper.my_path, "images/cell_3.bmp"))
        self.image_cell_3 = pygame.transform.scale(
            self.image_cell_3, (self.settings.cell_size, self.settings.cell_size))
        self.image_cell_4 = pygame.image.load(os.path.join(
            minesweeper.my_path, "images/cell_4.bmp"))
        self.image_cell_4 = pygame.transform.scale(
            self.image_cell_4, (self.settings.cell_size, self.settings.cell_size))
        self.image_cell_5 = pygame.image.load(os.path.join(
            minesweeper.my_path, "images/cell_5.bmp"))
        self.image_cell_5 = pygame.transform.scale(
            self.image_cell_5, (self.settings.cell_size, self.settings.cell_size))
        self.image_cell_6 = pygame.image.load(os.path.join(
            minesweeper.my_path, "images/cell_6.bmp"))
        self.image_cell_6 = pygame.transform.scale(
            self.image_cell_6, (self.settings.cell_size, self.settings.cell_size))
        self.image_cell_7 = pygame.image.load(os.path.join(
            minesweeper.my_path, "images/cell_7.bmp"))
        self.image_cell_7 = pygame.transform.scale(
            self.image_cell_7, (self.settings.cell_size, self.settings.cell_size))
        self.image_cell_8 = pygame.image.load(os.path.join(
            minesweeper.my_path, "images/cell_8.bmp"))
        self.image_cell_8 = pygame.transform.scale(
            self.image_cell_8, (self.settings.cell_size, self.settings.cell_size))

        # Status -1 means mine, 0 is empty, number refers to number of
        # adjesent mines.
        self.status = 0

        # State 0 means closed, 1 means opened
        self.state = 0

    def blitme(self):
        """Draw cell to the screen."""
        if self.state == 0:
            self.screen.blit(self.image, self.rect)
        elif self.state == 1:
            if self.status == 0:
                self.screen.blit(self.image_open, self.rect)
            elif self.status == -1:
                self.screen.blit(self.image_mine, self.rect)
            elif self.status == 1:
                self.screen.blit(self.image_cell_1, self.rect)
            elif self.status == 2:
                self.screen.blit(self.image_cell_2, self.rect)
            elif self.status == 3:
                self.screen.blit(self.image_cell_3, self.rect)
            elif self.status == 4:
                self.screen.blit(self.image_cell_4, self.rect)
            elif self.status == 5:
                self.screen.blit(self.image_cell_5, self.rect)
            elif self.status == 6:
                self.screen.blit(self.image_cell_6, self.rect)
            elif self.status == 7:
                self.screen.blit(self.image_cell_7, self.rect)
            elif self.status == 8:
                self.screen.blit(self.image_cell_8, self.rect)
