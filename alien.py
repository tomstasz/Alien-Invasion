import pygame
from pygame.sprite import Sprite  # sprite do obsługi wielu poruszających się elementów


class Alien(Sprite):

    def __init__(self, ai_settings, screen):
        super().__init__()     # dziedziczenie po klasie Sprite
        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width  # pozycja 'startowa' oddalona o jeden 'wymiar' aliena od góry i boku ekranu
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)  # uściślenie pozycji aliena

    def blitme(self):
        self.screen.blit(self.image, self.rect)  # narysuj aliena na ekranie w jego aktualnej pozycji

    def update(self):
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)  # * fleet_direction (1/-1)
        self.rect.x = self.x

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

