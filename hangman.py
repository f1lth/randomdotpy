import random
from os import system

def extractVocab():
    file = open("nounlist.txt", "r")
    words = file.read().strip()
    wordArray = words.split("\n")

    return wordArray

def pickWord():
    wordList = extractVocab()

    randomNum = random.randint(1,5000)
    selectedWord = wordList[randomNum]

    return selectedWord

def userGuess():
    guess = input("Enter your guess: ")

    if guess == "quit":
        exit()
    return guess

def displayWord(word):
    cachedWord = ''

    for i in range(len(word)):
        cachedWord += "*"
        
    return cachedWord

def rungame():
    
    print("--- Type 'quit' at any time to close the program ---")
    winGame = False

    guessedList = []
    getWord = pickWord()
    

    cachedWord = displayWord(getWord)
    cachedList = list(cachedWord)
    print("Your word is: ",cachedWord)

    while winGame == False:
        
        newGuess  = userGuess()

        if newGuess not in guessedList:
            guessedList += newGuess

        for chars in range(len(getWord)):
            if getWord[chars] == newGuess:
                cachedList[chars] = newGuess
        
        if "*" not in cachedList:
            return getWord

        system('cls')
        print(''.join(cachedList))
        print("Guessed Letters: " + ','.join(guessedList))

        if len(guessedList) == 9 and winGame == False:
            print("You have one guess left!")

        if len(guessedList) == 10 and winGame == False and newGuess not in getWord:
            print("You have died, the word was:", getWord)
            exit() 

def main():
    system('color D')
    getWord = rungame()
    if len(getWord) != 0:
        print(getWord)
        print("Congrats, you guessed the word!")

main()
