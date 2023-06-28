import pygame, sys, time
from debug import debug

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

test_rect = pygame.Rect(0, 310, 100, 100)
test_rect_position = test_rect.x
test_speed = 144

previous_time = time.time()

while True:
    dt = time.time() - previous_time
    previous_time = time.time()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    screen.fill('white')

    # rect movement and drawing
    test_rect_position += test_speed * dt
    test_rect.x = round(test_rect_position) 
    pygame.draw.rect(screen, 'red', test_rect)

    debug(dt) # this function just shows the info on the top left
    pygame.display.update()
