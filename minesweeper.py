"""The main file with all the logic for Minesweeper"""

import os
import random
import sys

import pygame

from button import Button
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

        # Dictionary to hold stats
        self.stats = {
            "state": 2,  # 0 means playing, -1 is dead, 1 solved, 2 start
            "mines_left": self.settings.mines,
            "time": 0,
            "time_float": 0
        }

        # Create the button
        self.emoji_button = Button(self)

        # Create cells and mines.
        self.cells = []
        self._create_grid()
        self._create_mines()
        self._calculate_all_neighbours()

    def run_game(self):
        """Function with main game loop."""
        # Main game loop
        while True:
            self._check_events()
            self._check_solve()
            self._update_screen()
            self._update_time()

    def _check_solve(self):
        """Check if all empty cells are open."""
        all_open = True
        for row in self.cells:
            for cell in row:
                if cell.status != -1 and cell.state == 1:
                    all_open = False

        if all_open:
            self.stats["state"] = 1
            self.emoji_button.current_emoji = 2

            # Flag all mine cells if not already
            for row in self.cells:
                for cell in row:
                    if cell.status == -1 and cell.state != -1:
                        cell.state = -1

    def _check_events(self):
        """Check for events and respond to them."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self.emoji_button.current_emoji *= -1
                if event.button == 3:
                    if self.stats["state"] == 0:
                        self._check_right_mouse(mouse_pos)
            elif event.type == pygame.MOUSEBUTTONUP:
                mouse_pos = pygame.mouse.get_pos()
                self.emoji_button.current_emoji *= -1
                if event.button == 1:
                    self._check_left_mouse(mouse_pos)
                elif event.button == 2:
                    if self.stats["state"] == 0:
                        self._check_middle_mouse(mouse_pos)

    def _check_left_mouse(self, mouse_pos):
        """Check for left mouse button presses and respond to them."""
        # Check if one of the cells is clicked.
        if self.stats["state"] == 0:
            for row in self.cells:
                for cell in row:
                    cell_clicked = cell.rect.collidepoint(mouse_pos)
                    # Open the selected cell.
                    if cell_clicked and cell.state == 1:
                        cell.open_cell(self.cells, self)

        # Check if one of the cells is clicked at the beginning.
        if self.stats["state"] == 2:
            self.stats["state"] = 0
            for row in self.cells:
                for cell in row:
                    cell_clicked = cell.rect.collidepoint(mouse_pos)
                    # Open the selected cell.
                    if cell_clicked and cell.state == 1:
                        cell.open_cell(self.cells, self)

        # Check if the emoji button is clicked.
        if self.emoji_button.rect.collidepoint(mouse_pos):
            self._reset_game()

    def _check_middle_mouse(self, mouse_pos):
        """check for middle mouse button presses and respond to them."""
        for row in self.cells:
            for cell in row:
                cell_clicked = cell.rect.collidepoint(mouse_pos)
                # Check if cell is already opened.
                # Only chord if cell.flagged_number == cell.status
                if (cell_clicked and cell.state == 0
                        and cell.flagged_number == cell.status):
                    # Open all the cells around the original one.
                    cell_x = []
                    cell_y = []

                    # Go through all neighbour's coordinates
                    # and only use good ones.
                    for p_value in range(cell.column - 1, cell.column + 2):
                        if 0 <= p_value < self.settings.cells_x:
                            cell_x.append(p_value)
                    for q_value in range(cell.row - 1, cell.row + 2):
                        if 0 <= q_value < self.settings.cells_y:
                            cell_y.append(q_value)

                    # Open surrounding cells.
                    for x_value in cell_x:
                        for y_value in cell_y:
                            if x_value != cell.column or y_value != cell.row:
                                self.cells[y_value][x_value].open_cell(
                                    self.cells, self)

    def _check_right_mouse(self, mouse_pos):
        """Check for right mouse button presses and respond to them."""
        for row in self.cells:
            for cell in row:
                cell_clicked = cell.rect.collidepoint(mouse_pos)
                # Only flag closed cells.
                if cell_clicked and cell.state != 0:
                    if cell.state == 1:
                        self.stats["mines_left"] -= 1
                    elif cell.state == -1:
                        self.stats["mines_left"] += 1
                    cell.flag_cell(self.cells)

    def _update_screen(self):
        """Update all the elements on the screen."""
        # Fill the background.
        self.screen.fill(self.settings.background_colour)
        # Draw cells to the screen.
        self._draw_cells()
        # Draw button to the screen.
        self.emoji_button.draw_button()
        # Update the screen.
        pygame.display.update()

    def _create_cell(self, cell_x, cell_y, row_number):
        """Create one cell and add it to cells group."""
        cell = Cell(self)
        cell.rect.x = cell_x
        cell.rect.y = cell_y
        self.cells[row_number].append(cell)

        # Set cell's row and column attributes.
        cell.column = self.cells[row_number].index(cell)
        cell.row = row_number

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
        # Create a temporary list of all cells.
        temp_cells = []
        for row in self.cells:
            for cell in row:
                temp_cells.append(cell)

        # Create a list of random indexes.
        mines_indexes = []
        for _ in range(self.settings.mines):
            mines_indexes.append(random.randint(0, len(temp_cells) - 1))

        # Assign mines.
        for index in mines_indexes:
            temp_cells[index].status = -1

    def _calculate_all_neighbours(self):
        """Calculate neighbours of all the cells."""
        for row in range(self.settings.cells_y):
            for column in range(self.settings.cells_x):
                # Stop calculating if cell has a mine.
                if self.cells[row][column].status == 0:
                    self._check_neighbours(row, column)

    def _check_neighbours(self, row, column):
        """Calculate neighbours of a given cell."""
        mines = 0
        cell_x = []
        cell_y = []
        # Go through all coordinates,
        # if they are good, add them to lists of coordinates.
        for p_value in range(column - 1, column + 2):
            if 0 <= p_value < self.settings.cells_x:
                cell_x.append(p_value)
        for q_value in range(row - 1, row + 2):
            if 0 <= q_value < self.settings.cells_y:
                cell_y.append(q_value)

        # Check every cell and add 1 to mines if it has a mine.
        for x_value in cell_x:
            for y_value in cell_y:
                if self.cells[y_value][x_value].status == -1:
                    mines += 1

        # Change cell's status according
        # to number of mines around it.
        self.cells[row][column].status = mines

    def _update_time(self):
        """Update game."""
        self.clock.tick(self.settings.game_framerate)
        if self.stats["state"] == 0:
            self.stats["time_float"] += 1 / self.settings.game_framerate
            self.stats["time"] = int(self.stats["time_float"])

    def _reset_game(self):
        """Reset game to its starting state."""
        # Remove all cells from list and recreate the grid and mines.
        self.cells.clear()
        self._create_grid()
        self._create_mines()
        self._calculate_all_neighbours()

        # Reset stats
        self.stats = {
            "state": 2,
            "mines_left": self.settings.mines,
            "time": 0,
            "time_float": 0
        }

        # Reset emoji to the normal one
        self.emoji_button.current_emoji = 1


if __name__ == "__main__":
    minesweeper = Minesweeper()
    minesweeper.run_game()
