from logic import *
# Read the input file
def read_file(path):
    file = open(path, 'rt')
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
    golds_breeze_stench = [False for i in range(height*width)]
    golds_breeze = [False for i in range(height*width)]
    golds_stench = [False for i in range(height*width)]
    emptys = [False for i in range(height*width)]
    visible = [False for i in range(height*width)]
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
        if lst_cells[i] == 'BGS':
            golds_breeze_stench[i] = True
        if lst_cells[i] == 'BG':
            golds_breeze[i] = True
        if lst_cells[i] == 'GS':
            golds_stench = True

    return map, lst_cells, height, width, start, pits, wumpus, breeze, stench, golds, breeze_stench, emptys, golds_breeze_stench, golds_breeze, golds_stench, visible
def find_near_cell(pos, height, width):
    pos_x = pos % width
    pos_y = (pos-pos_x)/width

    (right_x, right_y) = (pos_x+1, pos_y)
    if right_x == width:
        right_x = pos_x

    (left_x, left_y) = (pos_x-1, pos_y)
    if left_x < 0:
        left_x = pos_x

    (up_x, up_y) = (pos_x, pos_y-1)
    if up_y < 0:
        up_y = pos_y

    (down_x, down_y) = (pos_x, pos_y + 1)
    if down_y == height:
        down_y = pos_y

    right_pos = int(right_x + right_y*width)
    left_pos = int(left_x + left_y*width)
    up_pos = int(up_x + up_y*width)
    down_pos = int(down_x + down_y*width)

    return right_pos, left_pos, up_pos, down_pos


