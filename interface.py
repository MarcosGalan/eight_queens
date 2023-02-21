import time

import pygame
from ocho_damas import *

tablero_loc = ocho_reinas(tablero)

pygame.init()

ROWS = 8
PIXELS = 112
WIDTH = PIXELS * ROWS
SIZE = (WIDTH + 56, WIDTH + 56)

pantalla = pygame.display.set_mode(SIZE)
pantalla.fill((255, 255, 255))

fondo = pygame.image.load('tablero.png')
fondo = pygame.transform.scale(fondo, SIZE)

dama = pygame.image.load('dama_img.png')
dama = pygame.transform.scale(dama, (106, 106))

print(tablero_loc)
run = True
while run:
    pantalla.blit(fondo, (0, 0))
    for pos_row, row in enumerate(tablero_loc):
        for pos_element, element in enumerate(row):
            if element == 'o':
                pantalla.blit(dama, (106 * pos_row+54, 106 * pos_element+52))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if pygame.mouse.get_pressed()[0]:
        mouse_pos = pygame.mouse.get_pos()
        print(mouse_pos)

    pygame.display.update()
