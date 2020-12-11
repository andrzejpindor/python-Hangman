import random


def print_word(word_array):
    print("".join(c[0] if c[1] is True else "-" for c in word_array))


def reveal_letter(word_array, letter):
    revealed = False
    no_improvements = False
    for item in word_array:
        if item[0] == letter:
            if item[1] is True:
                print("You've already guessed this letter")
                no_improvements = True
                break
            else:
                item[1] = True
                revealed = True
    if revealed is False and no_improvements is False:
        print("That letter doesn't appear in the word")

    return revealed


def all_revealed(word_array):
    return len([c for c in word_array if c[1]]) == len(word_array)


def is_valid_letter(letter):
    if len(letter) != 1:
        print('You should input a single letter')
        return False
    if letter not in 'abcdefghijklmnopqrstuwvxyz':
        print('Please enter a lowercase English letter')
        return False
    return True


print("H A N G M A N")

start = ''
while start != 'play':
    start = input('Type "play" to play the game, "exit" to quit: ')
    if start == 'exit':
        exit(0)

words = ["python", "java", "kotlin", "javascript"]
random_word = [[c, False] for c in list(random.choice(words))]
entered_letters = []
retries_left = 8
won = False
while retries_left > 0:
    print()
    print_word(random_word)
    if won:
        break
    input_letter = input("Input a letter: ")
    if is_valid_letter(input_letter) is False:
        continue
    if input_letter in entered_letters:
        print("You've already guessed this letter")
        continue
    entered_letters.append(input_letter)
    if reveal_letter(random_word, input_letter) is False:
        retries_left -= 1
    won = all_revealed(random_word)

if won:
    print("You guessed the word!")
    print("You survived!")
else:
    print("You lost!")