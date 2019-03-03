import string
from words import choose_word
from images import IMAGES
# End of helper code
# -----------------------------------

def ifValid(user_input):
    if len(user_input) != 1:
        return False

    if not user_input.isalpha():
        return False

    # True humne tab hi return kiya hai jab
    # user_input ki length 1 hai aur woh character hai
    return True
def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: ek string word jo ki user ko guess karna hai
    letters_guessed: ek list hai, jisme wo letters hai jo ki user nai abhi tak guess kare hai
    returns: return True kare agar saare letters jo ki user ne guess kiye hai wo secret_word mai hai, warna no
      False otherwise
    '''
    # if secret_word==letters_guessed:
    #     return True
    for i in secret_word:
        if i not in letters_guessed:
            return False
                    
    else:
        return True

# Iss function ko test karne ke liye aap get_guessed_word("kindness", [k, n, d]) call kar sakte hai
def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: ek string word jo ki user ko guess kar raha hai
    letters_guessed: ek list hai, jisme wo letters hai jo ki user nai abhi tak guess kare hai
    returns: ek string return karni hai jisme wo letters ho jo sahi guess huye ho and baki jagah underscore ho.
    eg agar secret_word = "kindness", letters_guessed = [k,n, s]
    to hum return karenge "k_n_n_ss"
    '''

    index = 0
    guessed_word = ""
    while (index < len(secret_word)):
        if secret_word[index] in letters_guessed:
            guessed_word += secret_word[index]
        else:
            guessed_word += "_"
        index += 1
    
    return guessed_word
def get_available_letters(letters_guessed):
    available=""
    '''
    letters_guessed: ek list hai, jisme wo letters hai jo ki user nai abhi tak guess kare hai
    returns: string, hame ye return karna hai ki kaun kaun se letters aapne nahi guess kare abhi tak
    eg agar letters_guessed = ['e', 'a'] hai to humme baki charecters return karne hai
    jo ki `bcdfghijklmnopqrstuvwxyz' ye hoga
    '''
    import string
    letters_left = string.ascii_lowercase
    for i in letters_left:
        if i not in letters_guessed:
            available+=i
    return available

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Hangman game yeh start karta hai:

    * Game ki shuruaat mei hi, user ko bata dete hai ki
      secret_word mei kitne letters hai

    * Har round mei user se ek letter guess karne ko bolte hai

    * Har guess ke baad user ko feedback do ki woh guess uss
      word mei hai ya nahi

    * Har round ke baar, user ko uska guess kiya hua partial word
      display karo, aur underscore use kar kar woh letters bhi dikhao
      jo user ne abhi tak guess nahi kiye hai

    '''
    print "Welcome to the game, Hangman!"
    print "I am thinking of a word that is " + str(len(secret_word)) + " letters long."
    print ""

    letters_guessed = []
    lives=8
    list_of_images=[0,1,2,3,4,5,6,7]
    level=raw_input("Enter your level esay, medium,hard ")
    if level=="easy":
        lives=8
        list_of_images=[0,1,2,3,4,5,6,7]
    if level=="medium":
        lives=6
        list_of_images=[0, 2, 3, 5, 6, 7]
    if level=="hard":
        lives=4
        list_of_images=[1, 3, 5, 7]

    while lives>0:
        available_letters = get_available_letters(letters_guessed)
        print "Available letters: " + available_letters
        guess = raw_input("Please guess a letter: ")
        letter = guess.lower()
        if letter=="hint":
            for i in secret_word:
                if i in available_letters:
                    letter=i
        if (not ifValid(letter)):
            print "Invalid Input "
            continue

        if letter in secret_word:
            letters_guessed.append(letter)
            print "Good guess: " + get_guessed_word(secret_word, letters_guessed)
            print ""

            if is_word_guessed(secret_word, letters_guessed) == True:
                print " * * Congratulations, you won! * * "
                print ""
                break
        else:
            print "Oops! That letter is not in my word: " + get_guessed_word(secret_word, letters_guessed)
            letters_guessed.append(letter)
            print ""
            
            print IMAGES[8-lives]
            lives-=1
    print "sorry you have lost your lives ."
            
        
# Load the list of words into the variable wordlist
# So that it can be accessed from anywhere in the program
secret_word = choose_word()
# print secret_word
hangman(secret_word)
