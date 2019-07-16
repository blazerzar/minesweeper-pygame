"""The main file with all the logic for Minesweeper"""

import sys
import os
import random

import pygame

from cell import Cell
from settings import Settings


class Minesweeper:
    """Class to handle running the game."""

    def __init__(self):
        """Initialize pygame and game resources."""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        self.my_path = os.path.dirname(os.path.realpath(__file__))
        pygame.display.set_caption("Minesweeper")

        self.clock = pygame.time.Clock()

        # Create cells and mines
        self.cells = []
        self._create_grid()
        self._create_mines()

    def run_game(self):
        """Function with main game loop."""
    	# Main game loop
        while True:
            self._check_events()
            self._update_screen()
            self.clock.tick(self.settings.game_framerate)

    def _check_events(self):
        """Check for events and respond to them."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        """Update all the elements on the screen."""
        # Fill the background
        self.screen.fill(self.settings.background_colour)
        # Draw cells to the screen
        self._draw_cells()
        # Update the screen
        pygame.display.update()

    def _create_cell(self, cell_x, cell_y, row_number):
        """Create one cell and add it to cells group."""
        cell = Cell(self)
        cell.rect.x = cell_x
        cell.rect.y = cell_y
        self.cells[row_number].append(cell)

    def _create_row(self, row_number):
        """Create one row of cells."""
        for column in range(0, self.settings.cells_x):
            cell_x = self.settings.side_margin + column*self.settings.cell_size
            cell_y = (self.settings.top_margin
                      + row_number*self.settings.cell_size)
            self._create_cell(cell_x, cell_y, row_number)

    def _create_grid(self):
        """Create full grid of cells."""
        for row in range(0, self.settings.cells_y):
            self.cells.append([])
            self._create_row(row)

    def _draw_cells(self):
        """Draw all cells to the screen."""
        for row in self.cells:
            for cell in row:
                cell.blitme()

    def _create_mines(self):
        """Give mines to desired number of cells."""
        # Create a temporary list of all cells
        temp_cells = []
        for row in self.cells:
            for cell in row:
                temp_cells.append(cell)

        # Create a list of random indexes
        mines_indexes = []
        for _ in range(self.settings.mines):
            mines_indexes.append(random.randint(0, len(temp_cells) - 1))
        print(mines_indexes)

        # Assign mines
        for index in mines_indexes:
            temp_cells[index].status = -1


if __name__ == "__main__":
    MINESWEEPER = Minesweeper()
    MINESWEEPER.run_game()
