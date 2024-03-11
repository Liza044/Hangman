# Hangman game
# I added color to part of the text


# print the start of the game
def start():
    max_tries = 6
    hangman_art = """            Welcome to the game Hangman\n
              _    _
             | |  | |                                        
             | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
             |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
             | |  | | (_| | | | | (_| | | | | | | (_| | | | |
             |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                                 __/ |                      
                                |___/  \n"""
    arrow = r"""                        | |
                        _| |_
                        \   /
                         \ /
                   """
    print("\n\033[1;32;40m", hangman_art, "\n             Number of tries:", max_tries, "\n\n", arrow, "\n\033[0m")


# check the index in txt file
def check_txt_index(index):
    if index <= 0:
        return False
    return True


# choose the word in txt file by index
def choose_word(file_path, index):
    with open(file_path) as words_l:
        sentence = words_l.read()
        all_words = sentence.split()
        words_list = []
        for i in range(len(all_words)):
            if words_list.count(all_words[i]) == 0:
                words_list.append(all_words[i])
        the_word = words_list[index % (len(words_list)) - 1]
        new_word = ''
        for letter in the_word:
            new_word += letter.lower()
        return new_word


# check if the player wins
def check_win(secret_word, old_letters_guessed):
    for letter in secret_word:
        if letter not in old_letters_guessed:
            return False
    return True


# print a word ( _ or letter)
def show_hidden_word(secret_word, old_letters_guessed):
    print("\nThe word: ")
    for letter in secret_word:
        if letter in old_letters_guessed:
            print(letter, "", end='')
        else:
            print("_ ", end='')
    print("\n")


# check if the letter is matched
def check_valid_input(letter_guessed, old_letters_guessed):
    if (letter_guessed < 'a' or letter_guessed > 'z') or \
            (len(letter_guessed) != 1) or (letter_guessed in old_letters_guessed):
        return False
    return True


# if the letter does not match, the function print a message
def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    if not check_valid_input(letter_guessed, old_letters_guessed):
        print('X')
        print("\nYou try before this letters: ")
        for i in range(len(old_letters_guessed) - 1):
            print(old_letters_guessed[i], " -> ", end='')
        if len(old_letters_guessed) != 0:
            print(old_letters_guessed[-1], "\n")
        return False

    else:
        old_letters_guessed.append(letter_guessed)
        return True


# check if the letter is in a secret word
def check_letter(letter, secret_word):
    if letter in secret_word:
        return True
    return False


# print a photo of a hangman
def print_hangman(num_of_tries):
    hangman_art = {1: "     x-------x",
                      2: """       x-------x
        |
        |
        |
        |
        |""",
                      3: """       x-------x
        |       |
        |       0
        |
        |
        |""",
                      4: """       x-------x
        |       |
        |       0
        |       |
        |
        |""",
                      5: """       x-------x
        |       |
        |       0
        |      /|\ 
        |
        |""",
                      6: """       x-------x
        |       |
        |       0
        |      /|\ 
        |      /
        |""",
                      7: """       x-------x
        |       |
        |       0
        |      /|\ 
        |      / \ 
        |"""}

    print("\n\033[1;32;40m", hangman_art[num_of_tries], "\n\033[0m")


def main():
    start()
    letters_guessed = []
    number_of_tries = 1

    try:
        txt_file = input("Enter a text file, the file must contain words separated by spaces: \n")
        index_word = int(input("Enter a place of the word in the file: "))
        check_index = check_txt_index(index_word)

        while not check_index:
            print("The index must be greater then 1")
            index_word = int(input("Enter an index of the word in the file: "))
            check_index = check_txt_index(index_word)

        the_word = choose_word(txt_file, index_word)
        print_hangman(number_of_tries)
        show_hidden_word(the_word, letters_guessed)
        your_letter = input("Enter a letter: ")
        the_letter = your_letter.lower()
        check = try_update_letter_guessed(the_letter, letters_guessed)

        while not check:
            print("The letter not match, or you wrote this letter before, try again, its must be one letter")
            your_letter = input("Enter a letter: ")
            the_letter = your_letter.lower()
            check = try_update_letter_guessed(the_letter, letters_guessed)

        if the_letter not in letters_guessed:
            letters_guessed.append(the_letter)
        if not check_letter(the_letter, the_word):
            print(" \n:(\n ")
            number_of_tries += 1
            print_hangman(number_of_tries)
        check_w = check_win(the_word, letters_guessed)

        while not check_w:
            show_hidden_word(the_word, letters_guessed)
            your_letter = input("Enter a letter: ")
            the_letter = your_letter.lower()
            check = try_update_letter_guessed(the_letter, letters_guessed)
            while not check:
                print("The letter not match, or you wrote this letter before, try again, its must be one letter")
                your_letter = input("Enter a letter: ")
                the_letter = your_letter.lower()
                check = try_update_letter_guessed(the_letter, letters_guessed)

            if the_letter not in letters_guessed:
                letters_guessed.append(the_letter)
            if not check_letter(the_letter, the_word):
                number_of_tries += 1
                print(" \n:(\n ")
                print_hangman(number_of_tries)
            check_w = check_win(the_word, letters_guessed)
            if number_of_tries == 7:
                print("\nLOSE\n")
                break

        if check_w:
            show_hidden_word(the_word, letters_guessed)
            print("\nWIN ☻\n")

    except:
        print('Something else went wrong')



if __name__ == '__main__':
    main()
