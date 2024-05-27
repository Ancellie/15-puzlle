import pygame
import time
from pygame.locals import *
from game import Game, save_board_to_file
from solver import Solver
import threading


class Button:
    def __init__(self, text, rect, font, fg_color, bg_color, callback):
        self.text = text  # Текст кнопки
        self.rect = rect  # Прямокутник, який представляє кнопку
        self.font = font  # Шрифт кнопки
        self.fg_color = fg_color  # Колір тексту кнопки
        self.bg_color = bg_color  # Колір фону кнопки
        self.callback = callback  # Функція зворотного виклику, яка виконується при натисканні кнопки
        self.running = True  # Прапорець, що вказує, чи триває робота кнопки

    def draw(self, surface):
        pygame.draw.rect(surface, self.bg_color, self.rect)  # Відображення фону кнопки
        text_surface = self.font.render(self.text, True, self.fg_color)  # Створення поверхні з текстом кнопки
        text_rect = text_surface.get_rect(center=self.rect.center)  # Вирівнювання тексту кнопки по центру прямокутника кнопки
        surface.blit(text_surface, text_rect)  # Відображення тексту кнопки на екрані

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:  # Перевірка на натискання кнопки мишею
            if self.rect.collidepoint(event.pos):  # Перевірка, чи позиція натискання знаходиться в межах прямокутника кнопки
                self.callback()  # Виклик функції
                return True
        return False


