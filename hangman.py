import random 

def loadWords():
    with open("words.txt", "r") as notepad:
        wordlist = notepad.read().splitlines()
    return wordlist
    

def chooseWord(wordlist):
    secretWord=random.choice(wordlist).lower()
    return secretWord


def isWordGuessed(secretWord, lettersGuessed):
    counter=0
    for i in secretWord:
        if i in lettersGuessed:
            counter+=1
    if counter==len(secretWord):
        return True
    else:
        return False
        
    
def getGuessedWord(secretWord, lettersGuessed):
    str1=""
    for i in secretWord:
        if i in lettersGuessed:
            str1=str1+i+" "
        else:
            str1+="_ "
    return str1
                
            
def getAvailableLetters(lettersGuessed):
    AvailableLetters='abcdefghijklmnopqrstuvwxyz'
    for i in range (len(lettersGuessed)):
        AvailableLetters=AvailableLetters.replace(lettersGuessed[i],"")
    print(AvailableLetters)

def hangman(secretWord):
    no_of_gusses =7
    lettersGuessed=[]
    print("The word has",len(secretWord),"letters")
    while no_of_gusses>=0:
        if no_of_gusses==0:
            print("__________________________________")
            print("Sorry,Your guesses ran out .the word was",secretWord)
            break
        else:
            print("The available letters are:")
            getAvailableLetters(lettersGuessed)
            print("You have" ,no_of_gusses, "guesses")
            user_input=input("Guess a letter: ").lower()
            if user_input in lettersGuessed :
                print("__________________________________")
                print("You have already used that letter ")
                x=getGuessedWord(secretWord, lettersGuessed)
                print(x)
            elif user_input in secretWord:
                lettersGuessed.append(user_input)
                print("__________________________________")
                print("Good guess ")
                x=getGuessedWord(secretWord, lettersGuessed)
                print(x)
                if isWordGuessed(secretWord, lettersGuessed)==True:
                    print("Congratulations, you won!!!")
                    break
            else:
                print("__________________________________")
                print("Wrong guess ")
                x=getGuessedWord(secretWord, lettersGuessed)
                print(x)
                no_of_gusses-=1
                lettersGuessed.append(user_input)
                
                

wordlist = loadWords()
secretWord = chooseWord(wordlist).lower()
hangman(secretWord)





