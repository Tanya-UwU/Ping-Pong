from pygame import *
font.init()

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

# текст
font = font.Font(None, 50)
lose1 = font.render('PLAYER_L LOSE!', True, (180,0,0))
lose2 = font.render('PLAYER_R LOSE!', True, (180,0,0))

# игроки
player_l = Player('pin3.png', 20, 300, 120, 120, 10)
player_r = Player('test2.png', 460, 300, 120, 120, 10)
ball = Player('ball.png', 300, 300, 90, 90, 8)

# игровой цикл
run = True
finish = False

speed_x = 3
speed_y = 3

win_height = 600

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

        ball.reset()      

        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if ball.rect.y > win_height - 50 or ball.rect.y < 0:
            speed_y *= -1

        if sprite.collide_rect(player_l, ball) or sprite.collide_rect(player_r, ball):
            speed_x *= -1

        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (250,300))

        if ball.rect.x > 595:
            finish = True
            window.blit(lose2, (250,300))

        display.update()

    clock.tick(FPS)

    # этот комментарий удалят :)