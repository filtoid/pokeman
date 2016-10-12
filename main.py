import pygame
import random

ball = None
speed = [0, 0]
pikachu = None

def update(size):
    global ball
    global speed
    global pikachu

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

    if pikachu['visible']:
        # check if the ball is touching the pikachu
        if pikachu['rect'].colliderect(ball['rect']):
            pikachu['visible'] = False
            print("You put out the fire!")
    else:
        # pick a random location to place the pikachu
        new_x = random.randrange(20,500)
        new_y = random.randrange(20,300)
        pikachu['rect'].left = new_x
        pikachu['rect'].top = new_y
        pikachu['visible'] = True

def draw(screen):
    global ball
    global pikachu

    black = (0, 0, 0)

    screen.fill(black)

    screen.blit(ball['image'][ball['cur_image']], ball['rect'])
    if pikachu['visible']:
        screen.blit(pikachu['image'][0], pikachu['rect'])

    #Draw arbitrary text on the screen
    font = pygame.font.Font(None, 36)
    text = font.render("Fireman", 1, (255, 255, 0))
    textpos = text.get_rect()
    textpos.left = 200
    screen.blit(text, textpos)

    pygame.display.flip()


def main():
    global ball
    global speed
    global pikachu

    ball = {}
    ball['image'] = []
    ball['image'].append(pygame.image.load("kieran_fire.png"))
    ball['image'].append(pygame.image.load("kieran_fire.png"))
    ball['image'][0] = pygame.transform.scale(ball['image'][0],(150,200))
    ball['image'][1] = pygame.transform.scale(ball['image'][1],(150,200))
    ball['cur_image'] = 0
    ball['start_counter'] = 10
    ball['swap_counter'] = ball['start_counter']
    ball['rect'] = ball['image'][0].get_rect()

    pikachu = {}
    pikachu['image'] = []
    pikachu['image'].append(pygame.image.load("fire.png"))
    pikachu['image'][0] = pygame.transform.scale(pikachu['image'][0],(61,79))
    #211x314
    pikachu['rect'] = pikachu['image'][0].get_rect()
    pikachu['visible'] = False

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
