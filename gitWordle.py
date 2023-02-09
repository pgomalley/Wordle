"""Author Patrick OMalley,
Version 2
Finished on Oct 10th, 2022
WORDLE"""

from random import choice
from string import printable

# Function for opening words.dat, a file containing 5757 lines with one word
# per line.  These are the words used in the game management system.  We're 
# going to be appending these words into a list for later use with the
# random module and choice.


def readWords(filename='words.dat'):
    handle = open('words.dat' , 'r')
    wlist = []
    for line in handle:
        wlist.append(line.lower().strip())
    return(wlist)

# Function evalGuess is used later in the script to provide feedback to
# the user about how close their guess is to the target. If the guess
# contains a letter in the correct location, the letter will be capital.
# If the guess contains a letter in the target word, but in the wrong spot,
# the letter will be lower case.  If the letter doesn't reside in the target
# word at all, the spot it would've occupied will be a ".".


# Example:
#   >>> evalGuess('soapy', 'shoot')
#   'So...'

def evalGuess(guess, target):
    L = []
    for i, y in zip(guess, target):
        if i ==y:
            L.append(i.upper())
        elif i  in target and i != y:
            L.append(i.lower())
        elif i != target:
            L.append(' . '.lower())
    return ''.join(L)

# The consistent function returns True if the feedback is consistent with
# word guessed by the player. Consistent means the guess word has to have
# all of the upper case letters in feedback, once these are checked it must
# also have all of the lower case letters in feedback, only after the
# letters uppercase in feedback letters are excluded.

def consistent(feedback, word):
    list = [True,True,True,True,True]
    for i in feedback:
        if i.islower() and i not in word:
            list[0] = (False)
    if feedback[0].isupper() and feedback[0].lower() != word[0]:
            list[0] = (False)
            pass
    if feedback[1].isupper() and feedback[1].lower() != word[1]:
            list[1] = (False)
            pass
    if feedback[2].isupper() and feedback[2].lower() != word[2]:
            list[2] = (False)
            pass
    if feedback[3].isupper() and feedback[3].lower() != word[3]:
            list[3] = (False)
            pass
    if feedback[4].isupper() and feedback[4].lower() != word[4]:
            list[4] = (False)
            pass
    return (all(list))
      


# The calcSize function displays the number of words in S that are
# consistent with the feedback provided.  Calsize will display this as a
# % value, followed by an integer of remaining words.

def calcSize(S, feedback):
    numberOfWords = 0
    for word in S:
        if (consistent(feedback,word)):
            numberOfWords+=1
    return numberOfWords


from random import choice

# The wordle() game management function takes a list of words, S, andrandomly
# selects a target word for this round from S. It then manages game
# play, and returns True (meaning the user would like to play another
# round) or False (meaning that the user does not wish to play another
# round).  There are various methods for obtaining either a True or false
# statement.  This function also makes use of the other functions in the
# file, so know tampering with one may disrupt the whole system.

# To a further extent, game management means (1) printing a suitable prompt,
#(2) taking the players input, (3) rejecting the input if it is not "legal,"
# (4) responding to a special command (here, '.', '+', or '?'), or
# (5) evaluating the input against the target word (see previous
# function). The process repeats until the user guesses the target
# word, has six guesses without guessing the target word, or the user
# chooses to abruptly end the game via a special command ('.').

def wordle(S):
    target=choice(S)			# Random target word
    osize = len(S)			# Initial size of dictionary
    feedback = '.'*5			# Initial feedback is empty
    avail = list(printable[10:36])	# List of available letters
    history = ""			# String history of word + feedback
    n = 6				# Remaining guesses

    # Print opening banner
    print('Welcome to Wordle!')
    print('Enter your guess, or ? for history; + for new game; or . to exit')

    # Repeat while guesses remain (or user quits with '+' or '.'
    # input).
    while n > 0: 
        # Uncomment the following line to enable "cheat mode." Cheat
        # mode reveals the usually hidden target word. 
        # print("Cheat: {}".format(target))  # Cheat mode!

        print(('Status: ' + ''.join(avail)))
        pass

        # Prompt the user for a guess. 
        guess = input("\nWordle[{}]: '{}' >  ".format(7-n, feedback))

        # The next conditional statement breaks down game management
        # into an appropriately ordered series of outcomes.
        if guess in '.+':           # Abort game
            print("Abort game.\n{}The target word was {}\n".format(history, target))
            return(guess=='+')
        elif guess=='?':	    # Show guess history
            print("History:\n{}".format(history))
            continue
        elif guess in history:		    # You've already guessed that!
            print('Youve already guessed that!')
            continue
        elif guess not in S:        # Illegal guess
            print("Unrecognized word: '{}'".format(guess))
            continue
        elif not consistent(feedback, guess):
            print("Successive guesses must use all {} known hints.".format(5-feedback.count('.')))
            continue
        feedback = evalGuess(guess, target)
        # Guess is legal and fits known feedback; accept the guess and
        # check it for the win.
        history = history + " {}: {} => {}\n".format(7-n, guess, feedback)
        if feedback.lower() == target: # You win!
            print("Good job!\n{}The target word was {}\n".format(history, target))
            return(True)

        # Not a winner (yet): update status and try again. 
        nsize = calcSize(S, feedback)	# new size
        print("Quality: {:.2%} [{} words remain]".format((osize - nsize + 1)/osize, nsize))
        osize = nsize

        # Here we are updating list of available letters. Because this
        # takes place in an idle enivorment we can't shade letters, so the
        # semantics here will be a bit different: an upper case letter is
        # in the word in the correct spot , while lower case are in the word
        # but an undetermined location.

        lettersIn = []
        lettersNot = []
        for i in guess:
            if i in list(target):
                lettersIn.append(i)
            if i not in list(target):
                lettersNot.append(i)

        for letter in range(0, len(avail)):
            if avail[letter] in lettersIn:
                avail[letter] = avail[letter].upper()
            if avail[letter] in lettersNot:
                avail[letter] = '.'        

        # Go on to next guess
        n = n-1

    # If you get to this point, the player has run out of
    # guesses.
    print("Sorry, no dice...\n{}The target word was {}\n".format(target, history))
    # Assume they want to play another game.
    return(True)

######################################################################
# This code is executed automatically when you feed this file to a
# fresh invocation of Python. So, for example, from the Linux prompt:
#    > python wordle.py
# will start the game for interactive use right at the shell.
#
if __name__ == '__main__':
    # Read in the list of legal 5-letter words and then continue
    # playing the game until wordle() returns False.
    while wordle(S=readWords('words.dat')):
        print("Let's play again!\n")
        
            
