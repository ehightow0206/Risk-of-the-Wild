import pygame
import pygame_menu
from pygame.locals import *
 
display_width = 900
display_height = 600

pygame.mixer.init()
pygame.init()

gameDisplay = pygame.display.set_mode((display_width,display_height))

def game_menu():
    pygame.mixer.music.load("../Opening.mp3")
    pygame.mixer.music.play()
    botw_image = pygame_menu.baseimage.BaseImage(
        image_path="../background.jpg",
        drawing_mode=pygame_menu.baseimage.IMAGE_MODE_FILL,
        drawing_offset=(0,0)
    )
    mytheme = pygame_menu.Theme(background_color=botw_image, 
                    title_bar_style=pygame_menu.widgets.MENUBAR_STYLE_NONE,
                    title_font=pygame_menu.font.FONT_BEBAS,
                    widget_font=pygame_menu.font.FONT_BEBAS,
                    widget_background_color=(80, 80, 80, 30),
                    )
    menu = pygame_menu.Menu(
        height=display_height,
        theme=mytheme,
        title='Risk of the Wild',
        width=display_width
    )

    menu.add.button('Play', game_loop)
    menu.add.button('Quit', pygame_menu.events.EXIT)
    menu.mainloop(gameDisplay)
    
def game_loop():
    running = True
    img = pygame.image.load('../map.jpg')
    img.convert()
    rect = img.get_rect()
    rect.center = display_width//2, display_height//2
    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            elif event.type == QUIT:
                running = False
        gameDisplay.fill((0,0,0))
        gameDisplay.blit(img, rect)
        pygame.draw.rect(gameDisplay, (45,0,0), rect, 1)
        pygame.display.update()
    # pygame.mixer.music.stop()
    # pygame.mixer.quit()

game_menu()