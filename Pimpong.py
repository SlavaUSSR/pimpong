from pygame import *
from random import randint

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, size_x, size_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys_pressed[K_DOWN] and self.rect.x < win_wigth - 105:
            self.rect.x += self.speed

    def fire(self):
        pass

back = (200, 255, 255)
win_wigth = 1920
win_height = 1080
window = display.set_mode((win_wigth, win_height))
window.fill(back)

game = True
finish = False
clock = time.Clock()
FPS = 60

racket1 = Player('pngwing.png', 30, 200, 4, 50, 150)
racket2 = Player('pngwing.png', 520, 200, 4, 50, 150)
ball = GameSprite('tennis.png', 200, 200, 4, 50,150)
display.set_caption('Pimpong')

font.init()
font = font.font(None,35)
lose1 = font.render(Player_X)
lose2 = font.render(Player_X )

speed_x = 3
speed_y = 3

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        window.fill(back)
        racket1.update_l()
        racket2.update_r()
        ball.rect.x += speed_x
        ball.rect.y += speed_y

if sprite.collide_rect((racket1, ball)) or sprite.collide_rect(racket2, ball):

    racket1.reset()
    racket2.reset()
    ball.reset()

    display.update()
    clock.tick(FPS)