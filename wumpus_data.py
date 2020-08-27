import random
def setDimensions(data, width, height):
    data[0] = width
    data[1] = height
def getDimensions(data):
    return (data[0], data[1])
# Implement setCellSize
def setCellSize(data, cell_size):
    pass
# Implement getCellSize
def getCellSize(data):
    pass
# Implement setPits
def setPits(data, lst_pits):
    pass
# Implement getPits
def getPits(data):
    pass
# Implement setVisible
def setVisible(data, lst_visible):
    pass
# Implement getVisible
def getVisible(data):
    pass
# Implement setWumpusPosition
def setWumpusPosition():
    pass
# Implement getWumpusPosition
def getWumpusPosition():
    pass
# Implement setGoldPosition
def setGoldPosition():
    pass
# Implement getGoldPosition
def getGoldPosition():
    pass
# Implement setHaveGold
def setHaveGold():
    pass
# Implement getHaveGold
def getHaveGold():
    pass
# Implement setHaveArrow
def setHaveArrow():
    pass
# Implement getHaveArrow
def getHaveArrow():
    pass
# Implement setIsAlive
def setIsAlive():
    pass
# Implement getIsAlive
def getIsAlive():
    pass
# Implement setAdventurerPosition
def setAdventurerPosition():
    pass
# Implement getAdventurerPosition
def getAdventurerPosition():
    pass
# You must add to initializeData so that it will create
# correct values for the wumpus world
# The code provided here makes place holders for the values
def initializeData(width, height, cell_size, debug=0):
    pits = []
    visible = []
    for i in range(width*height):
        pits.append(False)
        visible.append(False)
    data = [ width, height, cell_size,
            pits, visible,
            width-1, height-1,
            1, 1,
            False, True, True,
            0, 0,
            ]
    return data

# Read file input.txt
def read_file(file_name):
    file = open(file_name, 'rt')
    size = int(file.readline().strip().split('\t')[0])
    height = size
    width = size
    assert height>0 and width>0
    
    map = []
    for i in range(height):
        row = file.readline().strip().split('.')
        map.append(row)
    lst_cells = []
    for i in range(len(map)):
        for j in range(len(map[0])):
            lst_cells.append(map[i][j])

    pits = [False for i in range(height*width)]
    wumpus = [False for i in range(height*width)]
    breeze = [False for i in range(height*width)]
    stench = [False for i in range(height*width)]
    golds = [False for i in range(height*width)]
    breeze_stench = [False for i in range(height*width)]
    emptys = [False for i in range(height*width)]
    start = ''

    for i in range(height*width):
        if lst_cells[i] == 'A':
            start = i
        if lst_cells[i] == 'B':
            breeze[i] = True
        if lst_cells[i] =='G':
            golds[i] = True
        if lst_cells[i] =='S':
            stench[i] = True
        if lst_cells[i] =='P':
            pits[i] = True
        if lst_cells[i] == 'BS':
            breeze_stench = True
        if lst_cells[i] == 'W':
            wumpus[i] = True
        if lst_cells[i] == '-':
            emptys[i] = True
    return map, lst_cells, height, width, start, pits, wumpus, breeze, stench, golds, breeze_stench, emptys
