from pygame import * 
wd = display.set_mode((700,500))
background = transform.scale(image.load("background.jpg"), (700,500))
display.set_caption("Maze")
clock = time.Clock()
FPS = 144
mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()
money = mixer.Sound('money.ogg')
kick = mixer.Sound('kick.ogg')
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (55, 55))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x 
        self.rect.y = player_y
    def reset(self):
        wd.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 450:
            self.rect.y += self.speed
        if keys_pressed[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys_pressed[K_RIGHT] and self.rect.x <650:
            self.rect.x += self.speed
class Wall(sprite.Sprite):
    def __init__(self,color_1,color_2,color_3,wall_x,wall_y,wall_width,wall_height):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.widht = wall_width
        self.height = wall_height
        self.stena = Surface((self.widht, self.height))
        self.stena.fill((color_1, color_2, color_3))
        self.rect = self.stena.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        wd.blit(self.stena,(self.rect.x, self.rect.y))
class Enemy(GameSprite):
    direction = 'left'
    def update(self):
        if self.rect.x <= 500:
            self.direction = 'right'
        if self.direction == 'right':
            self.rect.x += self.speed

        if self.rect.x >= 660:
            self.direction = 'left'
        if self.direction == 'left':
            self.rect.x -= self.speed

w1 = Wall(124,252,0, 100, 20, 480, 10)
w2 = Wall(124,252,0, 100, 20, 10, 355)
w3 = Wall(124,252,0, 70, 480, 430, 10)
w4 = Wall(124,252,0, 210, 105, 10, 380)
w5 = Wall(124,252,0, 320, 20, 10, 350)
w6 = Wall(124,252,0, 490, 130, 10, 350)
w7 = Wall(124,252,0, 410, 120, 150, 10)
player = Player('hero.png', 10, 390, 4)
enemy = Enemy('cyborg.png', 500, 250, 3)
gold = GameSprite('treasure.png', 615, 415, 0)
game = True
finish = False
font.init()
font = font.SysFont('Arial', 80)
win = font.render('YOU WIN!', True, (255, 215, 0))
lose = font.render('YOU LOSE!', True, (0, 0, 0))
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        wd.blit(background,(0, 0))
        player.update()
        enemy.update()
        gold.reset()
        enemy.reset()
        player.reset()
        w1.draw_wall()
        w2.draw_wall()
        w3.draw_wall()
        w4.draw_wall()
        w5.draw_wall()
        w6.draw_wall()
        w7.draw_wall()
        if sprite.collide_rect(player, gold):
            finish = True
            money.play()
            wd.blit(win, (200, 200))
        if sprite.collide_rect(player, enemy) or sprite.collide_rect(player, w1) or sprite.collide_rect(player, w2) or sprite.collide_rect(player, w3) or sprite.collide_rect(player, w4) or sprite.collide_rect(player, w5) or sprite.collide_rect(player, w6) or sprite.collide_rect(player, w7):
            finish = True
            kick.play()
            wd.blit(lose, (100, 200))
        display.update()
    else:
        finish = False
        player = Player('hero.png', 10, 390, 4)
        time.delay(2000)
    clock.tick(FPS)

    