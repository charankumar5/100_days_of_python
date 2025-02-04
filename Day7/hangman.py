
import random

def Gneranate_Random_Word():
    word_list = ["aardvark", "baboon", "camel"]
    lives = 6
    stages = ['''
    +---+
    |   |
    O   |
    /|\  |
    / \  |
        |
    =========
    ''', '''
    +---+
    |   |
    O   |
    /|\  |
    /    |
        |
    =========
    ''', '''
    +---+
    |   |
    O   |
    /|\  |
        |
        |
    =========
    ''', '''
    +---+
    |   |
    O   |
    /|   |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
    |   |
        |
        |
    =========
    ''', '''
    +---+
    |   |
    O   |
        |
        |
        |
    =========
    ''', '''
    +---+
    |   |
        |
        |
        |
        |
    =========
    ''']
    word = random.choice(word_list)
    print(word)
    # store the word in list
    word = list(word)
    #aprint(word)
    
    guess_word = []
    # print spaces of the word for number of guesses.
    for i in range(len(word)):
        print("_", end="")
        guess_word.append("_")
    # print(guess_word)
    print("\n")
    
    correct_letters = []
    game_over = False
    while not game_over:
        guess_letter = input("Enter a letter to guess the word: ").lower()
        display = ""
        for letter in word:
            if guess_letter == letter:
                display += letter
                correct_letters.append(letter)
            elif letter in correct_letters:
                display += letter
            else:
                 display +="_"
        print(display)
        
        if guess_letter not in word:
            lives -= 1
            if lives == 0:
                game_over = True
                print("Game over.")      
        if "_" not in display:
            game_over = True
            print("You win!")
        
        print(stages[lives])
    return 0

def main():
    Gneranate_Random_Word()
    return 0



if __name__ == "__main__":
    main()