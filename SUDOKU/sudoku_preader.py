#Sheila Robles
#Assignment 2 Problem 1
#Python Version 3.0.1

from __future__ import print_function
import time
start_time = time.time()
puzzle_string = ""
character_list = []
puzzle_list = []
list_of_needs = []
dict_of_possible_answers = {}
#------------------------------------------------#
#------------------------------------------------#
#--------GET PUZZLE INFO BOX, ROW, COLUMN--------#

def sudoku_box(x, y, plist): 
    # get a string of characters of a given box. Grid starts at the top left with 
    # (0,0) coord and ends at bottom right with (3,3) coord
    y = y * 4
    x = x * 4
    string = plist[y][x:x+4]+plist[y+1][x:x+4]+plist[y+2][x:x+4]+plist[y+3][x:x+4]
    return string 
               
def sudoku_row(y, plist):
    # get a string of characters of a given row
    string = "".join(plist[y])
    return string
    
def sudoku_column(x, plist):
    # get a string of characters of a given row
    string = ""
    for lst in plist:
        string += lst[x]
    return string

#------END GET PUZZLE INFO BOX, ROW, COLUMN------#
#------------------------------------------------#
#------------------------------------------------#
#------CHECK ONE BOX, ROW, COLUMN SOLUTION-------#

def box_solution(plist, charlst):
    # check the boxes if they're solved
    for x in range(1):
        for y in range(1):
            box = list(sudoku_box(x,y,plist))
            if set(box) != set(charlst):
                return False
            print("True at: (",x,",",y,").",sep="")
    return True    
    
def row_solution(plist, charlst):
    # check the boxes if they're solved
    for y in range(16):
        row = list(sudoku_row(y,plist))
        if set(row) != set(charlst):
            return False
        print("True at row ",y,sep="")
    return True    
    
def col_solution(plist, charlst):
    # check the boxes if they're solved
    for x in range(16):
        col = list(sudoku_column(x,plist))
        if set(col) != set(charlst):
            return False
        print("True at col ",x,sep="")
    return True
    
#------END CHECK BOX, ROW, COLUMN SOLUTIONS-----#
#-----------------------------------------------#
#-----------------------------------------------#
#------------CHECK OVERALL SOLUTION-------------#

def is_solution(plist, charlst):
    # check if the game is solved
    is_solution = box_solution(plist, charlst)
    if is_solution == False: 
        return is_solution
    is_solution = row_solution(plist, charlst)
    if is_solution == False: 
        return is_solution
    is_solution = row_solution(plist, charlst)
    if is_solution == False: 
        return is_solution        
    return True

def is_complete(x, y, plist):
    # check if the assignment is complete for the spot (x,y)
    return plist[x][y] != "-"
    
def is_consistent(x,y, plist):
    global character_list
    charlst = character_list
    # check if the assignment is consistent for the row, column, and box
    # containing the x,y coordinates
    col_row_box = [col_solution(plist, charlst)]
    col_row_box += [row_solution(plist, charlst)]
    col_row_box += [box_solution(plist, charlst)]
    for item in col_row_box:
        dict = get_characters(item)
        for key in dict.keys():
            if dict[key] > 1:
             return False
    return True
    
#----------END CHECK OVERALL SOLUTION-----------#
#-----------------------------------------------#
#-----------------------------------------------#
#--------------SOLVING FUNCTIONS----------------#

def sudoku_box_generator(x,y,plist):
    # checks the x and y values to get the values in
    # the box with that coordinate
    if x in [0,1,2,3]:
        new_x = 0
    elif x in [4,5,6,7]:
        new_x = 1
    elif x in [8,9,10,11]:
        new_x = 2
    else:
        new_x = 3
    if y in [0,1,2,3]:
        new_y = 0
    elif y in [4,5,6,7]:
        new_y = 1
    elif y in [8,9,10,11]:
        new_y = 2
    else:
        new_y = 3
    return sudoku_box(new_x, new_y, plist) #string
        
# check row, col, and box to see what value to assign
# while not is_consistent():
def available_answers(plist, coordinates):
    global character_list
    charlst = character_list
    for coordinate in coordinates:
        # get whats missing in the row, column, and box
        # check that set, if it's len 1 apply change
        r = sudoku_row(coordinate[0], plist)
        c = sudoku_column(coordinate[1], plist)
        b = sudoku_box_generator(coordinate[0], coordinate[1], plist)
        have_set = set(r) | set(c) | set(c) - set("-")
        the_set = "".join(str(char) for char in (set(character_list) - have_set)) # possible str conversion
        dict_of_possible_answers[(coordinate[0], coordinate[1]) ] = the_set
    return dict_of_possible_answers #with str solutions

def select_unassigned(plist):
    available = available_answers(plist, list_of_needs)
    for key in available.keys():
        for lst in available[key]:
            return lst

#--------------END SOLVING FUNCTIONS------------#
#-----------------------------------------------#
#-----------------------------------------------#
#------GAME RELATED FUNCTIONS AND GETTERS-------#

def set_list_of_needs(coord_of_needs):
    global list_of_needs
    # set up in col, row
    list_of_needs += [coord_of_needs]

def find_needed_spots(plist):
    # check coordinates of blank spots and sets the list of coordinates
    for row in range(len(plist)):
        for col in range(len(plist)):
            if plist[row][col] == "-":
                set_list_of_needs((row, col))

def show_game(lst):
    # print a visually appealing version of the puzzle
    string = "+---------------------------------------+"
    do_once = True
    char_index = 0
    
    for row in lst:
        string += "\n|"
        for r in range(len(row)):
            if lst.index(row) in [4,8,12] and do_once:
               string += "---------+---------+---------+---------|\n|"
               do_once = False
            elif char_index in [4,8,12,16]:
                string += " |"
            string += " " + row[r]
            char_index += 1
        do_once = True
        char_index = 0
        string += " |"
    string += "\n+---------------------------------------+"
    print(string)

def get_characters(string):
    # counts the frequency of each character in string
    # store and return count in a dictionary
    letter_frequency = {}
    
    for character in string:
        if character not in letter_frequency:
            letter_frequency[character] = 0
        letter_frequency[character] += 1
    letter_frequency.pop("\n", None)
    letter_frequency.pop("-", None)
    return letter_frequency
    
def add_chars(lst): 
    # add characters to the character list if there aren't enough defined
    list_of_chars = "123456789ABCDEFG"
    while len(lst) < 16:
        for item in list_of_chars:
            if item not in lst:
                lst += item
    return lst # now a str
    
#-----END GAME RELATED FUNCTIONS AND GETTERS-----#
#------------------------------------------------#
#------------------------------------------------#
#-------------Backtracking-----------------------#

def BACKTRACKINGSEARCH(csp):# returns a solution, or failure
   return BACKTRACK({ }, csp)

def BACKTRACK(assignment,csp):
    if is_complete(assignment[0], assignment[1], csp):
        return assignment
    var = select_unassigned(csp)
    for value in order_domain_values(var):
        if is_consistent(var, assignment, csp):
            csp[assignment[0]][assignment[1]] = value
            inferences = inferences(var, value)
            if inferences:
                csp[assignment[0]][assignment[1]] = value
                result = BACKTRACK(assignment, csp)
                if not result:
                    return result
        var = var.replace(value, "")
    return False

def inference(var, value):
    if var in value:
        return True

def order_domain_values(var):
    for v in var:
        return v


#--------------end backtracking------------------#
#------------------------------------------------#
#------------------------------------------------#
#------------------------------------------------#
#---------------INITIALIZE VARIABLES-------------#


#-----------END INITIALIZE CHARACTERS------------#
#------------------------------------------------#
#------------------------------------------------#
#-------------GET THE SUDOKU PUZZLE--------------#
def getSudokuPuzzle():
    f = open('SudokuPuzzle3.txt', 'r')
    puzzle_string = f.read()
    f.close()
    return [puzzle_string, puzzle_string.splitlines()] # get all the lines from the file

def checkIfValid(puzzleList):
    if len(puzzle_list) == 16:
        game_string = show_game(puzzle_list)
        print(game_string)
    else:
        print(puzzle_list)
        print("invalid file")

def reget_info(csp):
    if not is_solution(csp):
        return available_answers(csp)
    return True



#----------END GET THE SUDOKU PUZZLE-------------#
#------------------------------------------------#
#------------------------------------------------#
#-------------TESTING ENVIRONMENT----------------#


#CHECK IF PUZZLE IS VALID AND PASS IT TO THE SHOW GAME FUNCTION
#TESTING GET CHARACTERS
puzzle_string, puzzle_list = getSudokuPuzzle()
checkIfValid(puzzle_list)

solution_list = get_characters(puzzle_string)
character_list = list(solution_list.keys())

if len(character_list) != 16:
    character_list = add_chars(character_list)#add more characters to the list
print("".join(str(character_list)))

#TESTING GET LIST OF AVAILABLE COORDINATES
find_needed_spots(puzzle_list)
possible_values = available_answers(puzzle_list, list_of_needs)
print(possible_values)

BACKTRACKINGSEARCH(puzzle_string)

print("--- %s seconds ---" % (time.time() - start_time))
