import pygame, os
from scripts.player import Player
from scripts.functions import load_image
from scripts.bullet import Bullet

flags = pygame.RESIZABLE | pygame.SCALED
window = pygame.display.set_mode((600, 800), flags)
clock = pygame.time.Clock()

FPS = 60

background = load_image(os.path.abspath("images\\background.png"), (600, 800), None)
spacescipe_image = load_image("images\\spaceship.png", (50, 50), None)
bullet_image = load_image("images\\bullet.png", (30, 30), None)
ufo_image = load_image("images\\UFOsprite.gif", (100, 100), None)

player = Player(400, 550, spacescipe_image, 3)
bullets = list()

game = True
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullets.append(Bullet(player.rect.centerx, player.rect.y, bullet_image, 30))


    player.update()
    for bullet in bullets.copy():
        bullet.update()
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    window.blit(background, (0, 0))
    player.render(window)
    for bullet in bullets:
        bullet.render(window)
    pygame.display.update()
    clock.tick(FPS)