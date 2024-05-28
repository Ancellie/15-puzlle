import itertools
from heapq import heappop, heappush


class Node:
    #Клас, що представляє вузол розв'язувача
    #- 'puzzle' - це екземпляр класу Puzzle
    #- 'parent' - попередній вузол, створений розв'язувачем, якщо є
    #- 'action' - дія, виконана для отримання головоломки, якщо є

    def __init__(self, puzzle, parent=None, action=None):
        self.puzzle = puzzle
        self.parent = parent
        self.action = action
        if self.parent is not None:
            self.g = parent.g + 1
        else:
            self.g = 0

    @property
    def score(self):
        return self.g + self.h

    @property
    def state(self):
        #Повертає хешований представлення self
        return str(self)

    @property
    def path(self):
        #Відновлює шлях від кореня 'parent'

        node, p = self, []
        while node:
            p.append(node)
            node = node.parent
        yield from reversed(p)

    @property
    def solved(self):
        #Обгортка для перевірки, чи головоломка 'puzzle' розв'язана
        return self.puzzle.solved

    @property
    def actions(self):
        #Обгортка для 'actions', доступних в поточному стані
        return self.puzzle.actions

    @property
    def h(self):
        return self.puzzle.manhattan

    def __str__(self):
        return str(self.puzzle)

    def __lt__(self, other):
        return self.score < other.score

    def __gt__(self, other):
        return self.score > other.score

    def __le__(self, other):
        return self.score <= other.score

    def __ge__(self, other):
        return self.score >= other.score

    def __eq__(self, other):
        return self.score == other.score

    def __ne__(self, other):
        return self.score != other.score