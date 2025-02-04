import random
word_list = ["aardvark", "baboon", "camel"]

def Gneranate_Random_Word():
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
    
    j = 0
    while j <= len(word):
        guess_letter = input("Enter a letter to guess the word: ")
        matched = False
        for i in range(len(word)):
            if guess_letter == word[i]:
                #print("matched" + guess_letter + " " + word[i])
                matched = True
                guess_word[i] = guess_letter
                
            else:
                #print("unmatched")
                continue
        # Join the word of list.
        final_word = ""
        print(final_word.join(guess_word))
        
        if matched:
            j += 1
        else:
            print("didn't match try again.")
    return 0

def main():
    Gneranate_Random_Word()
    return 0



if __name__ == "__main__":
    main()