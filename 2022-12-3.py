import pathlib
import string

lower = list(string.ascii_lowercase)
upper = list(string.ascii_uppercase)

def day_3():
    sack = 0
    badge = 0
    line = 0
    badge_list = []
    f = pathlib.Path("2022-12-3-input.txt").read_text().splitlines()
    for item in f:
        divider = (len(item)//2)
        compartment1 = slice(0, divider)
        compartment2 = slice(divider, len(item))
        for character in list(item[compartment1]):
            if character in item[compartment2]:
                if(character not in lower):
                    sack += (upper.index(character) + 27)
                    break
                else:
                    sack += (lower.index(character) + 1)
                    break
        print(sack)
    for lines in f:
        if line == 2:
            line = 0
            badge_list.append(lines)
            for letter in badge_list[0]:
                if(letter in badge_list[1] and letter in badge_list[2]):
                    if(letter not in lower):
                        badge += upper.index(letter) + 27
                        break
                    else:
                        badge += lower.index(letter) + 1
                        break
            badge_list = []
        else:
            badge_list.append(lines)
            line += 1
    print(badge)
day_3()