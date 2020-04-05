import random
import string
word_list = ('python', 'java', 'kotlin', 'javascript')
rand_word = random.choice(word_list)
c = 0
input_letters = set()
word = '-'*len(rand_word)
word_list = list(word)


def play():
    print("H A N G M A N")
    global word_list, c
    count = 0
    while count < 8:
        print()
        print(''.join(word_list))
        letter = input('Input a letter: ')
        if letter in input_letters:
            print("You already typed this letter")
        else:
            for x in rand_word:
                if letter == x and letter != ' ':
                    word_list[c] = letter
                    input_letters.add(letter)
                else:
                    pass
                c += 1
        c = 0
        if len(letter) != 1:
            print('You should print a single letter')
        elif letter not in string.ascii_lowercase:
            print('It is not an ASCII lowercase letter')
        elif letter not in rand_word and letter not in input_letters:
            print('No such letter in the word')
            count += 1
            input_letters.add(letter)
        elif ''.join(word_list) == rand_word:
            print("""You guessed the word!
You survived!
""")
            break
        if count == 8:
            print('You are hanged!')


while True:
    state = input('Type "play" to play the game, "exit" to quit: ')
    if state == 'play':
        play()
    elif state == 'exit':
        break
