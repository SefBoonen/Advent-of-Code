games = []
sum_power = 0

f = open("input.txt", "r")
for i in f.readlines():
    games.append("{}".format(i).replace("\n", ""))

for game_i in range(len(games)):
    game_words = games[game_i].split(" ")

    min_red_cubes = 0
    min_green_cubes = 0
    min_blue_cubes = 0

    for word_i in range(2, len(game_words) - 1):
        if "blue" in game_words[word_i + 1] and int(game_words[word_i]) > min_blue_cubes:
            min_blue_cubes = int(game_words[word_i])
        if "red" in game_words[word_i + 1] and int(game_words[word_i]) > min_red_cubes:
            min_red_cubes = int(game_words[word_i])
        if "green" in game_words[word_i + 1] and int(game_words[word_i]) > min_green_cubes:
            min_green_cubes = int(game_words[word_i])

        
    game_power = min_blue_cubes * min_red_cubes * min_green_cubes

    sum_power += game_power
    
print(sum_power)