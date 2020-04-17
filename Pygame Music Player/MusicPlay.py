import pygame, sys
from pygame.locals import *
pygame.init()

screen = pygame.display.set_mode((640, 480))
screen.fill((0, 0, 0, 255))
pygame.display.set_caption("Pygame Music Player")

pygame.mixer.music.load("Superman.mp3")
print("Superman The Movie Theme!")
print("Loading Music...")
pygame.mixer.music.play(-1, 0.0)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
