

data = open('input.txt', 'r')
sum = 0

for game in data:
    color_dict = {
    "red": 0,
    "green": 0,
    "blue": 0
    }
    
    tries_of_game = game.split(";")
    game_num = tries_of_game[0].split(":")[0][5:] 
    tries_of_game[0] = tries_of_game[0].split(":")[1]
    
    for tryy in tries_of_game:
        colors = tryy.split(",")
        for color in colors:
            num_and_color = color.split(" ")
            num_and_color.pop(0)
            
            if int(num_and_color[0]) > int(color_dict[num_and_color[1].rstrip("\n")]): 
                color_dict[num_and_color[1].rstrip("\n")] = num_and_color[0]
    
    color_pow = int(color_dict['red']) * int(color_dict['green']) * int(color_dict['blue'])
    sum += color_pow
    
print(sum)