from Engine.GameObject import GameObject
import pygame
import sys

BLACK = (0,0,0)
isDebug = True

pygame.init()
pygame.display.set_caption("Тестируем GameObject")

screen = pygame.display.set_mode((800, 600))
objects = []


cube = GameObject(0,0,64,64)


def Start():
    objects.append(cube)

def Main():
    pass

def Update():

    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    for gameObject in objects:
        gameObject.Update(screen)
    

    pygame.time.Clock().tick(60)
    pygame.display.update()