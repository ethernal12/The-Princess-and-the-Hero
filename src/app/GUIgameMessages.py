import pygame

def messages(canvas, text):
    pygame.draw.rect(canvas, (0, 0, 0), (
        10, 10, 20, 20))
    print('draw pricess')
    pygame.display.update()
    # Set the font and font size
    my_font = pygame.font.Font('freesansbold.ttf', 30)
    # Create a surface containing the text
    text_surface = my_font.render(text.value, True, (255, 0, 0))
    # Draw the text onto the canvas
    canvas.blit(text_surface, (100, 100))

