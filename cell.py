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

        # Cell's row and column attributes
        self.column = None
        self.row = None

        # Create image of a closed cell
        self.image = pygame.image.load(os.path.join(
            minesweeper.my_path, "images/cell_closed.bmp"))
        self.image = pygame.transform.scale(
            self.image, (self.settings.cell_size, self.settings.cell_size))
        self.rect = self.image.get_rect()

        # Create images of open cells.
        self.image_open = pygame.image.load(os.path.join(
            minesweeper.my_path, "images/cell_open.bmp"))
        self.image_open = pygame.transform.scale(
            self.image_open,
            (self.settings.cell_size, self.settings.cell_size))
        self.image_mine = pygame.image.load(os.path.join(
            minesweeper.my_path, "images/mine_open.bmp"))
        self.image_mine = pygame.transform.scale(
            self.image_mine,
            (self.settings.cell_size, self.settings.cell_size))
        self.image_cell_1 = pygame.image.load(os.path.join(
            minesweeper.my_path, "images/cell_1.bmp"))
        self.image_cell_1 = pygame.transform.scale(
            self.image_cell_1,
            (self.settings.cell_size, self.settings.cell_size))
        self.image_cell_2 = pygame.image.load(os.path.join(
            minesweeper.my_path, "images/cell_2.bmp"))
        self.image_cell_2 = pygame.transform.scale(
            self.image_cell_2,
            (self.settings.cell_size, self.settings.cell_size))
        self.image_cell_3 = pygame.image.load(os.path.join(
            minesweeper.my_path, "images/cell_3.bmp"))
        self.image_cell_3 = pygame.transform.scale(
            self.image_cell_3,
            (self.settings.cell_size, self.settings.cell_size))
        self.image_cell_4 = pygame.image.load(os.path.join(
            minesweeper.my_path, "images/cell_4.bmp"))
        self.image_cell_4 = pygame.transform.scale(
            self.image_cell_4,
            (self.settings.cell_size, self.settings.cell_size))
        self.image_cell_5 = pygame.image.load(os.path.join(
            minesweeper.my_path, "images/cell_5.bmp"))
        self.image_cell_5 = pygame.transform.scale(
            self.image_cell_5,
            (self.settings.cell_size, self.settings.cell_size))
        self.image_cell_6 = pygame.image.load(os.path.join(
            minesweeper.my_path, "images/cell_6.bmp"))
        self.image_cell_6 = pygame.transform.scale(
            self.image_cell_6,
            (self.settings.cell_size, self.settings.cell_size))
        self.image_cell_7 = pygame.image.load(os.path.join(
            minesweeper.my_path, "images/cell_7.bmp"))
        self.image_cell_7 = pygame.transform.scale(
            self.image_cell_7,
            (self.settings.cell_size, self.settings.cell_size))
        self.image_cell_8 = pygame.image.load(os.path.join(
            minesweeper.my_path, "images/cell_8.bmp"))
        self.image_cell_8 = pygame.transform.scale(
            self.image_cell_8,
            (self.settings.cell_size, self.settings.cell_size))

        # Create image of a flagged cell.
        self.image_flagged = pygame.image.load(os.path.join(
            minesweeper.my_path, "images/cell_flagged.bmp"))
        self.image_flagged = pygame.transform.scale(
            self.image_flagged,
            (self.settings.cell_size, self.settings.cell_size))

        # Status -1 means mine, 0 is empty, number refers to number of
        # adjesent mines.
        self.status = 0

        # State 1 means closed, 0 means opened, -1 means flagged.
        self.state = 1

        # Number of surrounding cells that are flagged
        self.flagged_number = 0

    def open_cell(self, cells):
        """Open the selected cell and cell's around it, if its status is 0"""
        if self.status == 0 and self.state == 1:
            self.state = 0
            # Open all the cells around the original one.
            cell_x = []
            cell_y = []

            # Go through all neighbour's coordinates and only use good ones.
            for p_value in range(self.column - 1, self.column + 2):
                if 0 <= p_value < self.settings.cells_x:
                    cell_x.append(p_value)
            for q_value in range(self.row - 1, self.row + 2):
                if 0 <= q_value < self.settings.cells_y:
                    cell_y.append(q_value)

            # Open surrounding cells.
            for x_value in cell_x:
                for y_value in cell_y:
                    if x_value != self.column or y_value != self.row:
                        cells[y_value][x_value].open_cell(cells)

        if self.state != -1:
            self.state = 0

    def flag_cell(self, cells):
        """Flag the selected cell."""
        self.state *= -1

        # Change flagged_number attribute for all neighbours.
        cell_x = []
        cell_y = []

        # Go through all neighbour's coordinates and only use good ones.
        for p_value in range(self.column - 1, self.column + 2):
            if 0 <= p_value < self.settings.cells_x:
                cell_x.append(p_value)
        for q_value in range(self.row - 1, self.row + 2):
            if 0 <= q_value < self.settings.cells_y:
                cell_y.append(q_value)

        # Add 1 to every cell's attribute.
        for x_value in cell_x:
            for y_value in cell_y:
                if x_value != self.column or y_value != self.row:
                    cells[y_value][x_value].flagged_number += 1

    def blitme(self):
        """Draw cell to the screen."""
        if self.state == 1:
            self.screen.blit(self.image, self.rect)
        elif self.state == -1:
            self.screen.blit(self.image_flagged, self.rect)
        elif self.state == 0:
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
