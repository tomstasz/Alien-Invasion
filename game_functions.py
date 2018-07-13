import sys  # sys używamy do wychodzenia z programu
import pygame


def check_events(ship):
    for event in pygame.event.get():  # pętla do wykrywania eventów myszy i klawiatury
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship)     # rozbicie check_events na mniejsze moduły
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def check_keydown_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True


def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def update_screen(ai_settings, screen, ship):
    screen.fill(ai_settings.bg_color)  # wypełnia ekran kolorem przy każdym przejściu pętli
    ship.blitme()
    pygame.display.flip()  # pokazujemy ostatnie rysowanie ekranu
