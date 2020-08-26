import sys
import random
import wumpus_logic
import wumpus_data
from wumpus_data_black_box import testInt, testBool, testList, show_error, show_ok

g_width        = 4
g_height       = 4
g_cell_size    = 100
g_wumpus_x     = random.randint(1,2)
g_wumpus_y     = random.randint(1,2)
g_gold_x       = random.randint(1,2)
g_gold_y       = random.randint(1,2)
g_pit_x        = random.randint(1,2)
g_pit_y        = random.randint(1,2)
g_visible_x    = random.randint(1,2)
g_visible_y    = random.randint(1,2)
g_adventurer_x = 0
g_adventurer_y = 0
    
def good_sample_data(width, height, cell_size):
    return [ width,
             height,
             cell_size,
             [ ((x == g_pit_x) and (y == g_pit_y)) 
               for y in range(height) for x in range(width)],
             [ ((x == g_visible_x) and (y == g_visible_y)) 
               for y in range(height) for x in range(width)],
             g_wumpus_x, g_wumpus_y, # wumpus
             g_gold_x, g_gold_y, # gold
             False, # gold
             True,  # arrow
             True,  # alive
             g_adventurer_x, g_adventurer_y, # adventurer
             ]

def testCellContainsWumpus():
    error = 0
    data = good_sample_data(g_width, g_height, g_cell_size)
    
    fname = "cellContainsWumpus"
    for y in range(g_height):
        for x in range(g_width):
            r = (g_wumpus_x == x) and (g_wumpus_y == y)
            try:
                v = wumpus_logic.cellContainsWumpus(data, x, y)
            except NameError as e:
                show_error(fname, str(e))
                error += 1
            except AttributeError as e:
                show_error(fname, str(e))
                error += 1
            except:
                print "Unexpected error:", sys.exc_info()[0]
            else:
                error += testBool(v, fname, "(%d,%d)" % (x,y), r)
    return error

def testCellContainsGold():
    error = 0
    data = good_sample_data(g_width, g_height, g_cell_size)
    
    fname = "cellContainsGold"
    for y in range(g_height):
        for x in range(g_width):
            r = (g_gold_x == x) and (g_gold_y == y)
            try:
                v = wumpus_logic.cellContainsGold(data, x, y)
            except NameError as e:
                show_error(fname, str(e))
                error += 1
            except AttributeError as e:
                show_error(fname, str(e))
                error += 1
            except:
                print "Unexpected error:", sys.exc_info()[0]
            else:
                error += testBool(v, fname, "(%d,%d)" % (x,y), r)
    return error


def testCellContainsPit():
    error = 0
    data = good_sample_data(g_width, g_height, g_cell_size)
    
    fname = "cellContainsPit"
    for y in range(g_height):
        for x in range(g_width):
            r = (g_pit_x == x) and (g_pit_y == y)
            try:
                v = wumpus_logic.cellContainsPit(data, x, y)
            except NameError as e:
                show_error(fname, str(e))
                error += 1
            except AttributeError as e:
                show_error(fname, str(e))
                error += 1
            except:
                print "Unexpected error:", sys.exc_info()[0]
            else:
                error += testBool(v, fname, "(%d,%d)" % (x,y), r)
    return error


def testCellIsVisible():
    error = 0
    data = good_sample_data(g_width, g_height, g_cell_size)
    
    fname = "cellIsVisible"
    for y in range(g_height):
        for x in range(g_width):
            r = (g_visible_x == x) and (g_visible_y == y)
            try:
                v = wumpus_logic.cellIsVisible(data, x, y)
            except NameError as e:
                show_error(fname, str(e))
                error += 1
            except AttributeError as e:
                show_error(fname, str(e))
                error += 1
            except:
                print "Unexpected error:", sys.exc_info()[0]
            else:
                error += testBool(v, fname, "(%d,%d)" % (x,y), r)
    return error


def testCellIsInCavern():
    error = 0
    data = good_sample_data(g_width, g_height, g_cell_size)
    
    fname = "cellIsInCavern"
    for y in range(-1,g_height+1):
        for x in range(-1,g_width+1):
            r = ((x >= 0 and x < g_width) and
                 (y >= 0 and y < g_height))
            try:
                v = wumpus_logic.cellIsInCavern(data, x, y)
            except NameError as e:
                show_error(fname, str(e))
                error += 1
            except AttributeError as e:
                show_error(fname, str(e))
                error += 1
            except:
                print "Unexpected error:", sys.exc_info()[0]
            else:
                error += testBool(v, fname, "(%d,%d)" % (x,y), r)
    return error

def testNeighborCellIsVisible():
    error = 0
    data = good_sample_data(g_width, g_height, g_cell_size)
    
    fname = "neighborCellIsVisible"
    for y in range(g_height):
        for x in range(g_width):
            r = (abs(g_visible_x - x) + abs(g_visible_y - y)) == 1
            try:
                v = wumpus_logic.neighborCellIsVisible(data, x, y)
            except NameError as e:
                show_error(fname, str(e))
                error += 1
            except AttributeError as e:
                show_error(fname, str(e))
                error += 1
            except:
                print "Unexpected error:", sys.exc_info()[0]
            else:
                error += testBool(v, fname, "(%d,%d)" % (x,y), r)
    return error



def testNeighborCellContainsPit():
    error = 0
    data = good_sample_data(g_width, g_height, g_cell_size)
    
    fname = "neighborCellContainsPit"
    for y in range(g_height):
        for x in range(g_width):
            r = (abs(g_pit_x - x) + abs(g_pit_y - y)) == 1
            try:
                v = wumpus_logic.neighborCellContainsPit(data, x, y)
            except NameError as e:
                show_error(fname, str(e))
                error += 1
            except AttributeError as e:
                show_error(fname, str(e))
                error += 1
            except:
                print "Unexpected error:", sys.exc_info()[0]
            else:
                error += testBool(v, fname, "(%d,%d)" % (x,y), r)
    return error


def testNeighborCellContainsWumpus():
    error = 0
    data = good_sample_data(g_width, g_height, g_cell_size)
    
    fname = "neighborCellContainsWumpus"
    for y in range(g_height):
        for x in range(g_width):
            r = (abs(g_wumpus_x - x) + abs(g_wumpus_y - y)) == 1
            try:
                v = wumpus_logic.neighborCellContainsWumpus(data, x, y)
            except NameError as e:
                show_error(fname, str(e))
                error += 1
            except AttributeError as e:
                show_error(fname, str(e))
                error += 1
            except:
                print "Unexpected error:", sys.exc_info()[0]
            else:
                error += testBool(v, fname, "(%d,%d)" % (x,y), r)
    return error


def testSetCellVisible():
    error = 0
    data = good_sample_data(g_width, g_height, g_cell_size)
    
    fname = "setCellVisible"
    for y in range(g_height):
        for x in range(g_width):
            r = True
            try:
                wumpus_logic.setCellVisible(data, x, y)
                v = wumpus_logic.cellIsVisible(data, x, y)
            except NameError as e:
                show_error(fname, str(e))
                error += 1
            except AttributeError as e:
                show_error(fname, str(e))
                error += 1
            except:
                print "Unexpected error:", sys.exc_info()[0]
            else:
                error += testBool(v, fname, "(%d,%d)" % (x,y), r)
    return error



def testVisitCell():
    error = 0
    data = good_sample_data(g_width, g_height, g_cell_size)

    # test the cellContainsPit test,
    #      the cellContainsWumpus test, and
    #      the cellContainsGold test
    # try to click left, right, above, and below the visible cell
    delta = [ (True,  True,  False, False, False), # pit,  wumpus,  !gold
              (True,  True,  True,  False, False), # pit,  wumpus,  gold
              (True,  False, False, False, False), # pit,  !wumpus, !gold
              (True,  False, True,  False, False), # pit,  !wumpus, gold
              (False, True,  False, False, False), # !pit, wumpus,  !gold
              (False, True,  True,  False, False), # !pit, wumpus,  gold
              (False, False, False, True,  False), # !pit, !wumpus, !gold
              (False, False, True,  True,  True ), # !pit, !wumpus, gold
              ]
    
    fname0 = "visitCell"
    x = 2
    y = 1
    i = x + y * g_width
    for (contains_pit, contains_wumpus, contains_gold, is_alive, have_gold) in delta:
        fname = "%s(Pit:%s, Wumpus:%s, Gold:%s)" % (fname0, str(contains_pit), str(contains_wumpus), str(contains_gold))
        wumpus_data.getPits(data)[i] = contains_pit
        if contains_wumpus:
            wumpus_data.setWumpusPosition(data, x, y)
        else:
            wumpus_data.setWumpusPosition(data, x-1, y-1)
        if contains_gold:
            wumpus_data.setGoldPosition(data, x, y)
        else:
            wumpus_data.setGoldPosition(data, x-1, y-1)
        wumpus_data.setIsAlive(data, True)
        wumpus_data.setHaveGold(data, False)
        try:
            wumpus_logic.visitCell(data, x, y)
            v1 = wumpus_logic.cellIsVisible(data, x, y)
            v2 = wumpus_data.getIsAlive(data)
            v3 = wumpus_data.getHaveGold(data)
        except NameError as e:
            show_error(fname, str(e))
            error += 1
        except AttributeError as e:
            show_error(fname, str(e))
            error += 1
        except:
            print "Unexpected error:", sys.exc_info()[0]
        else:
            error += testBool(v1, fname, "cellIsVisible", True)
            error += testBool(v2, fname, "getIsAlive", is_alive)
            error += testBool(v3, fname, "getHaveGold", have_gold)

    return error


def testHandleMouseClick():
    error = 0
    data = good_sample_data(g_width, g_height, g_cell_size)

    # test the cell calculation,
    #      the neighborCellIsVisible test,
    #      the getIsAlive test,
    #      the not getHaveGold test,
    #      the setAdventurerPosition call, and
    #      the visitCell call
    # try to click left, right, above, and below the visible cell
    delta = [ (1, 0, False, False, False), # is dead
              (1, 0, False, True, True),   # has gold
              (1, 0, False, False, True),  # is dead and has gold
              # bad directions
              (-1, -1, False, True, False),
              (-1, 1, False, True, False),
              (1, -1, False, True, False),
              (1, 1, False, True, False),
              # good directions
              (-1, 0, True, True, False),
              (1, 0, True, True, False),
              (0, -1, True, True, False),
              (0, 1, True, True, False),
              ]
    
    fname = "handleMouseClick"
    for (dx, dy, legal, is_alive, have_gold) in delta:
        if dx > 0: dxp = g_cell_size
        else: dxp = dx
        if dy > 0: dyp = g_cell_size
        else: dyp = dy
        pixel_x = g_visible_x*g_cell_size + dxp
        pixel_y = g_visible_y*g_cell_size + dyp
        cell_x  = g_visible_x + dx
        cell_y  = g_visible_y + dy
        ax_shouldbe = -1
        ay_shouldbe = -1
        wumpus_data.setAdventurerPosition(data, ax_shouldbe, ay_shouldbe)
        wumpus_data.setIsAlive(data, is_alive)
        wumpus_data.setHaveGold(data, have_gold)
        if legal:
            ax_shouldbe = cell_x
            ay_shouldbe = cell_y
        r = legal
        try:
            wumpus_logic.handleMouseClick(data, pixel_x, pixel_y)
            v1 = wumpus_logic.cellIsVisible(data, cell_x, cell_y)
            ax,ay = wumpus_data.getAdventurerPosition(data)
        except NameError as e:
            show_error(fname, str(e))
            error += 1
        except AttributeError as e:
            show_error(fname, str(e))
            error += 1
        except:
            print "Unexpected error:", sys.exc_info()[0]
        else:
            error += testBool(v1, fname, "cellIsVisible(%d,%d)" % (dx,dy), r)
            error += testInt(ax, fname, "getAdventurerPosition(%d,%d)x" % (dx,dy), ax_shouldbe, ax_shouldbe)
            error += testInt(ay, fname, "getAdventurerPosition(%d,%d)y" % (dx,dy), ay_shouldbe, ay_shouldbe)

    return error



def main():
    error = 0
    error += testCellContainsWumpus()
    error += testCellContainsGold()
    error += testCellContainsPit()
    error += testCellIsVisible()
    error += testCellIsInCavern()
    error += testNeighborCellIsVisible()
    error += testNeighborCellContainsPit()
    error += testNeighborCellContainsWumpus()
    error += testSetCellVisible()
    error += testVisitCell()
    error += testHandleMouseClick()

    print
    if error == 0:
        print "All tests succeeded."
    else:
        print "One or more errors occurred."

if __name__ == "__main__":
    main()
