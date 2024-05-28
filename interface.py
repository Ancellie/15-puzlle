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


class GameWindow:
    TILE_SIZE = 100
    BOARD_SIZE = TILE_SIZE * 4 + 10
    WINDOW_SIZE = (BOARD_SIZE + 120, BOARD_SIZE + 220)
    FPS = 60

    def create_tiles(self, board):
        tiles = []
        for row in range(len(board.board)):
            for col in range(len(board.board[row])):
                tile_rect = pygame.Rect(
                    col * (self.TILE_SIZE + 7) + 50 + (self.BOARD_SIZE - self.TILE_SIZE  * self.game.size) // 1.5,
                    row * (self.TILE_SIZE + 7) + 10 + (self.BOARD_SIZE - self.TILE_SIZE  * self.game.size) // 1.5,
                    self.TILE_SIZE,
                    self.TILE_SIZE
                )

                if board.board[row][col] != 0:
                    tile_surface = pygame.font.Font(None, 36).render(str(board.board[row][col]), True, (255, 255, 255))
                    tile_color = (255, 178, 102)
                else:
                    tile_surface = pygame.Surface((self.TILE_SIZE, self.TILE_SIZE))
                    tile_surface.fill((128, 128, 128))
                    tile_color = (0, 0, 0)
                tiles.append((tile_surface, tile_rect, tile_color))
        return tiles

    def __init__(self):
        self.game  = Game(size=4)
        self.board = self.game.puzzle
        self.empty_row = self.game.empty_row
        self.empty_col = self.game.empty_col
        self.font = pygame.font.SysFont('arial', 40)
        self.tiles = self.create_tiles(self.board)
        self.window = pygame.display.set_mode(self.WINDOW_SIZE)
        pygame.display.set_caption("15 Puzzle")
        self.buttons = self.create_buttons()

    def new_game(self):
        self.game = Game(size=4, shuffle_steps=100)
        self.game.shuffle_board()
        self.board     = self.game.puzzle
        self.empty_row = self.game.empty_row
        self.empty_col = self.game.empty_col
        self.tiles = self.create_tiles(self.board)
        self.draw_board()

    def solve_game(self):
        puzzle = self.game.puzzle
        # puzzle = puzzle.shuffle()
        #s = Solver(puzzle)
        tic = time.perf_counter()
        p = Solver(self.board).solve()
        toc = time.perf_counter()

        steps = 0
        for node in p:
            print(node.action)
            node.puzzle.pprint()
            steps += 1

            self.game.move(node.action)
            pygame.display.update()
            self.update_tiles()
            pygame.time.wait(100)

        print("Total number of steps: " + str(steps))
        print("Total amount of time in search: " + str(toc - tic) + " second(s)")

    def quit_game(self):
        self.running = False

    def update_tiles(self):
        self.board = self.game.puzzle
        self.tiles = self.create_tiles(self.board)
        self.empty_row = self.game.empty_row
        self.empty_col = self.game.empty_col
        self.draw_board()
        pygame.display.update()

    def animate_solution(self, solution):
        for move in solution:
            self.game.move(move)
            self.update_tiles()
            pygame.time.wait(500)

    def draw_board(self):
        self.window.fill((0, 150, 150))
        for tile in self.tiles:
            pygame.draw.rect(self.window, tile[2], tile[1])
            text_rect = tile[0].get_rect(center=tile[1].center)
            self.window.blit(tile[0], text_rect)

    def create_buttons(self):
        buttons = []
        button_width = 150
        button_height = 50
        button_spacing = 60

        new_game_button_rect = pygame.Rect(10, self.BOARD_SIZE + button_spacing, button_width, button_height)
        new_game_button = Button("New Game", new_game_button_rect, pygame.font.Font(None, 24), (255, 255, 255), (0, 51, 102),
                                 self.new_game)
        buttons.append(new_game_button)

        quit_button_rect = pygame.Rect(10 + (button_width + button_spacing - 30) * 2, self.BOARD_SIZE + button_spacing,
                                       button_width, button_height)
        quit_button = Button("Quit", quit_button_rect, pygame.font.Font(None, 24), (255, 255, 255), (102, 0, 0), self.quit_game)
        buttons.append(quit_button)

        solve_button_rect = pygame.Rect(10 + (button_width + button_spacing - 30), self.BOARD_SIZE + button_spacing,
                                        button_width, button_height)
        solve_button = Button("Solve", solve_button_rect, pygame.font.Font(None, 24), (255, 255, 255), (0, 102, 51), self.solve_game)
        buttons.append(solve_button)

        return buttons

    def run(self):
        clock = pygame.time.Clock()
        while self.running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False
                elif event.type == KEYDOWN:
                    self.moving(event)
                    self.update_tiles()
                elif not self.solve_running:
                    for button in self.buttons:
                        button.handle_event(event)

            self.draw_board()
            for button in self.buttons:
                button.draw(self.window)

            self.display_message()

            pygame.display.update()
            clock.tick(self.FPS)

        save_board_to_file(self.board, "board.txt")
        pygame.quit()
