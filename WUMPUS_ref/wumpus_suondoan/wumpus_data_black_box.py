import sys
import wumpus_data

def good_sample_data(width, height, cell_size):
    return [ width,
             height,
             cell_size,
             [ (x%2)!=0 for x in range(width*height)],
             [ x==0 for x in range(width*height)],
             1, 2,
             3, 4,
             False,
             True,
             True,
             0, 0 
             ]
def bad_sample_data(width, height, cell_size):
    return [ width-1,
             height+1,
             cell_size/2,
             [True for x in range(width*height)],
             [True for x in range(width*height)],
             0, 0,
             0, 0,
             True,
             False,
             False,
             1,
             2 
             ]

def show_error(fname, msg):
    print "Error:   %s: %s" % (fname, msg)
def show_ok(fname, msg):
    #print "Success: %s: %s" % (fname, msg)
    pass

def testDimensions():
    error = 0
    width, height, cell_size = 4, 5, 6
    width2, height2, cell_size2 = 7, 8, 9
    data = good_sample_data(width, height, cell_size)
    
    fname = "getDimensions"
    try:
        (w, h) = wumpus_data.getDimensions(data)
    except NameError as e:
        show_error(fname, str(e))
        error += 1
    except AttributeError as e:
        show_error(fname, str(e))
        error += 1
    except:
        print "Unexpected error:", sys.exc_info()[0]
    else:
        error += testInt(w, fname, "data[0]:width", width, width)
        error += testInt(h, fname, "data[1]:height", height, height)

    fname = "setDimensions"
    try:
        wumpus_data.setDimensions(data, width2, height2)
    except NameError as e:
        show_error(fname, str(e))
        error += 1
    except AttributeError as e:
        show_error(fname, str(e))
        error += 1
    except:
        print "Unexpected error:", sys.exc_info()[0]
    else:
        error += testInt(data[0], fname, "data[0]:width", width2, width2)
        error += testInt(data[1], fname, "data[1]:height", height2, height2)

    return error
    
def testCellSize():
    error = 0
    width, height, cell_size = 4, 5, 6
    width2, height2, cell_size2 = 7, 8, 9
    data = good_sample_data(width, height, cell_size)
    
    fname = "getCellSize"
    try:
        c = wumpus_data.getCellSize(data)
    except NameError as e:
        show_error(fname, str(e))
        error += 1
    except AttributeError as e:
        show_error(fname, str(e))
        error += 1
    except:
        print "Unexpected error:", sys.exc_info()[0]
    else:
        error += testInt(c, fname, "data[2]:cell_size", cell_size, cell_size)

    fname = "setCellSize"
    try:
        wumpus_data.setCellSize(data, cell_size2)
    except NameError as e:
        show_error(fname, str(e))
        error += 1
    except AttributeError as e:
        show_error(fname, str(e))
        error += 1
    except:
        print "Unexpected error:", sys.exc_info()[0]
    else:
        error += testInt(data[2], fname, "data[2]:cell_size", cell_size2, cell_size2)

    return error


def testPits():
    error = 0
    width, height, cell_size = 4, 5, 6
    width2, height2, cell_size2 = 7, 8, 9
    data = good_sample_data(width, height, cell_size)
    data2 = bad_sample_data(width2, height2, cell_size2)
    
    fname = "getPits"
    try:
        pits = wumpus_data.getPits(data)
    except NameError as e:
        show_error(fname, str(e))
        error += 1
    except AttributeError as e:
        show_error(fname, str(e))
        error += 1
    except:
        print "Unexpected error:", sys.exc_info()[0]
    else:
        error += testList(pits, fname, "data[3]:pits", width*height)
        if error == 0:
            for i in range(len(pits)):
                error += testBool(pits[i], fname, "data[3][%d]:pits[%d]" % (i, i), data[3][i])

    fname = "setPits"
    try:
        wumpus_data.setPits(data, data2[3])
    except NameError as e:
        show_error(fname, str(e))
        error += 1
    except AttributeError as e:
        show_error(fname, str(e))
        error += 1
    except:
        print "Unexpected error:", sys.exc_info()[0]
    else:
        error += testList(data[3], fname, "data[3]:pits", width2*height2)
        if error == 0:
            for i in range(len(data[3])):
                error += testBool(data[3][i], fname, "data[3][%d]:pits[%d]" % (i, i), data2[3][i])

    return error


def testVisible():
    error = 0
    width, height, cell_size = 4, 5, 6
    width2, height2, cell_size2 = 7, 8, 9
    data = good_sample_data(width, height, cell_size)
    data2 = bad_sample_data(width2, height2, cell_size2)
    
    fname = "getVisible"
    try:
        visible = wumpus_data.getVisible(data)
    except NameError as e:
        show_error(fname, str(e))
        error += 1
    except AttributeError as e:
        show_error(fname, str(e))
        error += 1
    except:
        print "Unexpected error:", sys.exc_info()[0]
    else:
        error += testList(visible, fname, "data[4]:visible", width*height)
        if error == 0:
            for i in range(len(visible)):
                error += testBool(visible[i], fname, "data[4][%d]:visible[%d]" % (i, i), data[4][i])

    fname = "setVisible"
    try:
        wumpus_data.setVisible(data, data2[4])
    except NameError as e:
        show_error(fname, str(e))
        error += 1
    except AttributeError as e:
        show_error(fname, str(e))
        error += 1
    except:
        print "Unexpected error:", sys.exc_info()[0]
    else:
        error += testList(data[4], fname, "data[4]:visible", width2*height2)
        if error == 0:
            for i in range(len(data[4])):
                error += testBool(data[4][i], fname, "data[4][%d]:visible[%d]" % (i, i), data2[4][i])

    return error


def testWumpusPosition():
    error = 0
    width, height, cell_size = 4, 5, 6
    width2, height2, cell_size2 = 7, 8, 9
    data = good_sample_data(width, height, cell_size)
    x2, y2 = data[6], data[5]
    
    fname = "getWumpusPosition"
    try:
        (x, y) = wumpus_data.getWumpusPosition(data)
    except NameError as e:
        show_error(fname, str(e))
        error += 1
    except AttributeError as e:
        show_error(fname, str(e))
        error += 1
    except:
        print "Unexpected error:", sys.exc_info()[0]
    else:
        error += testInt(x, fname, "data[5]:wumpus_x", data[5], data[5])
        error += testInt(y, fname, "data[6]:wumpus_y", data[6], data[6])

    fname = "setWumpusPosition"
    try:
        wumpus_data.setWumpusPosition(data, x2, y2)
    except NameError as e:
        show_error(fname, str(e))
        error += 1
    except AttributeError as e:
        show_error(fname, str(e))
        error += 1
    except:
        print "Unexpected error:", sys.exc_info()[0]
    else:
        error += testInt(data[5], fname, "data[5]:wumpus_x", x2, x2)
        error += testInt(data[6], fname, "data[6]:wumpus_y", y2, y2)

    return error


def testGoldPosition():
    error = 0
    width, height, cell_size = 4, 5, 6
    width2, height2, cell_size2 = 7, 8, 9
    data = good_sample_data(width, height, cell_size)
    x2, y2 = data[8], data[7]
    
    fname = "getGoldPosition"
    try:
        (x, y) = wumpus_data.getGoldPosition(data)
    except NameError as e:
        show_error(fname, str(e))
        error += 1
    except AttributeError as e:
        show_error(fname, str(e))
        error += 1
    except:
        print "Unexpected error:", sys.exc_info()[0]
    else:
        error += testInt(x, fname, "data[7]:gold_x", data[7], data[7])
        error += testInt(y, fname, "data[8]:gold_y", data[8], data[8])

    fname = "setGoldPosition"
    try:
        wumpus_data.setGoldPosition(data, x2, y2)
    except NameError as e:
        show_error(fname, str(e))
        error += 1
    except AttributeError as e:
        show_error(fname, str(e))
        error += 1
    except:
        print "Unexpected error:", sys.exc_info()[0]
    else:
        error += testInt(data[7], fname, "data[7]:gold_x", x2, x2)
        error += testInt(data[8], fname, "data[8]:gold_y", y2, y2)

    return error


def testHaveGold():
    error = 0
    width, height, cell_size = 4, 5, 6
    width2, height2, cell_size2 = 7, 8, 9
    data = good_sample_data(width, height, cell_size)
    v2 = not data[9]

    fname = "getHaveGold"
    try:
        v = wumpus_data.getHaveGold(data)
    except NameError as e:
        show_error(fname, str(e))
        error += 1
    except AttributeError as e:
        show_error(fname, str(e))
        error += 1
    except:
        print "Unexpected error:", sys.exc_info()[0]
    else:
        error += testBool(v, fname, "data[9]:have_gold", data[9])

    fname = "setHaveGold"
    try:
        wumpus_data.setHaveGold(data, v2)
    except NameError as e:
        show_error(fname, str(e))
        error += 1
    except AttributeError as e:
        show_error(fname, str(e))
        error += 1
    except:
        print "Unexpected error:", sys.exc_info()[0]
    else:
        error += testBool(data[9], fname, "data[9]:have_gold", v2)

    return error



def testHaveArrow():
    error = 0
    width, height, cell_size = 4, 5, 6
    width2, height2, cell_size2 = 7, 8, 9
    data = good_sample_data(width, height, cell_size)
    v2 = not data[10]

    fname = "getHaveArrow"
    try:
        v = wumpus_data.getHaveArrow(data)
    except NameError as e:
        show_error(fname, str(e))
        error += 1
    except AttributeError as e:
        show_error(fname, str(e))
        error += 1
    except:
        print "Unexpected error:", sys.exc_info()[0]
    else:
        error += testBool(v, fname, "data[10]:have_arrow", data[10])

    fname = "setHaveArrow"
    try:
        wumpus_data.setHaveArrow(data, v2)
    except NameError as e:
        show_error(fname, str(e))
        error += 1
    except AttributeError as e:
        show_error(fname, str(e))
        error += 1
    except:
        print "Unexpected error:", sys.exc_info()[0]
    else:
        error += testBool(data[10], fname, "data[10]:have_arrow", v2)

    return error





def testIsAlive():
    error = 0
    width, height, cell_size = 4, 5, 6
    width2, height2, cell_size2 = 7, 8, 9
    data = good_sample_data(width, height, cell_size)
    v2 = not data[11]

    fname = "getIsAlive"
    try:
        v = wumpus_data.getIsAlive(data)
    except NameError as e:
        show_error(fname, str(e))
        error += 1
    except AttributeError as e:
        show_error(fname, str(e))
        error += 1
    except:
        print "Unexpected error:", sys.exc_info()[0]
    else:
        error += testBool(v, fname, "data[11]:is_alive", data[11])

    fname = "setIsAlive"
    try:
        wumpus_data.setIsAlive(data, v2)
    except NameError as e:
        show_error(fname, str(e))
        error += 1
    except AttributeError as e:
        show_error(fname, str(e))
        error += 1
    except:
        print "Unexpected error:", sys.exc_info()[0]
    else:
        error += testBool(data[11], fname, "data[11]:is_alive", v2)

    return error





def testAdventurerPosition():
    error = 0
    width, height, cell_size = 4, 5, 6
    width2, height2, cell_size2 = 7, 8, 9
    data = good_sample_data(width, height, cell_size)
    x2, y2 = data[13], data[12]
    
    fname = "getAdventurerPosition"
    try:
        (x, y) = wumpus_data.getAdventurerPosition(data)
    except NameError as e:
        show_error(fname, str(e))
        error += 1
    except AttributeError as e:
        show_error(fname, str(e))
        error += 1
    except:
        print "Unexpected error:", sys.exc_info()[0]
    else:
        error += testInt(x, fname, "data[12]:adventurer_x", data[12], data[12])
        error += testInt(y, fname, "data[13]:adventurer_y", data[13], data[13])

    fname = "setAdventurerPosition"
    try:
        wumpus_data.setAdventurerPosition(data, x2, y2)
    except NameError as e:
        show_error(fname, str(e))
        error += 1
    except AttributeError as e:
        show_error(fname, str(e))
        error += 1
    except:
        print "Unexpected error:", sys.exc_info()[0]
    else:
        error += testInt(data[12], fname, "data[12]:adventurer_x", x2, x2)
        error += testInt(data[13], fname, "data[13]:adventurer_y", y2, y2)

    return error




def testInt(x, fname, vname, minimum, maximum):
    if not (type(x) == type(1)):
        show_error(fname, "%s should be an int, is a %s." % (vname, type(x).__name__))
        return 1
    else:
        show_ok(fname, "%s is an int." % (vname))
        if x < minimum or x > maximum:
            show_error(fname, "%s(%d) should be between %d and %d." % (vname, x, minimum, maximum))
            return 1
        else:
            show_ok(fname, "%s(%d) is between %d and %d." % (vname, x, minimum, maximum))
            return 0

def testBool(x, fname, vname, value):
    if not (type(x) == type(True)):
        show_error(fname, "%s should be a boolean, is a %s." % (vname, type(x).__name__))
        return 1
    else:
        show_ok(fname, "%s is a boolean." % (vname))
        if x != value:
            show_error(fname, "%s(%s) should be %s." % (vname, str(x), str(value)))
            return 1
        else:
            show_ok(fname, "%s(%s) is %s." % (vname, str(x), str(value)))
            return 0

def testList(x, fname, vname, size):
    if not (type(x) == type([])):
        show_error(fname, "%s should be a list, is a %s." % (vname, type(x).__name__))
        return 1
    else:
        if len(x) != size:
            show_error(fname, "%s should be a list of length %d, is of length %d." % (vname, size, len(x)))
            return 1
        else:
            show_ok(fname, "%s is a list of length %d." % (vname, size))
            return 0

g_MAX_INIT_TEST = 10        
g_no_pits_count = 0        
def testPitsList(x, fname, vname, size):
    global g_no_pits_count
    error = testList(x, fname, vname, size)
    if error == 0:
        if x[0]:
            show_error(fname, "%s 0,0 should not have a pit." % (vname))
            error += 1
        count = 0
        for p in x:
            if p: count += 1
        if count < 1:
            g_no_pits_count += 1
            if g_no_pits_count > g_MAX_INIT_TEST/2:
                show_error(fname, "%s No pits found." % (vname))
                error += 1
        if count >= size - 1:
            show_error(fname, "%s All pits found. Possible error." % (vname))
            error += 1
    return error

def testVisibleList(x, fname, vname, size):
    error = testList(x, fname, vname, size)
    if error == 0:
        if not x[0]:
            show_error(fname, "%s 0,0 should be visible." % (vname))
            error += 1
        count = 0
        for p in x:
            if p: count += 1
        if count != 1:
            show_error(fname, "%s Only 0,0 should be visible." % (vname))
            error += 1
    return error

def testInitializeDataAux():
    fname = "initializeData"
    width, height, cell_size, debug = 4, 4, 100, 0

    try:
        data = wumpus_data.initializeData(width, height, cell_size, debug)
    except NameError as e:
        show_error(fname, str(e))
        return 1
    except AttributeError as e:
        show_error(fname, str(e))
        return 1
    except:
        print "Unexpected error:", sys.exc_info()[0]
    
    int_members = [ (0,  "width",        testInt, width, width),
                    (1,  "height",       testInt, height, height),
                    (2,  "cell_size",    testInt, cell_size, cell_size),
                    (5,  "wumpus_x",     testInt, 0, width-1),
                    (6,  "wumpus_y",     testInt, 0, height-1),
                    (7,  "gold_x",       testInt, 0, width-1),
                    (8,  "gold_y",       testInt, 0, height-1),
                    (12, "adventurer_x", testInt, 0, 0),
                    (13, "adventurer_y", testInt, 0, 0),
                    ]
    bool_members = [ (9,  "have_gold",    testBool, False),
                     (10, "have_arrow",   testBool, True),
                     (11, "is_alive",     testBool, True),
                     ]
    list_members = [ (3,  "pits",         testPitsList),
                     (4,  "visible",      testVisibleList),
                     ]

    #data = bad_sample_data(width, height, cell_size)
    #data = good_sample_data(width, height, cell_size)
    
    errors = 0
    errors += testList(data, fname, "data", 14)
    for (i, vname, test, minimum, maximum) in int_members:
        if len(data) > i:
            errors += test(data[i], fname, "data[%d]:%s" % (i, vname), minimum, maximum)
    if len(data) > 6:
        wx = data[5]
        wy = data[6]
        if wx == 0 and wy == 0:
            show_error(fname, "wumpus should not be located at 0,0")
    if len(data) > 8:
        gx = data[7]
        gy = data[8]
        if gx == 0 and gy == 0:
            show_error(fname, "gold should not be located at 0,0")
    for (i, vname, test, value) in bool_members:
        if len(data) > i:
            errors += test(data[i], fname, "data[%d]:%s" % (i, vname), value)
    for (i, vname, test) in list_members:
        if len(data) > i:
            errors += test(data[i], fname, "data[%d]:%s" % (i, vname), width*height)
    return errors

def testInitializeData():
    error = 0
    for i in range(g_MAX_INIT_TEST):
        error += testInitializeDataAux()
    return error

def main():
    error = 0
    error += testInitializeData()
    if error == 0:
        error += testDimensions()
        error += testCellSize()
        error += testPits()
        error += testVisible()
        error += testWumpusPosition()
        error += testGoldPosition()
        error += testHaveGold()
        error += testHaveArrow()
        error += testIsAlive()
        error += testAdventurerPosition()

    print
    if error == 0:
        print "All tests succeeded."
    else:
        print "One or more errors occurred."

if __name__ == "__main__":
    main()
