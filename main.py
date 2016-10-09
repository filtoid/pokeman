import pygame

def main():
    size = width, height = (600, 400)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Poke-man')

    quit = False
    while quit == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit = True


if __name__ == '__main__':
    pygame.init()
    main()
