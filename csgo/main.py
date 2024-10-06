import pygame, os
from scripts.player import Player


flags = pygame.RESIZABLE | pygame.SCALED
window = pygame.display.set_mode((600, 800), flags)
clock = pygame.time.Clock()

FPS = 60

background = pygame.image.load(os.path.abspath("images\\background.png"))
spacescipe = pygame.image.load("images\\spaceship.png")
player = Player(400, 550, spacescipe, 3)

ufo = pygame.image.load("images\\UFOsprite.gif")
bullet = pygame.image.load("images\\bullet.png")


game = True
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    player.update()

    window.blit(background, (0, 0))
    player.render(window)
    pygame.display.update()
    clock.tick(FPS)