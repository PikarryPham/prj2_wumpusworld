from wumpus_data import *
# Implement cellContainsWumpus
# Implement cellContainsGold

def cellContainsPit(data, x, y):
    (width, height) = getDimensions(data)
    pits = getPits(data)
    i = y * width + x
    return pits[i]
# Implement cellIsVisible
# Implement cellIsInCavern
def neighborCellIsVisible(data, x, y):
    if cellIsInCavern(data, x + 1, y) and cellIsVisible(data, x + 1, y):
        return True
    elif cellIsInCavern(data, x - 1, y) and cellIsVisible(data, x - 1, y):
        return True
    elif cellIsInCavern(data, x, y + 1) and cellIsVisible(data, x, y + 1):
        return True
    elif cellIsInCavern(data, x, y - 1) and cellIsVisible(data, x, y - 1):
        return True
    return False
# Implement neighborCellContainsPit
# Implement neighborCellContainsWumpus
# Implement handleMouseClick
# Implement setCellVisible
# Implement visitCell