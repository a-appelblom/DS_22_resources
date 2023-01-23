from random import choice


def main():
    replies = ["It is certain.",
               "It is decidedly so.",
               "Without a doubt.",
               "Yes definitely.",
               "You may rely on it.",
               "As I see it, yes.",
               "Most likely.",
               "Outlook good.",
               "Yes.",
               "Signs point to yes.",
               "Reply hazy, try again.",
               "Ask again later.",
               "Better not tell you now.",
               "Cannot predict now.",
               "Concentrate and ask again.",
               "Don't count on it.",
               "My reply is no.",
               "My sources say no.",
               "Outlook not so good.",
               "Very doubtful.",
               ]
    will_continue = True
    while will_continue:
        random_answer = choice(replies)
        print("")
        print("Ask the almighty ball for answers!")
        input(">>> ")
        print(random_answer)
        print("")

        while True:
            choice__string = input("Do you have another question (y/n)?: ")
            if choice__string == "y":
                will_continue = True
                break
            elif choice__string == "n":
                will_continue = False
                break
            else:
                print("Please enter y or n")


if __name__ == "__main__":
    main()
