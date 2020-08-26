from game_mouse   import Game
from wumpus_data  import *
from wumpus_logic import *
from wumpus_draw  import *

class Wumpus(Game):

    def __init__(self, cells_width, cells_height, cell_size, data):
        self.cells_width  = cells_width
        self.cells_height = cells_height
        self.cell_size    = cell_size

        Game.__init__(self, "Find the Gold",
                      self.cells_width*self.cell_size,
                      self.cells_height*self.cell_size,
                      10)
        self.data = data
        loadImages()
        
    def game_logic(self, keys, newkeys, buttons, newbuttons, mouse_position):
        x = mouse_position[0]
        y = mouse_position[1]
        if 1 in newbuttons:
            handleMouseClick(self.data, x, y)
        
    def paint(self, surface):
        updateDisplay(surface, self.data)

#
# Initialize the graphics and wumpus world data.
# Launch the event processing loop
#
def main(debug=0):
    CELL_SIZE = 100
    WIDTH     = 4
    HEIGHT    = 4
    
    data = initializeData(WIDTH, HEIGHT, CELL_SIZE, debug)
    w = Wumpus(WIDTH, HEIGHT, CELL_SIZE, data)
    w.main_loop()
   
if __name__ == "__main__":
    main()

