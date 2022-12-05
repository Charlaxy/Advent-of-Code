import pathlib
import string

def day_4_1():
    fully_contained = 0
    f = pathlib.Path("2022-12-4-input.txt").read_text().splitlines()
    for assignment in f:
        parts = assignment.split(",")
        range1 = tuple(map(int, parts[0].split("-")))
        range2 = tuple(map(int, parts[1].split("-")))
        if range1[0] <= range2[0] and range1[1] >= range2[1]:
            fully_contained += 1
        elif range2[0] <= range1[0] and range2[1] >= range1[1]:
            fully_contained += 1
    print(fully_contained)

def day_4_2():
    filepath = "2022-12-4-input.txt"
    points = 0
    with open(filepath) as fp:
        line = fp.readline()
        while line:
            line = line.strip()
            left = line.split(",")[0]
            leftStart = int(left.split("-")[0].strip())
            leftStop = int(left.split("-")[1].strip())
            leftRange = range(leftStart, leftStop+1)
        
            right = line.split(",")[1]
            rightStart = int(right.split("-")[0].strip())
            rightStop = int(right.split("-")[1].strip())
            rightRange = range(rightStart, rightStop+1)
        
            ls = set(leftRange) 
            rs = set(rightRange)
            overlap = ls & rs
        
            if len(overlap)>0:
                points+=1

            line = fp.readline()
    print(points)

day_4_1()
day_4_2()