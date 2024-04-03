import pygame
pygame.init()
screen=pygame.display.set_mode((600,800))
while True:
    screen.fill("purple")
    pygame.draw.rect(screen,"pink",(40,70,100,300))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
    pygame.display.update()