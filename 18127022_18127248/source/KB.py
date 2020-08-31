from utils import *
import random

map, lst_cells, height, width, start, pits, wumpus, breeze, stench, golds, breeze_stench, emptys, golds_breeze_stench, golds_breeze, golds_stench, visible = read_file('1.txt')

def meet_state(curr_pos, visible_cells, height, width):
    right_pos, left_pos, up_pos, down_pos = find_near_cell(curr_pos, height, width)
    # if visible true -> no pit/no wumpus
    right, left, up, down = True, True, True, True
    if visible_cells[right_pos] == True:
        right = False
    if visible_cells[left_pos] == True:
        left = False
    if visible_cells[up_pos] == True:
        up = False
    if visible_cells[down_pos] == True:
        down = False
    return (right_pos, right), (left_pos, left), (up_pos, up), (down_pos, down)

# generate the inference sentence
def generate_thinking(curr_pos, state, height, width, visible_cells):
    right_cell, left_cell, up_cell, down_cell = meet_state(curr_pos, visible_cells, height, width)
    if state != 'A' and state != '-' and state != 'G':
        if state == 'B' or state == 'BG':
            state, know = 'B', 'P'
        if state == 'S' or state == 'GS':
            state, know = 'S', 'W'
        curr, right, left, up, down = vars(f'{state}{curr_pos}', 
                                            f'{know}{right_cell[0]}',
                                            f'{know}{left_cell[0]}',
                                            f'{know}{up_cell[0]}',
                                            f'{know}{down_cell[0]}')
        return curr.iff(right|left|up|down), [right, left, up, down]
        # right, left, up, down are the propositional sentence need to be infered from KB
    else:
        state_01, know_01 = 'B', 'P'
        state_02, know_02 = 'S', 'W'
        curr, right, left, up, down = vars(f'{state_01}{curr_pos}', 
                                            f'{know_01}{right_cell[0]}',
                                            f'{know_01}{left_cell[0]}',
                                            f'{know_01}{up_cell[0]}',
                                            f'{know_01}{down_cell[0]}')
        formula_01 = (~curr).iff(~right & ~left & ~up & ~down)
        curr, right, left, up, down = vars(f'{state_02}{curr_pos}', 
                                            f'{know_02}{right_cell[0]}',
                                            f'{know_02}{left_cell[0]}',
                                            f'{know_02}{up_cell[0]}',
                                            f'{know_02}{down_cell[0]}')
        formula_02 = (~curr).iff(~right & ~left & ~up & ~down)
        return formula_01, formula_02

class KB:
    # perception of the human around the cell where him stand
    def percept(self, state, height, width):
        if state == 'BS' or state == 'BGS':
            self.know_safe[self.pos] = True
            self.know_breeze[self.pos] = True
            self.know_stench[self.pos] = True
            if state == 'BGS':
                return ['Breeze', 'Gold', 'Stench']
            else: 
                return ['Breeze', None, 'Stench']
        elif state == 'B'or state == 'BG':
            self.know_safe[self.pos] = True
            self.know_breeze[self.pos] = True 
            if state == 'BG':
                return ['Breeze', 'Gold', None]
            else:
                return ['Breeze', None, None]
        elif state == 'S' or state == 'GS':
            self.know_safe[self.pos] = True
            self.know_stench[self.pos] = True
            if state == 'GS':
                return [None, 'Gold', 'Stench']
            else:
                return [None, None, 'Stench']
        elif state == '-' or state == 'G' or state == 'A':
            self.know_safe[self.pos] = True
            safe_right, safe_left, safe_up, safe_down = find_near_cell(self.pos, height, width)
            self.know_safe[safe_right] = self.know_safe[safe_left] = self.know_safe[safe_up] = self.know_safe[safe_down] = True
            if state == 'G':
                return [None, 'Gold', None]
            else:
                return [None, None, None]
    # initialize the KB for human
    def __init__(self, height, width, start, state):
        # position of the human
        self.pos = start
        # list of cell which human saw
        self.visible_cells = [False for i in range(height*width)]
        self.visible_cells[start] = True
        
        # list of cells pits human know
        self.know_pit = [False for i in range(height*width)]
        # list of cells wumpus human know
        self.know_wumpus = [False for i in range(height*width)]
        # list of cells breeze human know
        self.know_breeze = [False for i in range(height*width)]
        # list of cells stench human know
        self.know_stench = [False for i in range(height*width)]

        # list of safe cells human know
        self.know_safe = [False for i in range(height*width)]
        self.know_safe[start] = True

        safe_right, safe_left, safe_up, safe_down = find_near_cell(start, height, width)
        self.know_safe[safe_right] = self.know_safe[safe_left] = self.know_safe[safe_up] = self.know_safe[safe_down] = True

        self.thinking = []
        self.add_KB(state, height, width)
        # perception of human about the world around him
        self.percept(state, height, width)
    # inference process of the human
    def inference(self, height, width, state):
        if state == 'B' or state == 'S':
            x, y = generate_thinking(self.pos, state, height, width, self.visible_cells)
            return x
        if state == 'BS' or state == 'BGS':
            formula_01, infer_pit = generate_thinking(self.pos, 'B', height, width, self.visible_cells)
            formula_02, infer_wumpus = generate_thinking(self.pos, 'S', height, width, self.visible_cells)
            return formula_01, formula_02
        if state == 'A' or state == '-' or state == 'G':
            formula_01, formula_02 = generate_thinking(self.pos, '-', height, width, self.visible_cells)
            return formula_01, formula_02
    # add the inference of the human to the KB
    def add_KB(self, state, height, width):
        perception = self.percept(state, height, width)
        if state == 'A' or state == '-' or state == 'G' or state == 'BS' or state == 'BGS':
            x, y = self.inference(height, width, state)
            self.thinking.append(x)
            self.thinking.append(y)
        else:
            infer = self.inference(height, width, state)
            self.thinking.append(infer)
    # show the current KB of the human
    def show_KB(self):
        for i in range(len(self.thinking)):
            print(f"{self.thinking[i]}")

    def open_cell(self, meet_state):
        self.visible_cells[self.pos] = True
        self.know_safe[self.pos] = True
        if meet_state == 'B' or meet_state == 'BG':
            self.know_breeze[self.pos] = True
        if meet_state == 'S' or meet_state == 'GS':
            self.know_stench[self.pos] = True
        if meet_state == 'BGS' or meet_state == 'BS':
            self.know_breeze = self.know_stench = True

    def entail_query(self, query):
        conjunction = self.thinking[0]
        for i in range(1, len(self.thinking)):
            conjunction = conjunction & self.thinking[i]
        return ArgumentForm(conjunction, query).is_valid()
        """
        False: can't entail
        True: can entail
        """
    def decide(self):
        pass



class Human:
    def __init__(self, position_init, score=0, direction='Right', state='A', height=0, width=0):
        self.score = score
        self.direction = direction
        self.KB = KB(height, width, position_init, state)
    def move_toward_pos(self, pos, height, width):
        state_meet = lst_cells[pos]
        perception = self.KB.percept(state_meet, height, width)
        right, left, up, down = find_near_cell(self.KB.pos, height, width)
        action = ''
        if pos == right:
            action = 'Right'
        if pos == down:
            action = 'Down'
        if pos == up:
            action = 'Up'
        if pos == left:
            action = 'Left'
        if pos != self.KB.pos:
            self.KB.pos = pos
            self.KB.add_KB(lst_cells[self.KB.pos], height, width)
        self.KB.open_cell(lst_cells[self.KB.pos])
        return perception, action
        
    def move_toward_direction(self, direction='Right', height=0, width=0):
        right, left, up, down = find_near_cell(self.KB.pos, height, width)
        print(right)
        action = ''
        if direction == 'Right':
            if right != self.KB.pos:
                self.KB.pos = right
                self.KB.add_KB(lst_cells[right], height, width)
                self.score -= 10
                action = direction
            self.KB.pos = right
        if direction == 'Left':
            if left != self.KB.pos:
                self.KB.pos = left
                self.KB.add_KB(lst_cells[left], height, width)
                self.score -= 10
                action = direction
            self.KB.pos = left
        if direction == 'Down':
            if self.KB.pos != down:
                self.KB.pos = down
                self.KB.add_KB(lst_cells[down], height, width)
                self.score -= 10
                action = direction
            self.KB.pos = down
        if direction == 'Up':
            if self.KB.pos != up:
                self.KB.pos = up 
                self.KB.add_KB(lst_cells[up], height, width)
                self.score -= 10
                action = direction
            self.KB.pos = up 

        self.KB.open_cell(lst_cells[self.KB.pos])
        perception = self.KB.percept(lst_cells[self.KB.pos], height, width)

        return perception, action
    def show_all_human_KB(self):
        self.KB.show_KB()



human = Human(start, score=0, direction='Right', state='A', height=height, width=width)
for i in range(10):
    perception, action = human.move_toward_pos(i, height, width)
    human.show_all_human_KB()
    print(f'percept: {perception}, action: {action}')

        