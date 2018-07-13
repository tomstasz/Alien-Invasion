import pygame


class Ship:

    def __init__(self, ai_settings, screen):
        self.screen = screen
        self.ai_settings = ai_settings
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()  # pobranie pozycji 'kwadratu'(rectangle) statku
        self.screen_rect = screen.get_rect()   # pobranie pozycji 'kwadratu' ekranu

        self.rect.centerx = self.screen_rect.centerx  # startowa pozycja statku (oś X, środek ekranu)
        self.rect.bottom = self.screen_rect.bottom  # startowa pozycja statku (oś Y, dół ekranu)
        self.center = float(self.rect.centerx)

        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor  # przesuwamy statek w prawo o wartość z settings.py
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor  # było self.rect.centerx -= 1
        self.rect.centerx = self.center  # updatujemy rect po zmianach eventowych

    def blitme(self):
        self.screen.blit(self.image, self.rect)  # rysuj statek na ekranie w jego obecnym położeniu (self.rect)
        # 'kwadrat' statku ma się 'nakładać' z 'kwadratem' ekranu (obrazek wyswietlany w aktualnej pozycji po eventach)




