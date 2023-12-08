import pygame

class Button:
    def __init__(self, x, y, image, singleclick):
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.clicked = False
        self.singleclick = singleclick

    def draw(self, surface):
        action = False
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                action = True
                if self.singleclick:
                    self.clicked = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        surface.blit(self.image, self.rect.topleft)
        return action
