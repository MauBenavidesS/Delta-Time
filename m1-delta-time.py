import pygame, sys
from debug import debug

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

test_rect = pygame.Rect(0, 310, 100, 100)
test_speed = 200

while True:
    # clock.tick(60)
    # dt = clock.tick(60) 
    # dt gives us the milliseconds since the previous frame
    # 1/60 = 0.0166666, but we want it in seconds not in milliseconds
    # dt = 16
    dt = clock.tick(144) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    screen.fill('white')

    # rect movement and drawing
    test_rect.x += test_speed * dt # Here we want to multiply delta time
    pygame.draw.rect(screen, 'red', test_rect)

    debug(dt) # this function just shows the info on the top left
    pygame.display.update()