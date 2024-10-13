import pygame

flags = pygame.RESIZABLE | pygame.SCALED
window = pygame.display.set_mode((600, 800), flags)
clock = pygame.time.Clock

fps = 60

background = pygame.image.load("images\\background.jfif")
spacescipe = pygame.image.load("images\\spaceship.png")
ufo = pygame.image.load("images\\UFOsprite.gif")
bullet = pygame.image.load("images\\bullet.png")

game = True
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    window.blit(background, (0, 0))
    pygame.display.update()
    clock.tick(FPS)