red_cubes = 12
green_cubes = 13
blue_cubes = 14

games = []
possible = {}
id_sum = 0

def game_set_possible(x):
    x = x.split(" ")

    for word_i in range(len(x) - 1):
        if "blue" in x[word_i + 1] and int(x[word_i]) > blue_cubes:
            return False
        if "red" in x[word_i + 1] and int(x[word_i]) > red_cubes:
            return False
        if "green" in x[word_i + 1] and int(x[word_i]) > green_cubes:
            return False
    
    return True

f = open("input.txt", "r")
for i in f.readlines():
    games.append("{}".format(i).replace("\n", ""))

for game_i in range(len(games)):
    game_possible = True
    game_words = games[game_i].split(" ")
    game_sets = games[game_i].split(";")

    for game_set in game_sets:
        if not game_set_possible(game_set):
            game_possible = False
            break
        
    if game_possible:
        possible["{}{}".format(game_words[0], game_words[1]).replace(":", "")] = True
        id_sum += int(game_words[1].replace(":", ""))
    else:
        possible["{}{}".format(game_words[0], game_words[1]).replace(":", "")] = False
    
print(id_sum)
print(possible)