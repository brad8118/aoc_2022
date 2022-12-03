# Advent of code Year 2022 Day 3 solution
# Author = ?
# Date = December 2018

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

    def part2(self): # 11:30 -> 12 -> 30m
        part2Total = 0
        # for game in self.matches:
        #     game.updateMySelectionForPart2()
        #     game.calculateScore()
        #     part2Total += game.score
        #     # print(game)
        print("Part Two : ", part2Total)


aoc = AOC()
dataFile = "input.txt"
# dataFile = "test1.txt"
aoc.readFile(dataFile)
aoc.part1()
aoc.part2()