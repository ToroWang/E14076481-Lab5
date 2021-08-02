import pygame
import os

# load image
MENU_IMAGE = pygame.image.load(os.path.join("images", "upgrade_menu.png"))
UPGRADE_IMAGE = pygame.image.load(os.path.join("images", "upgrade.png"))
SELL_IMAGE = pygame.image.load(os.path.join("images", "sell.png"))


class UpgradeMenu:
    def __init__(self, x, y):
        self.image_menu = pygame.transform.scale(MENU_IMAGE, (180, 180))  # image of the menu
        self.image_upgrade = pygame.transform.scale(UPGRADE_IMAGE, (50, 50))
        self.image_sell = pygame.transform.scale(SELL_IMAGE, (50, 50))
        self.rect = self.image_menu.get_rect()
        self.rect.bottomright = (x, y)  # center of the menu
        self.__buttons = []  # (Q2) Add buttons here
        pass

    def draw(self, win):
        """
        (Q1) draw menu itself and the buttons
        (This method is call in draw() method in class TowerGroup)
        :return: None
        """
        # draw menu
        win.blit(self.image_menu, self.rect.center)

        # draw button
        x, y = self.rect.center
        win.blit(self.image_upgrade, (x+65, y))
        win.blit(self.image_sell, (x+65, y+135))

        self.__buttons.append(Button(self.image_upgrade, "upgrade", x+65 + 25, y + 25))
        self.__buttons.append(Button(self.image_sell, "sell",  x+65 + 25, y+135 + 25))
        # (Q2) Draw buttons here
        pass

    def get_buttons(self):
        """
        (Q1) Return the button list.
        (This method is call in get_click() method in class TowerGroup)
        :return: list
        """
        return self.__buttons
        pass


class Button:
    def __init__(self, image, name, x, y):
        self.name = name
        self.rect = image.get_rect()
        self.rect.center = x, y

    def clicked(self, x, y):
        """
        (Q2) Return Whether the button is clicked
        (This method is call in get_click() method in class TowerGroup)
        :param x: mouse x
        :param y: mouse y
        :return: bool
        """
        return True if self.rect.collidepoint(x, y) else False
        pass

    def response(self):
        """
        (Q2) Return the button name.
        (This method is call in get_click() method in class TowerGroup)
        :return: str
        """
        return self.name
        pass






