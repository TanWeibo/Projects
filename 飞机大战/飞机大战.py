import random
import pygame
import tkinter.messagebox as message

try:
    file = open('H:/Projects/飞机大战/plug-in.plug-file', 'r')
    words = file.read()
    file.close()
    if words == 'True':
        外挂 = True
    else:
        外挂 = False
except Exception:
    外挂 = False
FPS = 60
WIDTH = 500
HEIGHT = 600
pygame.display.set_caption('飞机大战')
background_color = (0, 0, 0)
self_color = (0, 255, 0)
Rock_color = (255, 0, 0)
Bullet_color = (255, 255, 0)
text_color = (255, 255, 255)
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
set_FPS = pygame.time.Clock()

font_name = pygame.font.match_font('C:/Windows/Fonts/方正粗黑宋简体.ttf')


def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, text_color)
    text_rect = text_surface.get_rect()
    text_rect.centerx = x
    text_rect.top = y
    surf.blit(text_surface, text_rect)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 40))
        self.image.fill(self_color)

        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 20
        self.speedx = 8

    def update(self):
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_RIGHT]:
            self.rect.x += self.speedx
        if key_pressed[pygame.K_LEFT]:
            self.rect.x -= self.speedx
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        elif self.rect.left < 0:
            self.rect.left = 0

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.centery)
        all_sprites.add(bullet)
        bullets.add(bullet)


class Rock(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30, 30))
        self.image.fill(Rock_color)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)

        self.speedy = random.randrange(2, 5)
        self.speedx = random.randrange(-3, 3)

    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.top > HEIGHT or self.rect.left > WIDTH or self.rect.right < 0:
            self.rect.x = random.randrange(0, WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)

            self.speedy = random.randrange(2, 15)
            self.speedx = random.randrange(-3, 3)


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 20))
        self.image.fill(Bullet_color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.speedy = -20

    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill()


all_sprites = pygame.sprite.Group()
rocks = pygame.sprite.Group()
bullets = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
for circulate in range(5):
    rock = Rock()
    all_sprites.add(rock)
    rocks.add(rock)
running = True
why_exit = None
while running:
    set_FPS.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            why_exit = 'EXIT'
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot()
            elif event.key == pygame.K_F5:
                message.showinfo('About this', f"""由TanWeibo制作的飞机大战
https://github.com/TanWeibo/Projects/blob/main/飞机大战/飞机大战.py
外挂状态：{外挂}""")
            elif event.key == pygame.K_F6:
                message.showerror('Stop use this option.', '随着exe文件的停止使用\
该也停止使用了，请自行重新运行，Thanks!')
    all_sprites.update()

    hits_rocks_bullet = pygame.sprite.groupcollide(rocks, bullets, True, True)
    for hit in hits_rocks_bullet:
        r = Rock()
        all_sprites.add(r)
        rocks.add(r)

    hits_player_rocks = pygame.sprite.spritecollide(player, rocks, False)
    if not 外挂:
        for hit in hits_player_rocks:
            why_exit = 'LOSE'
            running = False

    screen.fill(background_color)
    all_sprites.draw(screen)
    draw_text(screen, str(screen), 18, WIDTH / 2, 2)
    pygame.display.update()

if why_exit == 'LOSE':
    message.showinfo('LOSE!', '你输了！')
elif why_exit == 'EXIT':
    message.showinfo('THANKS', '谢谢您的使用！！！')
pygame.quit()
