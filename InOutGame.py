import os

def cls():

    os.system('cls' if os.name=='nt' else 'clear') 

cls()

print("$$$$$$$$$$$$$$$$$$$$$$$")
print("$                     $")
print("$   In and Out Game   $")
print("$                     $")
print("$$$$$$$$$$$$$$$$$$$$$$$")
print("\n")
players = []
p1 = input("Enter player 1's name: ")
p2 = input("Enter player 2's name: ")
players.append(p1)
players.append(p2)
players[0]
print("Host:")
word = input("Please enter a phrase: ").lower()
hiddenWord = ""
hiddenList = []
val = 0
word_= " "
oddNumCount = []
inWord = []
inOrOut = ["(that IS in the phrase): ", "(that IS NOT in the phrase): "]
alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
i = 0

def beginning():
    cls()

    global hiddenWord
    global hiddenList

    for x in word:
        if x == " ":
            hiddenWord += " ."
        else:
            hiddenWord += " _"
    
    print(hiddenWord)

    hiddenList = list(hiddenWord)


beginning()
print("\n")
print(alpha)
print("\n")

def playerchange():
    global i
   
    i = (i+1) % 2

def Guesses(mode):
    match = 0
    global oddNumCount
    global hiddenWord
    global hiddenList
    global inOrOut

    guess = input("Player enter a letter "+inOrOut[mode]).lower()
    for letter in word:
        if letter == guess:
            match = 1 

    if match == 1:

        if mode == 0:

            inWord.append(guess)
            alpha.remove(guess)
            cls()
            print("CORRECT! This", guess,"is in the phrase!\n")

            a = 0

            for x in word:
                oddNum()

                if x == guess:
                    hiddenList[oddNumCount[a]] = guess
                a = a + 1

            hiddenWord = "".join(hiddenList)

            print(hiddenWord)
            print("\n")
            print(alpha)
            print("\n")
            finalGuess()
            Guesses(1)

        elif mode == 1:

            inWord.append(guess)
            alpha.remove(guess)
            cls()
            print("INCORRECT! This", guess,"is in the phrase!\n")

            a = 0

            for x in word:
                oddNum()

                if x == guess:
                    hiddenList[oddNumCount[a]] = guess
                a = a + 1

            hiddenWord = "".join(hiddenList)

            print(hiddenWord)
            print("\n")
            print(alpha)
            print("\n")
            playerchange()
            finalGuess()
            Guesses(0)

    if match == 0:

        if mode == 0:

            inWord.append(guess)
            alpha.remove(guess)
            cls()
            print("INCORRECT! This", guess, "is not in the phrase!\n")
            print(hiddenWord, end=" ")
            print("\n")
            print(alpha)
            print("\n")
            playerchange()
            finalGuess()
            Guesses(0)

        elif mode == 1:

            inWord.append(guess)
            alpha.remove(guess)
            cls()
            print("CORRECT! This", guess, "is not in the phrase!\n")
            print(hiddenWord, end=" ")
            print("\n")
            print(alpha)
            print("\n")
            finalGuess()
            Guesses(0)
        


def finalGuess():
    print(players[i],"'s turn\n")
    if input("Do you want to guess the full phrase? ").lower() == "n":
        return False
    else:
        phrase = input("What is the full phrase? ")
        if phrase.lower() == word:
            print("Congrats that is the phrase!")
            return True
        else:
            print("That is not the phrase!")
            return False

def oddNum():

    global oddNumCount

    for x in range (200):
        if (x % 2 ==1):
            oddNumCount.append(x)


while finalGuess() == False:
     
        Guesses(0)
        
        

        



    

