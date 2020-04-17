import pygame
pygame.init()
 
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
PI = 3.141592653
 
size = (400, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Text Examples")
 
done = False
clock = pygame.time.Clock()
 
text_rotate_degrees = 0
 
while not done:
 
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
            done = True  
 
    screen.fill(WHITE)
 
    pygame.draw.line(screen, BLACK, [100,50], [200, 50])
    pygame.draw.line(screen, BLACK, [100,50], [100, 150])
 
    font = pygame.font.SysFont('Calibri', 25, True, False)
 
    text = font.render("Sideways text", True, BLACK)
    text = pygame.transform.rotate(text, 90)
    screen.blit(text, [0, 0])
 
    text = font.render("Upside down text", True, BLACK)
    text = pygame.transform.rotate(text, 180)
    screen.blit(text, [30, 0])
 
    text = font.render("Flipped text", True, BLACK)
    text = pygame.transform.flip(text, False, True)
    screen.blit(text, [30, 20])
 
    text = font.render("Rotating text", True, BLACK)
    text = pygame.transform.rotate(text, text_rotate_degrees)
    text_rotate_degrees += 1
    screen.blit(text, [100, 50])
 
    pygame.display.flip()

    clock.tick(60)

pygame.quit()
