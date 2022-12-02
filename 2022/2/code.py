# Advent of code Year 2022 Day 2 solution
# Author = ?
# Date = December 2018

class Game:
    def __init__(self, opponetSelection=' ', mySelection=' '):
        self.orginialOpponetSelection = opponetSelection
        self.orginialMySelection = opponetSelection

        #convert ABC XYZ to R P S
        if opponetSelection == "A":  opponetSelection = "R"
        if mySelection == "X":  mySelection = "R"
        if opponetSelection == "B":  opponetSelection = "P"
        if mySelection == "Y":  mySelection = "P"
        if opponetSelection == "C":  opponetSelection = "S"
        if mySelection == "Z":  mySelection = "S"

        self.opponetSelection = opponetSelection
        self.mySelection = mySelection
        self.score = "NOT SET"

    def __repr__(self):
        return "[ME {} {} PTS {} ]".format(self.mySelection, self.opponetSelection, self.score)

    def __str__(self):
        return self.__repr__()

    def calculateScore(self):
        if self.opponetSelection == ' ' or self.mySelection ==' ':
            raise Exception("Can't calculate", "mySelection", self.mySelection, "opponetSelection", self.opponetSelection)

        self.score  = 0
        if self.mySelection == "R": #rock ==1
            self.score  = 1
        elif self.mySelection == "P": #paper ==2
            self.score  = 2
        else:    #Scissor==3
            self.score  = 3

        if self.mySelection == self.opponetSelection: #draw==3pts
            self.score  += 3
        elif ((self.mySelection == "R" and self.opponetSelection == "S") or # i win ==6pts
            (self.mySelection == "P" and self.opponetSelection == "R") or
            (self.mySelection == "S" and self.opponetSelection == "P")):
            self.score  += 6
        else: #lose 0pts
            self.score  += 0


class AOC:
    def __init__(self):
        self.matches = []
        self.totalScore = 0

    def strategyGuide(self, opponetSelection):
        pass


    def readFile(self, file):
        with open(dataFile) as file:
            while (line := file.readline().rstrip()):
                them, me = line.split(" ")
                game = Game(them, me)
                game.calculateScore()
                self.totalScore += game.score
                print(game)

    def part1(self):
        print("Part One : ", self.totalScore)

    def part2(self):
        print("Part Two : ", "")


aoc = AOC()
dataFile = "input.txt"
aoc.readFile(dataFile)
aoc.part1()
# aoc.part2()
