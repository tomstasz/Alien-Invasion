
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group


def run_game():

    pygame.init()  # zainicjowanie gry
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))  # stworzenie obiektu ekranu (surface)
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(ai_settings, screen)
    bullets = Group()  # tworzy listę sprite'ów. Tworzymy przed petlą, żeby nie zawieszać ciągłym generowaniem obiektów
    aliens = Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)

    while True:  # Start głównej pętli dzaiłania gry
        gf.check_events(ai_settings, screen, ship, bullets)   # sprawdza input gracza
        ship.update()                                         # upadte pozycji statku
        gf.update_bullets(ai_settings, screen, ship, aliens, bullets)                            # update wystrzelonych pocisków
        gf.update_aliens(ai_settings, ship, aliens)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)  # na końcu używamy tych update'ów do update ekranu


run_game()


