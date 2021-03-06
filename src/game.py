import pygame
import pygame_menu
import pygame_gui
from pygame.locals import *
from menu import Menu
from territory import Territory
 
display_width = 800
display_height = 600
territory_names = ['Akkala',
                    'Central Hyrule',
                    'Dueling Peaks',
                    'East Necluda',
                    'Eldin',
                    'Faron',
                    'Gerudo Highlands',
                    'Gerudo Wastelands',
                    'Great Hyrule Forest',
                    'Great Plateau',
                    'Hebra',
                    'Lake',
                    'Lanaryu',
                    'Ridgelands',
                    'Tabantha'
                    ]

pygame.mixer.init()
pygame.init()
manager = pygame_gui.UIManager((display_width, display_height))
hello_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((display_width // 2 - 50, display_height - 50 ), (100, 50)),
                                             text='Action Menu',
                                             manager=manager)
clock = pygame.time.Clock()

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
    territories = []
    for territory in territory_names:
        territories.append(Territory(territory))
    img = pygame.image.load('../map.jpg').convert()
    img_rect = img.get_rect()
    img_rect.center = display_width//2, display_height//2
    while running:
        time_delta = clock.tick(60)/1000.0
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            elif event.type == QUIT:
                running = False
            elif event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == hello_button:
                        Menu(pygame.Rect((10, 10), (640, 480)), manager)
            manager.process_events(event)
        manager.update(time_delta)
        gameDisplay.fill((0,0,0))
        gameDisplay.blit(img, img_rect)
        pygame.draw.rect(gameDisplay, (45,0,0), img_rect, 1)
        manager.draw_ui(gameDisplay)
        pygame.display.update()
    # pygame.mixer.music.stop()
    # pygame.mixer.quit()

game_menu()