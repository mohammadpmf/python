# all from here:
# mohammadpmf
# https://realpython.com/pygame-a-primer/#sound-effects

# from hashlib import new
import pygame
import random
# from pygame.constants import KEYUP, USEREVENT
# from pygame.display import update
# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
from pygame.locals import RLEACCEL, K_UP, K_DOWN, K_LEFT, K_RIGHT, K_ESCAPE, KEYDOWN, QUIT, K_q

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.image.load('jet.png').convert()
        self.surf = pygame.transform.scale(self.surf, (120, 80))
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        # self.surf = pygame.Surface((75, 25))
        # self.surf.fill((125,245,36))
        self.rect = self.surf.get_rect()
        self.rect.x = 100
        self.rect.y = 40
    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -1)
            move_up_sound.play()
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 1)
            move_down_sound.play()
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-1, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(1, 0)
        
        # Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.surf = pygame.image.load("missile.png").convert()
        self.surf = pygame.transform.scale(self.surf, (60, 30))
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        # self.surf = pygame.Surface((20, 10))
        # self.surf.fill((255, 0, 0))
        # self.surf.fill((random.randint(0,255), random.randint(0,255), random.randint(0,255)))
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT),
            )
        )
        enemy_sound.play()
        self.speed = random.randint(1, 2)
        
    # Move the sprite based on speed
    # Remove the sprite when it passes the left edge of the screen
    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()

# Define the cloud object by extending pygame.sprite.Sprite

# Use an image for a better-looking sprite

class Cloud(pygame.sprite.Sprite):
    def __init__(self):
        super(Cloud, self).__init__()
        self.surf = pygame.image.load("cloud.png")
        self.surf = pygame.transform.scale(self.surf, (100, 100))
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT),
            )
        )
    def update(self):
        self.rect.move_ip(-1, 0)
        if self.rect.right < 0:
            self.kill()

# Setup for sounds. Defaults are good.
'''
pygame.mixer.init() accepts a number of arguments, but the defaults work fine in most cases.
Note that if you want to change the defaults, you need to call pygame.mixer.init() before calling pygame.init().
Otherwise, the defaults will be in effect regardless of your changes.
'''
pygame.mixer.init()


# Initialize pygame
pygame.init()

clock = pygame.time.Clock()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

print(pygame.event.get()) # return a list of all events in the queue
screen.fill((120, 255, 255))
surf = pygame.Surface((200, 70))
surf.fill((0, 120, 120))
rect = surf.get_rect()

ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 250)
ADDCLOUD = pygame.USEREVENT + 2
pygame.time.set_timer(ADDCLOUD, 1000)

player = Player()
enemies = pygame.sprite.Group()
clouds = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# pygame.mixer.music.load("sounds/main.mp3")
# download main sound from 'https://opengameart.org/sites/default/files/dance_field_2.mp3'
pygame.mixer.music.load("sounds/downloaded.mp3")
pygame.mixer.music.set_volume(0.4)
pygame.mixer.music.play(loops=-1)
move_up_sound = pygame.mixer.Sound("sounds/up.mp3")
move_down_sound = pygame.mixer.Sound("sounds/down.mp3")
collision_sound = pygame.mixer.Sound("sounds/end.mp3")
enemy_sound = pygame.mixer.Sound('sounds/missile2.mp3')
move_up_sound.set_volume(0.2)
move_down_sound.set_volume(0.2)
collision_sound.set_volume(1)
enemy_sound.set_volume(0.2)

running = True

while running:
    # screen.blit(surf, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
    # or
    surf_center = (SCREEN_WIDTH-surf.get_width())/2, (SCREEN_HEIGHT-surf.get_height())/2
    # screen.blit(surf, surf_center)
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)
    if pygame.sprite.spritecollideany(player, enemies):
        player.kill()
        move_up_sound.stop()
        move_down_sound.stop()
        collision_sound.play()
        pygame.time.wait(400)
        running = False
    pygame.display.flip()
    clock.tick(300)
    for event in pygame.event.get():
        # Did the user hit a key?
        if event.type == KEYDOWN:
            # Was it the Escape key? If so, stop the loop.
            if event.key == K_ESCAPE:
                running = False
            # elif event.key == K_UP:
            #     print('up')
            # elif event.key == K_q:
            #     print('Q is pressed')
        # Did the user click the window close button? If so, stop the loop.
        elif event.type == QUIT:
            running = False
        # elif event.type == KEYUP:
        #     print(event.key)
        elif event.type == ADDENEMY:
            new_enemy = Enemy()
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)
        elif event.type == ADDCLOUD:
            new_cloud = Cloud()
            clouds.add(new_cloud)
            all_sprites.add(new_cloud)


    pressed_keys = pygame.key.get_pressed()
    player.update(pressed_keys)
    enemies.update()
    clouds.update()
    # screen.fill((120, 255, 255))
    # pygame.time.wait(1)
    screen.fill((135, 206, 250))

pygame.mixer.music.stop()
pygame.mixer.quit()