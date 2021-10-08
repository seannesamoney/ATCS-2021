games = ["Cards", "Temple Run", "Subway Surfers"]
print("These are the games I like: ")
for game in games :
    print(game)

new_game = input("Tell me a game you enjoy: ")
games.append(new_game)

print("These are the games WE like: ")
for game in games :
    print(game)