import pathlib

#A = X = Rock (1) or lose
#B = Y = Paper (2) or draw
#C = Z = Scissors (3) or win
#win = 6
#draw = 3
#lose = 0

def day_2_part_1():
    score = 0
    f = pathlib.Path("2022-12-2-input.txt").read_text().splitlines()
    for matches in f:
        if matches[0] == "A":
            if matches[2] == "X":
                score += 4
            elif matches[2] == "Y":
                score += 8
            elif matches[2] == "Z":
                score += 3
        elif matches[0] == "B":
            if matches[2] == "X":
                score += 1
            elif matches[2] == "Y":
                score += 5
            elif matches[2] == "Z":
                score += 9
        elif matches[0] == "C":
            if matches[2] == "X":
                score += 7
            elif matches[2] == "Y":
                score += 2
            elif matches[2] == "Z":
                score += 6
    print(score)

def day_2_part_2():
    score = 0
    f = pathlib.Path("2022-12-2-input.txt").read_text().splitlines()
    for matches in f:
        if matches[0] == "A":
            if matches[2] == "X":
                score += 3
            elif matches[2] == "Y":
                score += 4
            elif matches[2] == "Z":
                score += 8
        elif matches[0] == "B":
            if matches[2] == "X":
                score += 1
            elif matches[2] == "Y":
                score += 5
            elif matches[2] == "Z":
                score += 9
        elif matches[0] == "C":
            if matches[2] == "X":
                score += 2
            elif matches[2] == "Y":
                score += 6
            elif matches[2] == "Z":
                score += 7
    print(score)

day_2_part_1()
day_2_part_2()
    