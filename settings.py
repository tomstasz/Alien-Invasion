

class Settings:

    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)  # kolor tła (w pygame tylko jako RGB)
        self.ship_speed_factor = 1.5
        self.ship_limit = 2
        self.bullet_speed_factor = 3
        self.bullet_width = 3   # zmiana parametrów (np. szerokości pocisku) może ułatwić testowanie np. pustego ekranu
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3   # ustalamy maksymalną liczbę pocisków na ekranie, żeby zachęcić do celnego strzelania
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10  # wartość o jaką obniża się cały rząd alienów
        self.fleet_direction = 1  # 1 lub -1 determinuje kierunek przesuwania się alienów (prawo/lewo)

