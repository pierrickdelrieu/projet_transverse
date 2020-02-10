import pygame as pg


class Player(pg.sprite.Sprite):
    fuel: int
    speed = 5
    bounce = 50
    gun_offset = -11
    images = []

    def __init__(self, screen_rect):
        pg.sprite.Sprite.__init__(self, self.containers)
        self.screen_rect = screen_rect

        self.image = self.images[0]

        self.rect = self.image.get_rect(midbottom=self.screen_rect.midright)
        self.origtop = self.rect.top
        self.facing = -1

    def move(self, direction):
        if direction:
            self.facing = direction
        self.rect.move_ip(direction * self.speed, 0)
        self.rect = self.rect.clamp(self.screen_rect)
        if direction < 0:
            self.image = self.images[0]
            self.fuel -= 1
        elif direction > 0:
            self.image = self.images[1]
            self.fuel -= 1
        self.rect.top = self.origtop - (self.rect.left // self.bounce % 2)


class Cannon(pg.sprite.Sprite):
    angle = 0
    speed = 5
    bounce = 50
    gun_offset = -11
    images = []

    def __init__(self, screen_rect):
        pg.sprite.Sprite.__init__(self, self.containers)
        self.screen_rect = screen_rect

        self.image = self.images[0]

        self.rect = self.image.get_rect(midbottom=self.screen_rect.midright)

        self.origtop = self.rect.top
        self.facing = -1

    def move(self, direction):
        if direction:
            self.facing = direction

        self.rect.move_ip(direction * self.speed, 0)
        self.rect = self.rect.clamp(self.screen_rect)

        if direction < 0:
            self.image = self.images[0]
        elif direction > 0:
            self.image = self.images[1]

        self.rect.top = self.origtop - (self.rect.left // self.bounce % 2)

    def rotate(self, angle):
        self.angle += angle
        self.image = pg.transform.rotate(self.image, -self.angle)


class Fuel(pg.sprite.Sprite):
    fuel: int
    speed = 5
    images = []

    def __init__(self, screen_rect):
        pg.sprite.Sprite.__init__(self, self.containers)
        self.screen_rect = screen_rect

        self.image = self.images[0]

        self.rect = self.image.get_rect(
            midbottom=(self.screen_rect.midright[0], self.screen_rect.midright[1] - 30)
        )

        self.font = pg.font.Font(None, 20)
        self.font.set_bold(True)
        self.color = pg.Color('Green')

    def move(self, direction, fuel):
        self.rect.move_ip(direction * self.speed, 0)
        self.rect = self.rect.clamp(self.screen_rect)

        self.fuel = fuel
        if self.fuel == 0:
            self.font.set_underline(True)

        if self.fuel < 10:
            self.color = pg.Color('Red')
        elif self.fuel < 50:
            self.color = pg.Color('Orange3')
        elif self.fuel < 75:
            self.color = pg.Color('Orange')
        self.update()

    def update(self):
        self.image = self.font.render(f"Fuel: {self.fuel}%", 0, self.color)
