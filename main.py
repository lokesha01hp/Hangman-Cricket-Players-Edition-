import random,string
from words import players        

def get_valid_word(players): #This function is optional if all the words are in correct format
    word =  random.choice(players)
    while ' ' not in word:
        word = random.choice(players)
    return word.upper()

def hangman():
    word = get_valid_word(players)
    print("To help you \'",random.choice(word),"\'is present somewhere in the word")
    word_letters = set(word) - {" "} #removes empty spaces and get unique letters in word
    alphabet = set(string.ascii_uppercase)
    used_letters=set()
    
    lives = 5
    
    while len(word_letters) >0 and lives > 0:
        print("\nLives you have",lives,"And you have used this letters :",''.join(used_letters))
        
        word_list=[]
        for letter in word:
            if letter in used_letters or letter == " ":
                word_list.append(letter)
            else:
                word_list.append("-")
        print("Current words",''.join(word_list))

        user_letter=input("Type your letter :").upper()
        if user_letter in alphabet - used_letters :
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives -1
                print('\nYour letter,', user_letter, 'is not in the word.')
        elif user_letter in used_letters:
            print("You already tried this letter, try another one!")

        else:
            print("Invalid letter. Please try again.")

    if lives == 0:
        print("You died, Try again,The word was",word)
    else:
        print("You guessed the word",word)


if __name__ == '__main__':
    hangman()

