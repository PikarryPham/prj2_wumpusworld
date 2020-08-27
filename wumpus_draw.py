import pygame

from wumpus_data import *
from wumpus_logic import *
def loadImages():
    global HIDDEN, VISIBLE, BACKGROUND, MESSAGE_COLOR
    global WUMPUS_PIXMAP, PIT_PIXMAP, GOLD_PIXMAP, STENCH_PIXMAP, BREEZE_PIXMAP
    global ADVENTURER_GOLD_PIXMAP, ADVENTURER_DEAD_PIXMAP
    global ADVENTURER_ARROW_PIXMAP, ADVENTURER_NO_ARROW_PIXMAP
# Set Cell Colors
# Load Images
def drawPit(surface, data, x, y):
    pixmap = PIT_PIXMAP
    dx, dy = .5, .0
    cell_size = getCellSize(data)
    exists = cellContainsPit(data, x, y)
    point = ((x+dx)*cell_size, (y+dy*cell_size))
    if exists:
        surface.blit(pixmap, point)

# Implement drawWumpus
def drawWumpus():
    pass
# Implement drawGold
def drawGold():
    pass
# Implement drawBreeze
def drawBreeze():
    pass
# Implement drawStench
def drawStench():
    pass
# Implement drawCell
def drawCell():
    pass
# Implement drawAdventurer
def drawAdventurer():
    pass
# Implement drawGameOver
def drawGameOver():
    pass
# Implement updateDisplay
def updateDisplay():
    pass