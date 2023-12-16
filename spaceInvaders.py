import pygame
import time
import random

pygame.font.init()

# Setting up screen dimensions
WIDTH, HEIGHT = 1000, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders Low Budget version ")

# Background
BG = pygame.transform.scale(pygame.image.load("galaxy.jpeg"), (WIDTH, HEIGHT))

# Player and Star dimensions
PLAYER_WIDTH, PLAYER_HEIGHT = 40, 60
STAR_WIDTH, STAR_HEIGHT = 10, 20

# Velocities
PLAYER_VEL = 5
STAR_VEL = 3

# Score font
FONT = pygame.font.SysFont("verdana", 40)  # Changed font and size

# Function to draw elements on the screen
def draw(player, elapsed_time, stars, score):
    WIN.blit(BG, (0, 0))
    time_text = FONT.render(f"Time: {round(elapsed_time)}s", 1, (255, 255, 255))
    score_text = FONT.render(f"Score: {score}", 1, (255, 255, 255))  # Displaying the score

    WIN.blit(time_text, (10, 10))
    WIN.blit(score_text, (WIDTH - score_text.get_width() - 10, 10))

    # Drawing the player as an oval
    pygame.draw.ellipse(WIN, (0, 0, 255), player)  # Changed to blue oval

    # Drawing stars
    for star in stars:
        pygame.draw.rect(WIN, (255, 255, 255), star)

    pygame.display.update()

# Main function controlling the game logic
def main():
    run = True
    player = pygame.Rect(200, HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)
    clock = pygame.time.Clock()
    start_time = time.time()
    elapsed_time = 0
    star_add_increment = 2000
    star_count = 0
    stars = []
    hit = False
    score = 0  # Initializing score

    while run:
        star_count += clock.tick(60)
        elapsed_time = time.time() - start_time

        if star_count > star_add_increment:
            for _ in range(3):
                star_x = random.randint(0, WIDTH - STAR_WIDTH)
                star = pygame.Rect(star_x, -STAR_HEIGHT, STAR_WIDTH, STAR_HEIGHT)
                stars.append(star)

            star_add_increment = max(200, star_add_increment - 50)
            star_count = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        keys = pygame.key.get_pressed()
        move_player(player, keys)

        for star in stars[:]:
            star.y += STAR_VEL
            if star.y > HEIGHT:
                stars.remove(star)
                score += 1  # Increment score for dodging a star
            elif star.colliderect(player):
                display_end_message(WIN, FONT, WIDTH, HEIGHT)
                hit = True
                break

        if hit:
            break

        draw(player, elapsed_time, stars, score)

    pygame.quit()

# Function to move the player
def move_player(player, keys):
    if keys[pygame.K_LEFT] and player.x - PLAYER_VEL >= 0:
        player.x -= PLAYER_VEL
    if keys[pygame.K_RIGHT] and player.x + PLAYER_VEL + player.width <= WIDTH:
        player.x += PLAYER_VEL

# Function to display the end message
def display_end_message(WIN, FONT, WIDTH, HEIGHT):
     # Game over message with multicolored letters
            lost_text = [FONT.render(char, 1, (random.randint(0,255), random.randint(0,255), random.randint(0,255))) for char in "TOO SLOW !"]
            for i, char in enumerate(lost_text):
                WIN.blit(char, (WIDTH/2 - char.get_width()/2 + i*30, HEIGHT/2 - char.get_height()/2))
            pygame.display.update()
            pygame.time.delay(4000)


 

if __name__ == "__main__":
    main()
