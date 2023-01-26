import random
from sqlite_demo import call_db

# QUERIES
create_highcores_table = """
CREATE TABLE IF NOT EXISTS high_scores (
    id INTEGER PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    score INTEGER NOT NULL
)
"""
get_highscore_query = """
SELECT name, score FROM high_scores
"""
save_score_query = f"""
        INSERT INTO high_scores (
            name,
            score
        ) VALUES (
            ?,
            ? 
        )
        """
# /QUERIES

call_db(create_highcores_table)


max = 10
min = 1

score = 0
random_num = random.randint(min, max)


def print_highscore():
    print("_______HIGHSCORES_______")
    highscores = call_db(get_highscore_query)
    for highscore in highscores:
        name, score = highscore
        print(f"{name}: {score}")
    print("_______HIGHSCORES_______")


print_highscore()

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
        name = input("Skriv in ditt namn: ")
        # save_score_query = f"""
        # INSERT INTO high_scores (
        #     name,
        #     score
        # ) VALUES (
        #     '{name}',
        #     '{score}'
        # )
        # """
        call_db(save_score_query, name, score)
        score = 0
        print("Prova igen")
        print_highscore()

    random_num = new_num
