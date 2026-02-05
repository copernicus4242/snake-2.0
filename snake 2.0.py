#Prva naloga:
from cmath import rect

#naredi pygame program, kjer so na ekranu 4je recti; vsi se premikajo, lahko levo-desno, ali pa gor-dol,
#lahko tudi poševno

#naloga je, da vsakič, ko se dva recta dotakneta, si izmenjata malo barve
#(če je rumen, drug zelen, bo rumen dal malo svoje barve zelenemu in obratno)


#dodatna naloga; ko se recta dotakneta, se odbijeta nazaj v smer iz katere sta prišla

import pygame

pygame.init()
clock = pygame.time.Clock()

canvas = pygame.display.set_mode((900, 900))
canvas_color = "white"
pygame.display.set_caption("Vaja 1")

exit = False

color1 = [255, 0, 0]
color2 = [0, 255, 0]
color3 = [0, 0, 255]
color4 = [255, 0, 255]

rect1 = pygame.Rect(400, 50, 100, 100)
rect2 = pygame.Rect(750, 400, 100, 100)
rect3 = pygame.Rect(50, 400, 100, 100)
rect4 = pygame.Rect(400, 750, 100, 100)

rect1_waiting = False
wait_until = 0

rect1_vel = 1
rect2_vel = 1
rect3_vel = 1
rect4_vel = 1

cooldown_start = 0
cooldown_duration = 800

while not exit:
    clock.tick(400)
    canvas.fill(canvas_color)
    current_time = pygame.time.get_ticks()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True

    now = pygame.time.get_ticks()

    if (rect1.y < 0 or rect1.y > 800) and not rect1_waiting:
        rect1_vel *= -1
        wait_until = now + 4000

    if rect1_waiting and now >= wait_until:
        rect1_waiting = False

    if not rect1_waiting:
        rect1.y += rect1_vel





    pygame.draw.rect(canvas, tuple(color1), rect1)


    pygame.display.update()

pygame.quit()