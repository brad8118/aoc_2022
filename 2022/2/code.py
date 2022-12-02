# Advent of code Year 2022 Day 2 solution
# Author = ?
# Date = December 2018

class Game:
    def __init__(self, opponetSelection=' ', mySelection=' '):
        self.orginialOpponetSelection = opponetSelection
        self.orginialMySelection = mySelection

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
        return "[ME {} {} PTS {}  ---- {}{}]".format(self.mySelection, self.opponetSelection, self.score, self.orginialOpponetSelection , self.orginialMySelection )

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

    def updateMySelectionForPart2(self):
        # X means you need to lose, 
        # Y means you need to end the round in a draw, 
        # and Z means you need to win.

        if self.orginialMySelection == "X": #lose
            if self.opponetSelection == "R":  self.mySelection = "S"
            elif self.opponetSelection == "P":  self.mySelection = "R"
            elif self.opponetSelection == "S":  self.mySelection = "P"

        elif self.orginialMySelection == "Y": #draw
            if self.opponetSelection == "R":  self.mySelection = "R"
            elif self.opponetSelection == "P":  self.mySelection = "P"
            elif self.opponetSelection == "S":  self.mySelection = "S"

        elif self.orginialMySelection == "Z": #win
            if self.opponetSelection == "R":  self.mySelection = "P"
            elif self.opponetSelection == "P":  self.mySelection = "S"
            elif self.opponetSelection == "S":  self.mySelection = "R"  
        else:
            print("!!!!orginial not found!!!!!!!!!!!!!!", self) 


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
                self.matches.append(game)
                self.totalScore += game.score
                # print(game)

    def part1(self): # 10 ->11:30 -> 1.5h
        print("Part One : ", self.totalScore)

    def part2(self): # 11:30 -> 12 -> 30m
        part2Total = 0
        for game in self.matches:
            game.updateMySelectionForPart2()
            game.calculateScore()
            part2Total += game.score
            # print(game)
        print("Part Two : ", part2Total)


aoc = AOC()
dataFile = "input.txt"
aoc.readFile(dataFile)
aoc.part1()
aoc.part2()
