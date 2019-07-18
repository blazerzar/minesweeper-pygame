"""Module with Scoreboard class for Minesweeper."""

import pygame.font


class Scoreboard:
    """Class to represent a scoreboard."""

    def __init__(self, minesweeper):
        """Initialize scoreboard attributes."""
        self.minesweeper = minesweeper
        self.screen = minesweeper.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = minesweeper.settings

        # Font settings
        self.font_colour = (30, 30, 30)
        font_size = 32 * self.settings.scale
        self.font = pygame.font.SysFont(None, font_size)

        # Prepare the initial images
        self.prep_time()
        self.prep_mines()

    def prep_time(self):
        """Turn time into a rendered image."""
        time = self.minesweeper.stats["time"]
        time_str = str(time)
        self.time_image = self.font.render(
            time_str, True, self.font_colour, self.settings.background_colour)

        # Display time to the right of the emoji.
        self.time_rect = self.time_image.get_rect()
        self.time_rect.centery = self.minesweeper.emoji_button.rect.centery
        self.time_rect.x = (self.settings.screen_width
                            - self.settings.side_margin
                            - self.time_rect.width)

    def prep_mines(self):
        """Turn mines_left into a rendered image."""
        mines_left = self.minesweeper.stats["mines_left"]
        mines_left_str = str(mines_left)
        self.mines_left_image = self.font.render(
            mines_left_str, True, self.font_colour,
            self.settings.background_colour)

        # Display mines left to the left of the emoji.
        self.mines_left_rect = self.mines_left_image.get_rect()
        self.mines_left_rect.centery = (
            self.minesweeper.emoji_button.rect.centery)
        self.mines_left_rect.x = self.settings.side_margin

    def show_scoreboards(self):
        """Draw time and mines left scoreboards to the screen."""
        self.screen.blit(self.time_image, self.time_rect)
        self.screen.blit(self.mines_left_image, self.mines_left_rect)
