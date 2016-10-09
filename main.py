import pygame

def update():
    pass

def draw(screen):
    black = (0, 0, 0)
    
    screen.fill(black)
    pygame.display.flip()

def main():
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
