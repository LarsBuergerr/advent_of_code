with open("input.txt") as f:
    lines = f.readlines()
    

sum_of_each_elf = []
current_elf = 0

for line in lines:
    
    if len(line) == 1:
        sum_of_each_elf.append(current_elf)
        current_elf = 0
    else:
        current_elf += int(line)
        
print(max(sum_of_each_elf))