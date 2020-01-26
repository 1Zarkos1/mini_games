import random
import string

#gets 20000 words from file and stores it in list
def get_words():
    with open('words.txt') as file:
        words = [word.strip() for word in file.readlines()]
    return words

#finds position of chosen letter in game word and place it in player word
def mess_words(player_word, word, letter):
    for i, let in enumerate(word):
        if let == letter:
            player_word[i] = letter
    return player_word

while True:
    #ask if a user wants to play
    chose = input('Do you want to play? (y/n)')
    if chose == 'y':
        solved = False
        attempts = 3
        letters = list(string.ascii_lowercase)
        word = random.choice(get_words())
        player_word = ['_'] * len(word)
        while attempts > 0:
            #let the user choose a word
            letter = input((f'Word:{" ".join(player_word)}. \n' \
                f'You have {attempts} attempts left. ' \
                f'Choose your letter: {"".join(letters)}?'))
            
            #check if letter has already been chosen before
            if letter not in letters:
                print("There is no such letter in list!")
                continue
            
            #check if chosen letter is in word 
            if letter not in word:
                print('Wrong letter!')
                attempts -= 1
                letters.remove(letter)
                continue
            else:
                letters.remove(letter)
                player_word = mess_words(player_word, word, letter)
                if player_word == word:
                    solved = True
                    break
        #print result
        if solved:
            print('Congratulation! You won!')
        else:
            print('Sorry. You lost!')
        print(f'The right word is {word}')
    elif chose == 'n':
        break
    else:
        print('Uncorrect input!')
