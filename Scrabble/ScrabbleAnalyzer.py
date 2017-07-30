import BoardPlayer
import ScrabbleBoard
import time

start_time = time.time()


def getNextword(): # N
    return f.readline()


def getWordValue(word):
    points = 0
    if len(word) == 7:
        points += 50
    for letter in word:
        points += ScrabbleBoard.pointValue(letter)
    return points + ScrabbleBoard.doubleWordBonus(word)

def ifPossibleIsValid(possibleLetters, wordToCheck):
    isValid = True
    for letter in wordToCheck:
        if letter in possibleLetters:
            possibleLetters = possibleLetters.replace(letter, "")
        elif "!" in possibleLetters:
            possibleLetters = possibleLetters.replace("_", "")
        else:
            isValid = False
    return isValid

def checkForValueableLettersOrToss(word):
    toss_letters = ""
    keep_letters = ""
    for letter in word: # first check for valuable letters
        if ScrabbleBoard.pointValue(letter) < 5:
            toss_letters += letter
        else:
            keep_letters += letter
    if len(keep_letters) > 2:
        return "EXCHANGE: " + toss_letters
    temp_toss = toss_letters

    for letter in temp_toss: # second check for semi-valuable letters
        if ScrabbleBoard.pointValue(letter) == 1:
            keep_letters += letter
            toss_letters = toss_letters.replace(letter, "", 1)
    keep_letter_sum = 0
    for letter in keep_letters:
        keep_letter_sum += ScrabbleBoard.pointValue(letter)
        if keep_letter_sum >= 5:
            return "EXCHANGE: " + toss_letters
    return "PASS"



def checkIfPossibleWord(possibleLetters):
    newWord = getNextword().strip()
    word = " "
    wordScore = 0
    isValid = True

    while newWord != "":
        if len(newWord) < 8:
            for letter in newWord:
                if letter not in possibleLetters:
                    isValid = False
                    break
            isValid = ifPossibleIsValid(possibleLetters, newWord)
            if isValid:
                if getWordValue(word) < getWordValue(newWord):
                    word = newWord
                    wordScore = getWordValue(word)
        newWord = getNextword().strip()
        isValid = True
    if wordScore < 20:
        return checkForValueableLettersOrToss(word)
    ScrabbleBoard.points = wordScore
    print("PLACE WORD: ", word)
    BoardPlayer.placeWord(word)

def generateNewTestFile():
    with open('test_rack_file.txt', 'w') as file:
        for number in range(10):
            file.write(ScrabbleBoard.getPieces() + "\n")

if __name__ == '__main__':

    generateNewTestFile()
    with open('scrabble_test_rack.txt', 'r') as read:
        gamePlay = read.readline().strip()

        while gamePlay != "":
            start_time = time.time()
            f = open('SOWPODS_complete.txt', 'r')
            print("RACK: " + gamePlay)
            check = checkIfPossibleWord(gamePlay)
            if check != "":
                print(check)


            print("Elapsed time: %s seconds" % (time.time() - start_time), "\n")

            gamePlay = read.readline().strip()

            f.close()
    input("Press any key to continue.")