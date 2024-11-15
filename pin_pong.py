from pygame import *

window = display.set_mode((600,600))
display.set_caption('ping-pong')

# класс
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_wight, player_hight, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (player_wight, player_hight))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 500:
            self.rect.y += self.speed
            
    def update_r(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 500:
            self.rect.y += self.speed


# время 
clock = time.Clock()
FPS = 60

# задний фон игры
background = transform.scale(image.load('artacktida2.jpeg'), (600, 600))

# игроки
player_l = Player('pin3.png', 20, 300, 120, 120, 10)
player_r = Player('test2.png', 460, 300, 120, 120, 10)

# игровой цикл
run = True
finish = False

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False

    if finish != True:
        
        window.blit(background, (0,0))

        player_l.reset()
        player_l.update_l()

        player_r.reset()
        player_r.update_r()        

        display.update()

    clock.tick(FPS)

    # этот комментарий удалят :)