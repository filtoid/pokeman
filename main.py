import pygame

ball = None
speed = [2, 2]

def update(size):
    global ball
    global speed
    ball['rect'] = ball['rect'].move(speed)

    if ball['rect'].left < 0 or ball['rect'].right > size[0]:
        speed[0] = -speed[0]
    if ball['rect'].top < 0 or ball['rect'].bottom > size[1]:
        speed[1] = -speed[1]


def draw(screen):
    global ball

    black = (0, 0, 0)

    screen.fill(black)

    screen.blit(ball['image'], ball['rect'])

    pygame.display.flip()

def main():
    global ball
    ball = {}
    ball['image'] = pygame.image.load("pokeball_closed.png")
    ball['rect'] = ball['image'].get_rect()

    size = width, height = (600, 400)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Poke-man')

    quit = False
    while quit == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit = True
        update(size)
        draw(screen)


if __name__ == '__main__':
    pygame.init()
    main()
