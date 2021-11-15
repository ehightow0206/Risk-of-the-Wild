import pygame
from typing import Tuple, Any
from pygame_gui import UIManager, PackageResource
from pygame_gui.elements import *


class Menu(UIWindow):
    def __init__(self, rect, ui_manager):
        super().__init__(rect, ui_manager,
                         window_display_title='Action Menu',
                         object_id='#action_menu',
                         resizable=True)

        self.test_text = UITextBox('hello world',
                                    rect, 
                                    self.ui_manager,
                                    container=self)                 

        self.test_text_entry = UITextEntryLine(pygame.Rect((int(self.rect.width / 2),
                                                            int(self.rect.height * 0.50)),
                                                           (200, -1)),
                                               self.ui_manager,
                                               container=self)
        self.test_text_entry.set_forbidden_characters('numbers')

        current_resolution_string = 'Select a territory'
        self.test_drop_down_menu = UIDropDownMenu(['Akkala',
                                                   'Central Hyrule',
                                                   'Dueling Peaks',
                                                   'East Necula'
                                                   'Eldin',
                                                   'Faron',
                                                   'Gerudo Highlands',
                                                   'Gerudo Wastelands',
                                                   'Great Hyrule Forest'
                                                   'Great Plateau',
                                                   'Hebra',
                                                   'Lake',
                                                   'Lanaryu',
                                                   'Ridgelands'
                                                   'Tabantha'
                                                   ],
                                                  current_resolution_string,
                                                  pygame.Rect((int(self.rect.width / 2),
                                                               int(self.rect.height * 0.3)),
                                                              (200, 25)),
                                                  self.ui_manager,
                                                  container=self)

    def update(self, time_delta):
        super().update(time_delta)