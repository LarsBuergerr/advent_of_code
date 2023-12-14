data = open('input.txt', 'r')
sum = 0
valid_spelled_nums = [("one", 1), ("two", 2), ("three", 3), ("four", 4), ("five", 5), ("six", 6), ("seven", 7), ("eight", 8), ("nine", 9)]

for line in data:
    matches_w_index = []
    for num in valid_spelled_nums:
        index_first = line.find(num[0])
        index_last = line.rfind(num[0])
        if index_first != -1:
            matches_w_index.append((index_first, num[0]))
        if index_last != -1:
            matches_w_index.append((index_last, num[0]))

    for index, character in enumerate(line):
        
        if character.isnumeric():
            matches_w_index.append((index, character))
    
    lowest_entry =  None
    lowest_entry_num = ""
    highest_entry = None
    highest_entry_num = ""
      
    for entry in matches_w_index:
        if lowest_entry is None or entry[0] < lowest_entry:
            lowest_entry = entry[0]
            lowest_entry_num = entry[1]
    
        if highest_entry is None or entry[0] > highest_entry:
            highest_entry = entry[0]
            highest_entry_num = entry[1]
    
    if lowest_entry_num.isdigit():
        lowest_int = int(lowest_entry_num)
    else:
        for entry in valid_spelled_nums:
            if entry[0] == lowest_entry_num:
                lowest_int = entry[1]
                
    if highest_entry_num.isdigit():
        highest_int = int(highest_entry_num)
    else:
        for entry in valid_spelled_nums:
            if entry[0] == highest_entry_num:
                highest_int = entry[1]
                
    combined = str(lowest_int) + str(highest_int)
    sum += int(combined)

print(sum)      