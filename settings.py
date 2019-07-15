"""Module with all the settings for Minesweeper."""


class Settings:
    """Class to handle game settings."""

    def __init__(self):
        """Initialize game settings."""
        self.mines = 10
        self.cells_x = 8
        self.cells_y = 8