import pymunk
import pymunk.pygame_util
import pygame

GRAY = (220, 220, 220)

pygame.init()
size = 640, 800
screen = pygame.display.set_mode(size)
draw_options = pymunk.pygame_util.DrawOptions(screen)

space = pymunk.Space()
space.gravity = 0, -9.81

b0 = space.static_body
segment = pymunk.Segment(b0, (0, 0), (640, 0), 4)
segment.elasticity = 1

body = pymunk.Body(mass=1, moment=10 )
body.position = 100, 700
body.apply_impulse_at_local_point((15,0))

circle = pymunk.Circle(body, radius=30)
circle.elasticity = 0.95
space.add(body, circle, segment)

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