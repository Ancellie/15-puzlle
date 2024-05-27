import pygame
from pygame.locals import *

class Button:
    def __init__(self, text, pos, size, font, fg_color, bg_color, hover_color, callback):
        self.text = text
        self.pos = pos
        self.size = size
        self.rect = pygame.Rect(pos, size)
        self.font = font
        self.fg_color = fg_color
        self.bg_color = bg_color
        self.hover_color = hover_color
        self.callback = callback
        self.hovered = False

    def draw(self, surface):
        current_color = self.hover_color if self.hovered else self.bg_color
        pygame.draw.rect(surface, current_color, self.rect, border_radius=10)
        text_surface = self.font.render(self.text, True, self.fg_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            self.hovered = self.rect.collidepoint(event.pos)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.callback()
                return True
        return False

