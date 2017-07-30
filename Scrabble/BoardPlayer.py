import ScrabbleBoard



def placeLetters(word, position, length):
    board = ScrabbleBoard.boardGenerator().split()
    temp = []
    if position in "L":
        for letter in word:
            temp = list(board[7])
            temp[7 - length] = letter
            board[7] = "".join(temp)
            length -= 1
    elif position == "R":
        for letter in word:
            temp = list(board[7])
            temp[7 + length] = letter
            board[7] = "".join(temp)
            length += 1
    elif position == "T":
        for letter in word:
            temp = list(board[7 - length])
            temp[7] = letter
            board[7 - length] = "".join(temp)
            length -= 1
    elif position == "B":
        for letter in word:
            temp = list(board[7 + length])
            temp[7] = letter
            board[7 + length] = "".join(temp)
            length += 1
    for row in board:
        print(" ".join(list(row)))
    print("POINT TOTAL: ", ScrabbleBoard.points)



def checkIfWordinWord(word):
    f = open('SOWPODS_complete.txt', 'r')
    while word != "" and True:
        new_word = f.readline()
        if word in new_word:
            break
    f.close()
    return(new_word)


def containsMultipleVowels(word):
    vowel_count = 0
    for letter in word:
        if ScrabbleBoard.pointValue(letter) in [1, 2, 3]:
            vowel_count += 1
    if vowel_count >= 3:
        return False
    else:
        return True


def placeWord(word_to_play):
    new_word = checkIfWordinWord(word_to_play)

    if len(word_to_play) in [5]: # five letter word
        if ScrabbleBoard.pointValue(word_to_play[0]) >= ScrabbleBoard.pointValue(word_to_play[4]):
            ScrabbleBoard.points += ScrabbleBoard.pointValue(word_to_play[0])
            if containsMultipleVowels(word_to_play):
                align, move = ["L", len(word_to_play) - 1]
            else:
                align, move = ["T", len(word_to_play) - 1]
        else:
            ScrabbleBoard.points += ScrabbleBoard.pointValue(word_to_play[1])
            if containsMultipleVowels(word_to_play):
                align, move = ["R", 0]
            else:
                align, move = ["B", -1]


    elif len(word_to_play) in [6]: # six letter word
        index = 0
        for lett in range(len(word_to_play)):
            if ScrabbleBoard.pointValue(word_to_play[lett]) > index:
                index = lett
        ScrabbleBoard.points += ScrabbleBoard.pointValue(word_to_play[index])
        if index == 0:
            align, move = ["L", len(word_to_play) - 1]
        elif index == 1:
            align, move = ["T", len(word_to_play) - 1]
        elif index == 5:
            align, move = ["R", 0]
        else:
            align, move = ["B", -1]


    else: # get bonus points for using all letters!
        index = 0
        move = 0
        for lett in range(len(word_to_play)):
            if ScrabbleBoard.pointValue(word_to_play[lett]) > index:
                index = lett
        ScrabbleBoard.points += ScrabbleBoard.pointValue(word_to_play[index])
        if index == 0:
            align, move = ["L", len(word_to_play) - 1]
        elif index == 1:
            align, move = ["T", len(word_to_play) - 1]
        elif index == 2:
            align, move = ["L", len(word_to_play)-2]
        elif index == 4:
            align, move = ["R", 1]
        elif index == 5:
            align, move = ["R", 0]
        else:
            align, move = ["B", -1]

    placeLetters(word_to_play, align, move)