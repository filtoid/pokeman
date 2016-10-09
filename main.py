import pygame

ball = None

def update():
    global ball
    pass

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
        update()
        draw(screen)


if __name__ == '__main__':
    pygame.init()
    main()
