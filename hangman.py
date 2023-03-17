from random import randint  # Do not delete this line


def displayIntro():
    intro = open('intro', 'r')
    print(intro.read())
    intro.close()


def displayEnd(result):
    if result == True:
        _won = open('won', 'r')
        print(_won.read())
        _won.close()
    if result == False:
        _lost = open('lost', 'r')
        print(_lost.read())
        _lost.close()


def displayHangman(state):
    live = state
    if live == 5:
        live5 = open('live=5', 'r')
        print(live5.read())
        live5.close()
    if live == 4:
        live4 = open('live=4', 'r')
        print(live4.read())
        live4.close()
    if live == 3:
        live3 = open('live=3', 'r')
        print(live3.read())
        live3.close()
    if live == 2:
        live2 = open('live=2', 'r')
        print(live2.read())
        live2.close()
    if live == 1:
        live1 = open('live=1', 'r')
        print(live1.read())
        live1.close()
    if live == 0:
        live0 = open('live=0', 'r')
        print(live0.read())
        live0.close()


def getWord():
    words = open('hangman-words.txt', 'r')
    words_list = []
    pre_list = words.readlines()
    for line in pre_list:
        words_list.append(line.rstrip('\n'))
    choose = randint(0, len(words_list))
    words.close()
    return words_list[choose]



def valid(c):
    abc = 'abcdefghijklmnopqrstuvwxyz'
    if len(c) == 1 and c in abc and c:
        return True
    else:
        return False

save = ''


def play():
    _live = 5
    word = getWord()
    _var = len(word) * '_'
    guess_word = list(_var)
    while True:
        displayHangman(_live)
        char = input(f'''Guess the word: {''.join(guess_word)}
    Enter the letter:''')
        if valid(char) == False:
            print(f'{char} is invalid character!')
            displayHangman(_live)
            char = input(f'''Guess the word: {''.join(guess_word)}
Enter the letter:''')
        if valid(char) == True:
            if char not in word:
                _live -= 1
            else:
                for i in range(len(guess_word)):
                    if char == word[i]:
                        guess_word[i] = word[i]
        if _live == 0:
            displayHangman(_live)
            return False, word
        if guess_word == list(word):
            return True, word


def hangman():
    while True:
        displayIntro()
        result = play()
        print(f'Hidden word was: {result[1]}')
        displayEnd(result[0])
        y_n = input('Do you want to play again? (yes/no)')
        if y_n == 'no':
            break


if __name__ == "__main__":
    hangman()

