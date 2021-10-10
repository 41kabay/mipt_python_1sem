import pygame
from pygame.draw import *

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (154, 154, 154)
LIGHT_BLUE = (64, 128, 255)
GREEN = (222, 234, 176)
YELLOW = (28, 39, 0)
PINK = (230, 50, 230)
RED = (201, 52, 52)

pygame.init()

FPS = 30
screen = pygame.display.set_mode((800, 1200))

rect(screen, (0, 28, 39),(0, 0, 800, 600))
rect(screen, YELLOW, (0, 600, 800, 600))
ellipse(screen, (48, 48, 48), (200, 400, 600, 80))
polygon(screen, WHITE, [[25, 730], [120, 510], 
                     [220, 510], [350, 740]])
ellipse(screen, GRAY, (0, 400, 350, 115))
ellipse(screen, (205, 205, 205), (35, 390, 270, 90))
ellipse(screen, WHITE, (20, 455, 40, 18))
ellipse(screen, WHITE, (60, 475, 40, 18))
ellipse(screen, WHITE, (120, 485, 40, 18))
ellipse(screen, WHITE, (190, 485, 40, 18))
ellipse(screen, WHITE, (240, 475, 40, 18))
ellipse(screen, WHITE, (300, 455, 40, 18))
circle(screen, WHITE, (500, 260), 100)
circle(screen, RED, (650, 775), 22)
ellipse(screen, GREEN, (620, 796, 30, 13))
ellipse(screen, GREEN, (590, 775, 35, 25))
circle(screen, GREEN, (585, 778),17)
ellipse(screen, GREEN, (530, 765, 45, 110))
circle(screen, GREEN, (530, 770),15)
ellipse(screen, GREEN,(500, 778, 24, 15))
ellipse(screen, GREEN,(495, 795, 9, 14))
ellipse(screen, GREEN,(520, 835, 25, 45)) 
ellipse(screen, GREEN,(513, 875, 20, 40))
circle(screen, GREEN,(502, 905), 12)
ellipse(screen, GREEN,(560, 835, 25, 45))
ellipse(screen, GREEN,( 570, 875, 20,40))
circle(screen, GREEN,( 598, 915),13)

polygon(screen, GREEN, ([510,690],[520,740],[540,760],[570,760],[587,740],[605,690]))
circle(screen, BLACK, (540, 720), 15)
circle(screen, BLACK, (580, 720), 12)
circle(screen, WHITE, (545, 720), 3)
circle(screen, WHITE, (585, 720), 3)
ellipse(screen,GREEN,(507,675,10,15))
ellipse(screen, GREEN,(495, 659, 14, 22))
ellipse(screen, GREEN,( 475, 652, 21, 11))
ellipse(screen, GREEN,(470, 635, 26, 17))
ellipse(screen, GREEN,( 605, 680, 14,15))
ellipse(screen, GREEN,(610, 672, 12, 19))
circle(screen, GREEN,( 622, 665),7)
ellipse(screen, GREEN,( 630,645,12 ,10))
ellipse(screen, GREEN,( 645, 645, 14, 24))

line(screen, BLACK,[675,725],[650,750],2)
polygon(screen, (128,160,0),([660,740],[650,730],[655,720],[660,740]))

ellipse(screen, (102,102,102), (-100, 100, 700, 150))
ellipse(screen, (102,102,102), (-100, 250, 600, 100))
ellipse(screen, (102,102,102), (400, 300, 600, 100))
ellipse(screen, (102,102,102), (500, 100, 600, 170))

ellipse(screen, (48, 48, 48), (-300, 270, 600, 100))
ellipse(screen, (48, 48, 48), (200, 200, 700, 70))
#ellipse(screen, WHITE, 
#polygon(screen, (255, 255, 0), [(100,100), (200,50),
#                               (300,100), (100,100)])
#polygon(screen, (0, 0, 255), [(100,100), (200,50),
#                               (300,100), (100,100)], 5)
#circle(screen, (0, 255, 0), (200, 175), 50)
#circle(screen, (255, 255, 255), (200, 175), 50, 5)
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
