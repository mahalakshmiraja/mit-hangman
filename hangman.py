# Hangman Game
# -----------------------------------
import random
import string



WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    #print (wordlist)
    print("  ", len(wordlist), "words loaded.")

    return wordlist


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)



# -----------------------------------


# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, my_word):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    my_word: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    word_guessed = ''.join(map(str,my_word))
    if secret_word == word_guessed:
      return True
    else:
      return False


def get_guessed_word(secret_word,letters_guessed, letters_guessed_list):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed_list: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    user_guess = []
    for i in range(len(secret_word)):
      user_guess.append('_ ')
    
    if letters_guessed in secret_word:
      for i in range(len(letters_guessed_list)):
        for j in range(len(secret_word)):
          if letters_guessed_list[i] == secret_word[j]:
            user_guess[j]=letters_guessed_list[i]
      print (''.join(map(str,user_guess)))
    else:
      print ("Oops ! That's not in my word")
    return user_guess

  


def get_available_letters(letters_guessed,all_letters):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    i=0
    while i < len(all_letters):
      if all_letters[i] == letters_guessed:
        del(all_letters[i])
      i+=1  
    print ("Remaining Available Letters:")    
    print (''.join(map(str,all_letters)))
    return all_letters
    
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    print ('Welcome to the game Hangman!')
    print ('I am thinking of a word that is %d letters long.' %(len(secret_word)))
    print ("----------------")
    print ("You have 6 guesses left.")
    print ("Available letters: abcdefghijklmnopqrstuvwxyz")
    letters_guessed_list = []
    all_letters= ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    count = 1
    guess = 3
    warnings = 3
    while count<=guess:
      letters_guessed = str.lower(input("Please guess a letter: "))
      if letters_guessed not in letters_guessed_list:
        if letters_guessed.isalpha()==True:
          letters_guessed_list.append(letters_guessed)
          word_guessed = get_guessed_word(secret_word, letters_guessed, letters_guessed_list)
          get_available_letters(letters_guessed,all_letters)
          if count!=guess:
            print ("Remaining Number of Guesses: %d" %(guess-count))
            count +=1
          else:
            print (" Sorry !! You ran out of guesses. The word was %s" %(secret_word))
        elif letters_guessed == '*':
          print ("Possible word matches are:")

        else:
          print ("Oops ! This is not a valid letter")
          warnings -=1
          print ("You have %d warnings left" %(warnings))
      else:
        print("You have already guessed that word ")
  
    




# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, secret_word, wordlist):
    '''
    my_word: string with _ characters, current guess of secret word
    wordlist: list of string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of wordlist, or the letter is the special symbol
        _ , and my_word and wordlist are of the same length;
        False otherwise: 
    '''
       
    for i in range(len(wordlist)):
      if len(secret_word) == len(wordlist[i]):
        return True
      else:
        return False
      



def show_possible_matches(my_word,secret_word,wordlist):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    for i in range(len(wordlist)):
      match = True
      if len(secret_word) == len(wordlist[i]):
        for j in range(len(secret_word)):
          if my_word[j] == '_ ':
            match = match and True
          elif my_word[j] == wordlist[i][j]:
            match = match and True
          else:
            match = match and False
        match_result = match
        if match_result == True:
          print (wordlist[i])
          
        
            
    



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    print ('Welcome to the game Hangman!')
    print ('I am thinking of a word that is %d letters long.' %(len(secret_word)))
    print ("----------------")
    print ("You have 6 guesses left.")
    print ("Available letters: abcdefghijklmnopqrstuvwxyz")
    letters_guessed_list = []
    all_letters= ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    count = 1
    guess = 5
    warnings = 3
    
    while count<=guess:
      letters_guessed = str.lower(input("Please guess a letter: "))
      if letters_guessed not in letters_guessed_list:
        if letters_guessed.isalpha()==True:
          if letters_guessed in secret_word:
            letters_guessed_list.append(letters_guessed)
            my_word = get_guessed_word(secret_word, letters_guessed, letters_guessed_list)
            get_available_letters(letters_guessed,all_letters)
            completed = is_word_guessed(secret_word, my_word)
            if completed == True:
              print ("Congratulations !!  You Won")
              break
                       
          else:
            print ("Oops ! That's not in my word")
            get_available_letters(letters_guessed,all_letters)
            if count!=guess:
              print ("Remaining Number of Guesses: %d" %(guess-count))
              count +=1
            else:
              print (" Sorry !! You ran out of guesses. The word was %s" %(secret_word))
              break
            
        elif letters_guessed == '*':
            if guess==5:
              print ("Sorry ! Guess a letter")
            else:
              print ("Possible word matches are:")
              inFile = open(WORDLIST_FILENAME, 'r')
              line = inFile.readline()
              wordlist = line.split()
              show_possible_matches(my_word,secret_word,wordlist)

        else:
            print ("Oops ! This is not a valid letter")
            warnings -=1
            print ("You have %d warnings left" %(warnings))
      else:
          print("You have already guessed that word ")
      

    

if __name__ == "__main__":
    #secret_word = "hike"
    #hangman_with_hints(secret_word)
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
