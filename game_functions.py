import sys  # sys używamy do wychodzenia z programu
import pygame
from bullet import Bullet


def check_events(ai_settings, screen, ship, bullets):
    for event in pygame.event.get():  # pętla do wykrywania eventów myszy i klawiatury
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)   # rozbicie check_events na mniejsze moduły
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:  # dodajemy skrót klawiszowy do wyjścia z gry
        sys.exit()


def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def update_screen(ai_settings, screen, ship, bullets):
    screen.fill(ai_settings.bg_color)  # wypełnia ekran kolorem przy każdym przejściu pętli
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    pygame.display.flip()  # pokazujemy ostatnie rysowanie ekranu


def update_bullets(bullets):  # przekazujemy grupę bullets (stworzona w alien_invasion.py)
    bullets.update()  # uruchamia bullet.update() dla każdego pocisku z grupy
    for bullet in bullets.copy():  # tworzymy kopię bullets, bo nie powinno się usuwać w pętli z listy oryginalnej
        if bullet.rect.bottom <= 0:  # usuwamy z pamięci komputera pociski, które opuściły ekran
            bullets.remove(bullet)
            # print(len(bullets))   print po to, żeby wiedzieć, czy pociski faktycznie znikają poza ektranem,
            # potem do usunięcia, żeby nie spowalniał gry


def fire_bullet(ai_settings, screen, ship, bullets):  # wyciągnięte z check_keydown_events dla uproszczenia kodu
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)
