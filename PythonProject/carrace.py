import pygame
import random

# Initialize Pygame
pygame.init()


# Set screen size
screen_width = 400
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))

# Set window title
pygame.display.set_caption("Car Racing Game")
width,height = 800,600

bg_img = pygame.image.load("road.png")

bg_img = pygame.transform.scale(bg_img,(width,height))

# Load images
car_img = pygame.image.load("car.png")
car_width = 50
car_height = 100

# Set clock
clock = pygame.time.Clock()

# Set colors
white = (255, 255, 255)
black = (50, 180, 0)
red = (255, 0, 0)

# Define functions
def draw_car(x, y):
    screen.blit(car_img, (x, y))

def message_display(text):
    font = pygame.font.Font(None, 60)
    text_surface = font.render(text, True, red)
    text_rect = text_surface.get_rect()
    text_rect.center = (screen_width / 2, screen_height / 2)
    screen.blit(text_surface, text_rect)
    pygame.display.update()
    pygame.time.delay(3000)

def crash():
    message_display("Oops!!..")

# Set initial car position
car_x = (screen_width / 2) - (car_width / 2)
car_y = screen_height - car_height

# Set initial obstacle position
obstacle_width = 50
obstacle_height = 50
obstacle_x = random.randrange(0, screen_width - obstacle_width)
obstacle_y = -obstacle_height
obstacle_speed = 5

# Game loop
game_exit = False
while not game_exit:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_exit = True

    # Move car
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        car_x -= 5
    if keys[pygame.K_RIGHT]:
        car_x += 5

    # Move obstacle
    obstacle_y += obstacle_speed

    # Check for collision
    if car_x < obstacle_x + obstacle_width and car_x + car_width > obstacle_x and car_y < obstacle_y + obstacle_height and car_y + car_height > obstacle_y:
        crash()

    # Check if obstacle has reached bottom of screen
    if obstacle_y > screen_height:
        obstacle_y = -obstacle_height
        obstacle_x = random.randrange(0, screen_width - obstacle_width)

    # Draw background
    screen.fill(white)

    # Draw car
    draw_car(car_x, car_y)

    # Draw obstacle
    pygame.draw.rect(screen, black, [obstacle_x, obstacle_y, obstacle_width, obstacle_height])

    # Update screen
    pygame.display.update()

    # Set clock speed
    clock.tick(60)

# Quit Pygame
pygame.quit()
quit()