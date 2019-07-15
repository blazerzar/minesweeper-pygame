"""The main file with all the logic for Minesweeper"""

import sys
import os

import pygame


class Minesweeper:
    """Class to handle running the game."""

    def __init__(self):
        """Initialize pygame and game resources."""
        pygame.init()
        self.screen = pygame.display.set_mode()