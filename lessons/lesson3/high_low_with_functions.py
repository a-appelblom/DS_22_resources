import random


def main():
    max = 10
    min = 1
    score = 0

    random_num = random.randint(min, max)

    while True:
        print("Ditt nummer är: ", random_num)

        guess = get_input()
        new_num = random.randint(min, max)
        score = check_result(new_num, random_num, guess, score)
        random_num = new_num


def get_input() -> str:
    invalid = True

    while invalid:
        # Returnerar en string
        guess = input("Vad är din gissning högre eller lägre? (h/l) (exit): ")

        if guess != "h" and guess != "l" and guess != "exit":
            continue

        if guess == "exit":
            print("Tack för att du spelade")
            exit()

        invalid = False
    return guess


def check_result(new_num, random_num, guess, score) -> int:
    if new_num >= random_num and guess == "h":
        score += 1
        print("Rätt, din score är: ", score)
    elif new_num <= random_num and guess == "l":
        score += 1
        print("Rätt, din score är: ", score)
    else:
        print("Fel din score var: ", score)
        score = 0
        print("Prova igen")

    return score


main()
