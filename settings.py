"""Module with all the settings for Minesweeper."""


class Settings:
    """Class to handle game settings."""

    def __init__(self):
        """Initialize game settings."""

        # Game framerate
        self.game_framerate = 60

        # Background colour
        self.background_colour = (192, 192, 192)

        # Game mechanics settings
        self.scale = 3
        self.mines = 8
        self.cells_x = 8
        self.cells_y = 8
        self.cell_size = 16 * self.scale
        self.emoji_size = 26 * self.scale

        # Screen settings
        self.side_margin = 12 * self.scale
        self.top_margin = 55 * self.scale
        self.inner_margin = 3 * self.scale
        self.screen_width = (self.cells_x * self.cell_size
                             + 2*self.side_margin)
        self.screen_height = (self.cells_y * self.cell_size
                              + self.side_margin + self.top_margin)
