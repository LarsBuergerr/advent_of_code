import re

def print_all_neighbours(x, y, neighbours):
    
    print(f'[{x}|{y}]: ')
    for neighbour in neighbours:
        print(f'{matrix[neighbour[0]][neighbour[1]]},', end=" ")
    print()

matrix = []
sum = 0

with open("input.txt", "r") as data:
    for index, line in enumerate(data):
        matrix.append([])
        for character in line:
            matrix[index].append(character)
        matrix[index].pop()

    print(matrix[2][29])
    data.seek(0)
    
    for x, line in enumerate(data):
        for y, character in enumerate(line):
            
            if character != "*":
                continue
            
            top_nums_index = []
            bot_nums_index = []
            side_nums_index = []
            
            top_neighbours  = [(x - 1, y - 1), (x - 1, y),(x - 1, y + 1)]
            side_neighbours = [(x, y - 1), (x, y + 1)]
            bot_neighbours  = [(x + 1, y - 1), (x + 1, y), (x + 1, y + 1)]

            if y > 0:
                if matrix[top_neighbours[1][0]][top_neighbours[1][1]].isnumeric():
                    top_nums_index.append(top_neighbours[1])
                
                else:
                    if matrix[top_neighbours[0][0]][top_neighbours[0][1]].isnumeric():
                        top_nums_index.append(top_neighbours[0])
                    
                    if matrix[top_neighbours[2][0]][top_neighbours[2][1]].isnumeric():
                        top_nums_index.append(top_neighbours[2])
                    
            if y < (len(matrix[0]) - 1):
                if matrix[bot_neighbours[1][0]][bot_neighbours[1][1]].isnumeric():
                    bot_nums_index.append(bot_neighbours[1])
                
                else:
                    if matrix[bot_neighbours[0][0]][bot_neighbours[0][1]].isnumeric():
                        bot_nums_index.append(bot_neighbours[0])
                    
                    if matrix[bot_neighbours[2][0]][bot_neighbours[2][1]].isnumeric():
                        bot_nums_index.append(bot_neighbours[2])
            
            if x > 0:
                if matrix[side_neighbours[0][0]][side_neighbours[0][1]].isnumeric():
                    side_nums_index.append(side_neighbours[0])
            
            if x < len(matrix) - 1:
                if matrix[side_neighbours[1][0]][side_neighbours[1][1]].isnumeric():
                    side_nums_index.append(side_neighbours[1])
            
            all_indices = top_nums_index + bot_nums_index + side_nums_index
            
            if len(all_indices) != 2:
                continue

            sum_of_gear = 0
            first_num = None
            for index in all_indices:
                num = matrix[index[0]][index[1]]
                next_char_left = index[1] - 1
                print(f'[{index[0]}|{next_char_left}]')
                next_char_right = index[1] + 1
                print(f'[{index[0]}|{next_char_right}]')
                
                while(next_char_left > 0  and matrix[index[0]][next_char_left].isnumeric()):
                    num = matrix[index[0]][next_char_left] + num
                    print(f"NEW NUM BY APPENDING LEFT: {num}")
                    next_char_left -= 1
                
                while(next_char_right < len(matrix[0]) and matrix[index[0]][next_char_right].isnumeric()):
                    num = num + matrix[index[0]][next_char_right]
                    print(f"NEW NUM BY APPENDING RIGHT: {num}")
                    next_char_right += 1
                
                if first_num is None:
                    first_num = num
                else:
                    sum_of_gear = int(first_num) * int(num)
                    
            sum += sum_of_gear
            print(f'[{x},{y}] = {top_nums_index + bot_nums_index + side_nums_index} | len = {len(all_indices)} | sum = {sum_of_gear}')
            
    print(sum)