import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):

    def __init__(self, ai_settings, screen, ship):
        super().__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)  # tworzymy pocisk na (0, 0)
        self.rect.centerx = ship.rect.centerx  # po stworzeniu na (0, 0) ustawiamy pocisk na pozycji statku
        self.rect.top = ship.rect.top  # ustawiamy taki sam top kwadratu pocisku i statku dla iluzji 'strzału'
        self.y = float(self.rect.y)  # robimy floata z kordynatu pionowego, żeby manipulować prędkością pocisku
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        self.y -= self.speed_factor  # (0, 0) to lewy górny róg, więc y zmniejsza się po oddaniu strzału
        self.rect.y = self.y  # update aktualnego recta po strzale

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)  # wypełnia kwadrat ekranu określony w self.rect kolorem

