import pygame
import math
import random

# Initialize pygame
pygame.init()

# Create a game window
window = pygame.display.set_mode((800, 600)) 
pygame.display.set_caption("Rocket Launcher")

# Load the rocket image
rocket_img = pygame.image.load('rocket.png')

# Create variables to store the rocket's x and y coordinates
rocket_x = 400
rocket_y = 300

# Create a variable to store the rocket's speed
rocket_speed = 0.5

# Create a variable to store the rocket's angle
rocket_angle = 0

# Create variables to store the x and y components of the rocket's velocity
rocket_vx = 0
rocket_vy = 0

# Create a loop to run the game
running = True
while running:

    # Get the list of all events
    events = pygame.event.get()

    # Iterate through the list of events
    for event in events:
        # Check for the QUIT event
        if event.type == pygame.QUIT:
            running = False  # Stop the loop

    # Get the keys being pressed
    keys = pygame.key.get_pressed()

    # Check for left and right arrow keys
    if keys[pygame.K_LEFT]:
        rocket_angle -= 0.1
    if keys[pygame.K_RIGHT]:
        rocket_angle += 0.1

    # Calculate the x and y components of the rocket's velocity
    rocket_vx = rocket_speed * math.cos(rocket_angle)
    rocket_vy = rocket_speed * math.sin(rocket_angle)

    # Update the rocket's x and y coordinates
    rocket_x += rocket_vx
    rocket_y += rocket_vy

    # Draw the rocket
    window.fill((0, 0, 0))  # Fill the window with black
    rotated_rocket = pygame.transform.rotate(rocket_img, rocket_angle * 180 / math.pi)
    rect = rotated_rocket.get_rect(center=(rocket_x, rocket_y))
    window.blit(rotated_rocket, rect)

    # Update the display
    pygame.display.update()
