from collections import Counter
from functools import reduce
import random

#This function reads the file
def get_words():
    fn = './words.txt'
    book = open(fn)
    words = [(line.strip().lower()) for line in book.readlines()]
    book.close()
    return words
    
#This function selects random word from file
def select_word(words):
    word = random.choice(words)
    return [word, len(word)]

#This function counts full amount letters in word of equal length for stats
def get_full_length(words, guess_len):
    content = list(filter(lambda word: len(word) == guess_len, words))
    return len(content)*guess_len

#This function offers letter to be played
def top_letters(words, guess_word):
   
    content = list(filter(lambda word: len(word) == guess_word[1], words))
    letters = reduce(lambda init, word: init + Counter(word), content, Counter())
    for letter, count in sorted(letters.items(), key = lambda t: -t[1]):
        yield letter, count
    
#This function prints the word during every iteration
def print_word(guess_word, confirmed_letters, counter):
        word_in_progress = []
        result = ''
        for el in guess_word:
            if el in confirmed_letters:
                 word_in_progress.extend(el+' ')  
            else:
                word_in_progress.extend('_ ')    
        print(result.join(word_in_progress))
        
        if "_" not in  word_in_progress:
            print('\nThe word is ready!!!!!!!!!!')
            print(f'you played {counter+1} times')
            return True

#This is the main function
def play_the_game():
    words = get_words()
    guess_word = select_word(words)
    value = get_full_length(words, guess_word[1])
    confirmed_letters = []
    rejected_letters = []
    counter = 0
    
    print(f'your word consist of {guess_word[1]} letters')
    print("\n To quit the game please enter 'w'...")
    
    for letter, count in top_letters(words, guess_word):
        percentage = round((count/value)*100, 2)
        player_choice = input(f"Would you like to take letter '{letter}', which is in {percentage}% times?\ny/n: ")
        
        if player_choice == 'y':
           confirmed_letters.extend(letter)
           res = print_word(guess_word[0], confirmed_letters, counter)
           counter += 1
           if res:
               break
        elif player_choice == 'n':
            rejected_letters.extend(letter)
            print_word(guess_word[0], confirmed_letters, counter)
            counter += 1
        elif player_choice not in ('ynw'):
            print("\nYou entered wrong input...\nPlease enter 'y' or 'n'...")
        elif player_choice == 'w':
            print(f'you played {counter} times')
            break
     
play_the_game()
    


