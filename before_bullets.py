# import pygame
# import os


# WIDTH, HEIGHT = 900, 500
# WIN = pygame.display.set_mode((WIDTH, HEIGHT)) #window
# pygame.display.set_caption("First game!")

# WHITE = (255,255,255)
# PURPLE = (140, 10, 200)

# FPS = 60 #FRAMES per second. how many fps we want our game to update. 60 is standard.
# VEL = 5
# SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55,40
# BORDER = pygame.Rect(WIDTH/2 -5, 0, 10, HEIGHT)

# YELLOW_SPACESHIP_IMAGE = pygame.image.load(
#     os.path.join('Assets', 'spaceship_yellow.png'))#join because depending on operating system, path might be different.
# YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE,(SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90) #this resizes the spaceship. can look at aspect ratio first.


# RED_SPACESHIP_IMAGE = pygame.image.load(
#     os.path.join('Assets', 'spaceship_red.png'))#join because depending on operating system, path might be different.
# RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE,(SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270) #this resizes the spaceship. can look at aspect ratio first.


# def draw_window(red, yellow):
#     '''this creates the purple background and the spaceships'''

#     WIN.fill(PURPLE) #this gives the window color. rgb
#     # WIN.blit(YELLOW_SPACESHIP, (200, 125)) #the spaceship images are known as surfaces
#     # WIN.blit(RED_SPACESHIP, (700, 125))

#     pygame.draw.rect(WIN, WHITE, BORDER)

#     WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y)) #the spaceship images are known as surfaces
#     WIN.blit(RED_SPACESHIP, (red.x, red.y))


#     pygame.display.update() #this is mandatory to see the colors and fills

# def yellow_handle_movement(keys_pressed, yellow):
#     if keys_pressed[pygame.K_a] and yellow.x - VEL > 0: #LEFT
#         yellow.x -= VEL    
#     if keys_pressed[pygame.K_d] and yellow.x + VEL + yellow.width < BORDER.x: #RIGHT
#         yellow.x += VEL
#     if keys_pressed[pygame.K_w] and yellow.y - VEL > 0: #UP
#         yellow.y -= VEL
#     if keys_pressed[pygame.K_s] and yellow.y + VEL + yellow.height< HEIGHT - 10: #BOTTOM
#         yellow.y += VEL

# def red_handle_movement(keys_pressed, red):
#     if keys_pressed[pygame.K_LEFT] and red.x - VEL > BORDER.x + BORDER.width: #LEFT
#         red.x -= VEL    
#     if keys_pressed[pygame.K_RIGHT] and red.x + VEL < WIDTH - red.width: #RIGHT
#         red.x += VEL
#     if keys_pressed[pygame.K_UP] and red.y - VEL > 0: #UP
#         red.y -= VEL
#     if keys_pressed[pygame.K_DOWN] and red.y + VEL < HEIGHT - red.height - 10: #down
#         red.y += VEL


# #all games typically have a loop
# def main():
#     red = pygame.Rect(700, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
#     yellow = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)


#     clock = pygame.time.Clock()

#     run = True
#     while run:
#         clock.tick(FPS) #this controls the speed of this while loop

#         #always have this line
#         for event in pygame.event.get(): #this gets us the list of events and we're looping through them
#             if event.type == pygame.QUIT: #this executes when the x on the top right of the window is pressed. if not here, force quit is required.
#                 run = False
        
#         keys_pressed = pygame.key.get_pressed()
#         yellow_handle_movement(keys_pressed, yellow)
#         red_handle_movement(keys_pressed, red)

#         draw_window(red, yellow)
#     pygame.quit()

# if __name__ == "__main__": #this makes sure to run main ONLY when this file is ran, and not when this file is imported which causes the function to run.
#     main() 