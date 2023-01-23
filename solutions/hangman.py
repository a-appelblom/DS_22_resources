# Antingen har vi en lista med ord vi väljer från
# Eller så skriver 1 person ett ord i början (Börjar här)

# Kolla om bosktaven finns.
# Öka scoren när det är fel

# skriv ut alla förekomster av bokstaven, på rätt plats

# A != a

def main():
    score = 0
    game_list = []
    guessed_letters = []
    goal_string = input("What is the word: ")
    goal_string = goal_string.upper().strip()
    goal_string.capitalize()
    goal = list(goal_string)

    for _ in range(len(goal_string)):
        game_list.append("_")

    while "_" in game_list and score < 8:
        print(game_list)
        guess = input("Input a letter: ")
        guess = guess.strip()

        if len(guess) > 1:
            print("Only one letter att the time")
            continue

        guess = guess.upper()
        if guess in guessed_letters:
            print("Already guessed")
            continue
        guessed_letters.append(guess)

        if guess not in goal:
            score += 1
            continue

        for i, char in enumerate(goal):
            if char == guess:
                print("in if", i, guess)
                game_list[i] = guess
                print(game_list)


if __name__ == '__main__':
    main()
