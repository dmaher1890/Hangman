import random

#Welcome to the game
print ("Welcome to David's HangMan Game")

#Word Choosen 
words = ["hangman", "program", "python", "mountain", "family", "lighthouse", "recover", "news", "puzzle", "birthday"]
word = random.choice(words)
count = len(word)
print("The word has", count, "letters")

#split the word into letters
letters = list()
guessedlist = list()
for letter in word:
    letters.append(letter)

guessnumber = 6

# Is it a valid guess (is it a letter in the word)
while guessnumber > 0:
    left = list()
    guess = input ("What letter do you want to guess? ")
    for letter in letters:
        if guess == letter: 
            rightwrong = True
            break
        else:
            rightwrong = False
    if rightwrong == True:
        print("Yes that letter is in the word")
        letters.remove(guess)
        guessedlist.append(guess)
        if len(letters) == 0:
            print("You won")
            print(word)
            break
        print(guessedlist)
    else:
        print ("No that letter is not in the word")
        guessnumber = guessnumber - 1
        if guessnumber == 0:
            print("You lose because you are out of guesess")
            print("The word was", word)
        else:
            print ("You have",  guessnumber, "guesses left")
            print(guessedlist)



