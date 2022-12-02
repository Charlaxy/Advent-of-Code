import pathlib

def day_1():
    food = []
    elf = 0
    f = pathlib.Path("2022-12-1-input.txt").read_text().splitlines()
    for calories in f:
        if calories:
            elf += int(calories)
        else:
            food.append(elf)
            elf = 0
    food.sort()
    print (max(food))
    print (sum(food[-3:]))
    
day_1()
    