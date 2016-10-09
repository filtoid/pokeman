import pygame

ball = None
speed = [0, 0]

def update(size):
    global ball
    global speed
    ball['rect'] = ball['rect'].move(speed)

    if ball['rect'].left < 0 or ball['rect'].right > size[0]:
        ball['rect'] = ball['rect'].move([speed[0]*-1,0])
    if ball['rect'].top < 0 or ball['rect'].bottom > size[1]:
        ball['rect'] = ball['rect'].move([0,speed[1]*-1])

    ball['swap_counter'] -= 1
    if ball['swap_counter'] < 0:
        ball['swap_counter'] = ball['start_counter']
        ball['cur_image'] += 1
        if ball['cur_image'] > len(ball['image'])-1:
            ball['cur_image'] = 0


def draw(screen):
    global ball

    black = (0, 0, 0)

    screen.fill(black)

    screen.blit(ball['image'][ball['cur_image']], ball['rect'])

    pygame.display.flip()

    
def main():
    global ball
    global speed

    ball = {}
    ball['image'] = []
    ball['image'].append(pygame.image.load("pokeball_closed.png"))
    ball['image'].append(pygame.image.load("pokeball_open.png"))
    ball['cur_image'] = 0
    ball['start_counter'] = 10
    ball['swap_counter'] = ball['start_counter']
    ball['rect'] = ball['image'][0].get_rect()

    size = width, height = (600, 400)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Poke-man')

    quit = False
    clock = pygame.time.Clock()

    while quit == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit = True
        keys = pygame.key.get_pressed()
        #Reset speed then adjust based on which keys are pressed
        speed = [0,0]
        if keys[pygame.K_LEFT]:
            speed[0] -= 4
        if keys[pygame.K_RIGHT]:
            speed[0] += 4
        if keys[pygame.K_UP]:
            speed[1] -= 4
        if keys[pygame.K_DOWN]:
            speed[1] += 4

        if keys[pygame.K_ESCAPE]:
            quit = True

        clock.tick(30)
        update(size)
        draw(screen)


if __name__ == '__main__':
    pygame.init()
    main()
