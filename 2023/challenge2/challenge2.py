color_dict = {
    "red": 12,
    "green": 13,
    "blue": 14
}

data = open('input.txt', 'r')
sum = 0

for game in data:
    valid_game = True
    tries_of_game = game.split(";")
    game_num = tries_of_game[0].split(":")[0][5:] 
    tries_of_game[0] = tries_of_game[0].split(":")[1]
    
    for tryy in tries_of_game:
        colors = tryy.split(",")
        for color in colors:
            num_and_color = color.split(" ")
            num_and_color.pop(0)
            
            if int(num_and_color[0]) > int(color_dict[num_and_color[1].rstrip("\n")]): 
                valid_game = False
                break
    if valid_game:
        sum += int(game_num)
    
print(sum)