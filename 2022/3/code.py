# Advent of code Year 2022 Day 3 solution
# Author = ?
# Date = December 2018

from collections import defaultdict

class AOC:
    def __init__(self):
        self.letters = []
        self.totalpriority = 0
        self.letterValue = {}

        for i, l in enumerate("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"):
            self.letterValue[l] = i+1

    def readFile(self, file):
        with open(dataFile) as file:
            while (line := file.readline().rstrip()):
                lookup = {}
                halfed = len(line)/2
                for i, l in enumerate(line):
                    if i < halfed:
                        lookup[l]=''
                    elif l in lookup:
                        # print(l, self.letterValue[l])
                        self.totalpriority += self.letterValue[l]
                        break


    def part1(self): # 6:20 -> 6:50 : 30m
        print("Part One : ", self.totalpriority)

    def part2(self, file): # 6:50 -> 7:25: 35m
        self.totalpriority = 0
        grouping = []

        with open(dataFile) as file:
            while (line := file.readline().rstrip()):
                lookup = {}
                for l in line:
                    lookup[l] = True                    
                
                grouping.append(lookup)

                if len(grouping) == 3:
                    for key in grouping[0]:
                        if key in grouping[1] and key in grouping[2]:
                            self.totalpriority += self.letterValue[key]
                            grouping = []
                            break
            
        print("Part Two : ", self.totalpriority)


aoc = AOC()
dataFile = "input.txt"
# dataFile = "test1.txt"
aoc.readFile(dataFile)
aoc.part1()
aoc.part2(dataFile)