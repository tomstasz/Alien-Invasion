import sys  # sys używamy do wychodzenia z programu
import pygame
from bullet import Bullet
from alien import Alien


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


def update_screen(ai_settings, screen, ship, aliens, bullets):
    screen.fill(ai_settings.bg_color)  # wypełnia ekran kolorem przy każdym przejściu pętli
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()                      # blitme powoduje pojawienie się obiektu na ekranie
    aliens.draw(screen)  # draw na grupie to rysowanie każdego elem. wg. jego parametru rect (w tym wypadku na ekranie)
    pygame.display.flip()  # pokazujemy ostatnie rysowanie ekranu


def update_bullets(ai_settings, screen, ship, aliens, bullets):
    bullets.update()  # uruchamia bullet.update() dla każdego pocisku z grupy
    check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets)
    for bullet in bullets.copy():  # tworzymy kopię bullets, bo nie powinno się usuwać w pętli z listy oryginalnej
        if bullet.rect.bottom <= 0:  # usuwamy z pamięci komputera pociski, które opuściły ekran
            bullets.remove(bullet)
            # print(len(bullets))   print po to, żeby wiedzieć, czy pociski faktycznie znikają poza ektranem,
            # potem do usunięcia, żeby nie spowalniał gry


def fire_bullet(ai_settings, screen, ship, bullets):  # wyciągnięte z check_keydown_events dla uproszczenia kodu
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets):
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)  # sprawdzamy kolizję dwóch grup, powstaje
    # słownik trafionych {bullet: alien}, True mówi czy kasować dany obiekt po wykryciu kolizji
    if len(aliens) == 0:
        bullets.empty()  # matoda empty usuwa wszystkie sprite'y grupy, które pozostały
        create_fleet(ai_settings, screen, ship, aliens)


def create_fleet(ai_settings, screen, ship, aliens):
        alien = Alien(ai_settings, screen)
        number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)  # pobieramy współrzędne szerokości
        number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                create_alien(ai_settings, screen, aliens, alien_number, row_number)


def get_number_aliens_x(ai_settings, alien_width):
    available_space_x = ai_settings.screen_width - 2 * alien_width  # wyliczamy dostępną przestrzeń ekranu
    number_aliens_x = int(available_space_x / (2 * alien_width))  # możliwa liczba alienów (int zaokrągla do pełnych)
    return number_aliens_x


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    alien = Alien(ai_settings, screen)  # tworzymy instancję aliena, zebu pobrać jego wymiary (nie będzie we flocie)
    alien_width = alien.rect.width  # pobieramy width z recta aliena
    alien.x = alien_width + (2 * alien_width) * alien_number  # kolejne alieny o szerokość od brzegu,
    alien.rect.x = alien.x  # razy rezerwacja miejsca razem z przerwą pomiędzy, razy pozycja w rzędzie
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number  # w dół od drugiego (pierwszy rząd = numer 0)
    aliens.add(alien)  # powstający rząd 'wypycha' się w prawo, aż osiągnie brzeg ekranu


def get_number_rows(ai_settings, ship_height, alien_height):
    available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))  # int, bo nie chcemy 'częściowych' rzędów
    return number_rows


def update_aliens(ai_settings, ship, aliens):
    check_fleet_edges(ai_settings, aliens)  # najpierw sprawdzamy, czy brzeg, dopiero potem updateujemy pozycje
    aliens.update()    # metoda update na grupie powoduje automatyczne użycie update na każdym alienie
    if pygame.sprite.spritecollideany(ship, aliens):
        print("Ship hit!")


def check_fleet_edges(ai_settings, aliens):
    for alien in aliens.sprites():  # sprawdzamy sprite'y pojedynczych alienów z Group
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break


def change_fleet_direction(ai_settings, aliens):
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed  # obniżamy cały rząd zwiększając y
    ai_settings.fleet_direction *= -1  # zmieniamy kierunek ruchu mnożąc przez -1 (odwraca się znak)
