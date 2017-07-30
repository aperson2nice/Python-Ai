import random
points = 0

def boardGenerator():
    # 2 for DOUBLE WORD, 3 for TRIPLE WORD, @ for double letter, # for triple letter
    # - for NORMAL
    board = '3--@---3---@--3\n' \
            '-2---#---#---2-\n' \
            '--2---@-@---2--\n' \
            '@--2---@---2--@\n' \
            '----2-----2----\n' \
            '-#---#---#---#-\n' \
            '--@---@-@---@--\n' \
            '3--@---2---@--3\n' \
            '--@---@-@---@--\n' \
            '-#---#---#---#-\n' \
            '----2-----2----\n' \
            '@--2---@---2--@\n' \
            '--2---@-@---2--\n' \
            '-2---#---#---2-\n' \
            '3--@---3---@--3\n'
    return board

def doubleWordBonus(word):
    sum = 0
    for letter in word:
        sum += pointValue(letter)
    return sum * 2


def pointValue(letter):
    # check the point value of letters
    if letter in 'EAIONRTLSU': return 1
    elif letter in 'DG': return 2
    elif letter in 'BCMP': return 3
    elif letter in 'FHVWY': return 4
    elif letter in 'K': return 5
    elif letter in 'JX': return 8
    elif letter in 'QZ': return 10
    else: return 0

def allLetters():
    letters = "EEEEEEEEEEEEAAAAAAAAAIIIIIIIIIOOOOOOOO" \
              "NNNNNNRRRRRRTTTTTTLLLLSSSSUUUU" \
              "DDDDGGGBBCCMMPPFFHHVVWWYYKJXQZ__"
    return random.choice(list(letters))

def getPieces():
    pieces=""
    while len(pieces) < 7:
        pieces += allLetters()
    return pieces
