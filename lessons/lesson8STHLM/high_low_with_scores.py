import random
from sqlite_demo import call_db

max = 10
min = 1

score = 0


random_num = random.randint(min, max)

# Queries
create_table_query = """
CREATE TABLE IF NOT EXISTS score (
    name VARCHAR(80),
    score INTEGER
    )
"""

get_high_scores_query = """
SELECT * FROM score 

"""
create_score = f"""
INSERT INTO score (name, score) VALUES (?, ?)
"""
# / Queries


call_db(create_table_query)


def print_scores():
    scores = call_db(get_high_scores_query)
    print("_______Highscores________")
    if len(scores) == 0:
        print("No score yet")
    else:
        for the_score in scores:
            name, highscore = the_score
            print(f"{name}: {highscore}")
    print("___________________________")


print_scores()


while True:
    print("Ditt nummer är: ", random_num)

    guess = input("Vad är din gissning högre eller lägre? (h/l) (exit): ")

    if guess != "h" and guess != "l" and guess != "exit":
        continue

    if guess == "exit":
        print("Tack för att du spelade")
        break

    new_num = random.randint(min, max)

    if new_num >= random_num and guess == "h":
        score += 1
        print("Rätt, din score är: ", score)
    elif new_num <= random_num and guess == "l":
        score += 1
        print("Rätt, din score är: ", score)
    else:
        print("Fel din score var: ", score)
        name = input("Ange namn: ")

        call_db(create_score, name, score)
        score = 0
        print_scores()
        print("Prova igen")

    random_num = new_num
