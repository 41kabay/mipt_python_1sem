import pygame
from pygame.draw import *
from random import randint

pygame.init()

FPS = 30
H = 800
W = 1000

screen = pygame.display.set_mode((W, H))
Rslt = 0
Time = 1500

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]
n = 5


def new_ellipse():
    global x_e, y_e, r_e
    x_e = randint(100, 1100)
    y_e = randint(100, 800)
    r_e = randint(30, 50)
    vx_e = randint(-10, 10)
    vy_e = randint(-10, 10)
    color_e = COLORS[randint(0, 5)]
    return x_e, y_e, r_e, color_e, vx_e, vy_e


def new_ball():
    global x, y, r
    x = randint(100, 1100)
    y = randint(100, 800)
    r = randint(30, 50)
    vx = randint(-10, 10)
    vy = randint(-10, 10)
    color = COLORS[randint(0, 5)]
    return x, y, r, color, vx, vy


def draw_ellipse(ellipse):
    x, y, r, color, vx, vy = ellipse
    circle(screen, color, (x, y), r)
    circle(screen, (255, 255, 255), (x, y), r - 5)


def draw_ball(ball):
    x, y, r, color, vx, vy = ball
    circle(screen, color, (x, y), r)


def move_ellipse(ellipse):
    x, y, r, color, vx, vy = ellipse
    x += vx
    y += vy

    if x <= 0 + r or x >= W - r:
        vx *= -1
    if y <= 0 + r or y >= H - r:
        vy *= -1

    return x, y, r, color, vx, vy


def move_ball(ball):
    x, y, r, color, vx, vy = ball
    x += vx
    y += vy

    if x <= 0 + r or x >= W - r:
        vx *= -1
    if y <= 0 + r or y >= H - r:
        vy *= -1

    return x, y, r, color, vx, vy


def is_clicked(event, ball):
    x, y, r, color, vx, vy = ball
    e_x, e_y = event.pos
    for i in range(n):
        if ((e_x - x) ** 2 + (e_y - y) ** 2 <= r ** 2):
            return 1
    return 0


def check_Time(Time):
    if Time <= 0:
        add_Rslt("best_score.txt", Rslt)
        pygame.quit()
        exit()


def add_Rslt(input_filename, Rslt):
    Rslts = []
    with open(input_filename) as input_file:
        for line in input_file:
            Rslts.append(int(line))
    Rslts.append(Rslt)
    Rslts.sort(reverse=True)
    with open(input_filename, 'w') as out_file:
        for res in Rslts[:10]:
            print("%d" % (res), file = out_file)


pygame.display.update()
clock = pygame.time.Clock()
finished = False
balls = []
ellipses = []
for i in range(n):
    balls.append(new_ball())
    ellipses.append(new_ellipse())

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for i, ball in enumerate(balls):
                if is_clicked(event, ball):
                    Rslt += 1
                    print(Rslt)
                    balls[i] = new_ball()
            for i, ellipse in enumerate(ellipses):
                if is_clicked(event, ellipse):
                    Rslt += 5
                    print(Rslt)
                    ellipses[i] = new_ellipse()
    for i, ball in enumerate(balls):
        Time -= 1
        balls[i] = move_ball(ball)
        draw_ball(ball)
        check_Time(Time)
    for i, ellipse in enumerate(ellipses):
        Time -= 1
        ellipses[i] = move_ellipse(ellipse)
        draw_ellipse(ellipse)
        check_Time(Time)
    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()



