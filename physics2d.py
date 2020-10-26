import pymunk
import pymunk.pygame_util
import pygame
import random as r
import time 
GRAY = (220, 220, 220)

pygame.init()
size = 800, 800
screen = pygame.display.set_mode(size)
draw_options = pymunk.pygame_util.DrawOptions(screen)

space = pymunk.Space()
space.gravity = 0, -900

b0 = space.static_body
segment = pymunk.Segment(b0, (0, 0), (1000, 0), 4)
segment.elasticity = 1
segment2 = pymunk.Segment(b0,(200,200),(600,200), 20)
segment2.elasticity = 1
sidel = pymunk.Segment(b0,(0,0),(0,800), 4)
sider = pymunk.Segment(b0,(800,0),(800,800), 4)
sidel.elasticity = 1
sider.elasticity = 1

body = pymunk.Body(mass=100, moment=10 )
body.position = 100, 700
body.apply_force_at_local_point((r.randint(10,300),981),(100,700))



circle = pymunk.Circle(body, radius=30)
circle.elasticity = 1

space.add(body, circle, segment, segment2,sidel,sider)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.image.save(screen, 'intro1.png')

    screen.fill(GRAY)
    space.debug_draw(draw_options)
    pygame.display.update()
    space.step(0.01)

pygame.quit()


