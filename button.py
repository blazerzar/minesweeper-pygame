"""Module with Button class for Minesweeper."""

import os

import pygame


class Button:
    """Class to represent a button."""

    def __init__(self, minesweeper):
        """Initialize button attributes."""

        self.screen = minesweeper.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = minesweeper.settings

        # Load images of emoji button
        # Normal emoji ... 1
        self.image_emoji = pygame.image.load(os.path.join(
            minesweeper.my_path, "images/emoji.bmp"))
        self.image_emoji = pygame.transform.scale(
            self.image_emoji,
            (self.settings.emoji_size, self.settings.emoji_size))
        self.rect = self.image_emoji.get_rect()

        # Emoji dead ... 0
        self.image_emoji_dead = pygame.image.load(os.path.join(
            minesweeper.my_path, "images/emoji_dead.bmp"))
        self.image_emoji_dead = pygame.transform.scale(
            self.image_emoji_dead,
            (self.settings.emoji_size, self.settings.emoji_size))

        # Emoji solved ... 2
        self.image_emoji_solved = pygame.image.load(os.path.join(
            minesweeper.my_path, "images/emoji_solved.bmp"))
        self.image_emoji_solved = pygame.transform.scale(
            self.image_emoji_solved,
            (self.settings.emoji_size, self.settings.emoji_size))

        # Emoji o ... -1
        self.image_emoji_o = pygame.image.load(os.path.join(
            minesweeper.my_path, "images/emoji_o.bmp"))
        self.image_emoji_o = pygame.transform.scale(
            self.image_emoji_o,
            (self.settings.emoji_size, self.settings.emoji_size))

        # Set button location
        self.rect.x = (self.settings.screen_width - self.rect.width) / 2
        self.rect.y = self.settings.side_margin + self.settings.inner_margin

        self.current_emoji = 1

    def draw_button(self):
        """Draw the button to the screen."""
        if self.current_emoji == 1:
            self.screen.blit(self.image_emoji, self.rect)
        elif self.current_emoji == 0:
            self.screen.blit(self.image_emoji_dead, self.rect)
        elif self.current_emoji == 2:
            self.screen.blit(self.image_emoji_solved, self.rect)
        elif self.current_emoji == -1:
            self.screen.blit(self.image_emoji_o, self.rect)
