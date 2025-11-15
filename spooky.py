import pygame
import sys
import os

def main(image_path):
    # Initialize Pygame
    pygame.init()

    # Load the image
    try:
        image = pygame.image.load(image_path)
    except pygame.error as e:
        print(f"Cannot load image: {e}")
        return

    # Get the display size
    screen_info = pygame.display.Info()
    screen_width, screen_height = screen_info.current_w, screen_info.current_h

    # Create a full-screen display
    screen = pygame.display.set_mode((screen_width, screen_height), pygame.NOFRAME | pygame.FULLSCREEN)

    # Scale the image to fit the screen
    image = pygame.transform.scale(image, (screen_width, screen_height))

    # Hide the mouse cursor
    pygame.mouse.set_visible(False)

    # Game loop
    running = True
    while running:
        for event in pygame.event.get():
            # Exit on quit (but ignore keyboard input)
            if event.type == pygame.QUIT:
                running = False
            
            # Skip any keyboard events
            if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                continue

        screen.blit(image, (0, 0))
        pygame.display.flip()

    # Clean up
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    # Change this path to your image file
    image_path = './PJyEybKyQhGBpM4QXw7ccH-2902801811.jpg'
    main(image_path)

