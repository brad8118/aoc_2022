# Advent of code Year 2022 Day 9 solution
# Author = ?
# Date = December 2018

from collections import Counter

class Point:
    def __init__(self):
        self.X = 0 #left right
        self.Y = 0 #up down

    def __repr__(self):
        return "[{},{}]".format(self.X, self.Y)

    def __str__(self):
        return self.__repr__()


class AOC:
    def __init__(self):
        self.moves = [] #(direction, #moves)
        self.tailLocations = Counter()
        self.h = Point()
        self.t = Point()
        
    def readFile(self, file):   
        with open(dataFile) as file:
            while (line := file.readline().rstrip()):
                direction, move = line.split()
                self.moves.append((direction, int(move)))

    # def getDiff(self, x: Point, y: Point):
        
    def moveHead(self, d):
        if d == "U":
            self.h.Y += 1
        elif d == "D":
            self.h.Y -= 1
        elif d == "L":
            self.h.X -= 1
        elif d == "R":
            self.h.X += 1    


    def moveTail(self, d):
        # ......
        # .XXX..
        # .X0X..
        # .XXX..
        # ...... 
        neighbors = [
            (self.h.X-1, self.h.Y+1), (self.h.X+0, self.h.Y+1), (self.h.X+1, self.h.Y+1),
            (self.h.X-1, self.h.Y+0), (self.h.X+0, self.h.Y+0), (self.h.X+1, self.h.Y+0),
            (self.h.X-1, self.h.Y-1), (self.h.X+0, self.h.Y-1), (self.h.X+1, self.h.Y-1)]

        if (self.t.X, self.t.Y) in neighbors:
            return False

        # .....    .....    .....
        # .....    .....    .....
        # ..H.. -> ...H. -> ..TH.
        # .T...    .T...    .....
        # .....    .....    .....
        # diagonal and more than a space away
        # if self.h.X != self.t.X and self.h.Y != self.t.Y: 
        
        self.t.X, self.t.Y = self.h.X, self.h.Y

        if d == "U":
            self.t.Y -= 1
        elif d == "D":
            self.t.Y += 1
        elif d == "L":
            self.t.X += 1
        elif d == "R":
            self.t.X -= 1  
                
        self.tailLocations[(self.t.X, self.t.Y)] +=1
        return True
    
    def part1(self): # 8:07
        self.tailLocations[(0, 0)] +=1
        for move in self.moves:
            print("moving", move, "h:", self.h, "t:", self.t )
            for m in range(move[1]):
                self.moveHead(move[0])
                # print(self.h)
                self.moveTail(move[0])
                # print(self.t)
                # print("----------------")

    
        print("Part One : ", len(self.tailLocations)) 



# print("Part Two : "+ str(None))


aoc = AOC()
dataFile = "input.txt"
# dataFile = 'C:\\Users\\brad\\Documents\\aoc\\aoc_2022\\2022\\9\\test1.txt'
# dataFile = 'test1.txt'
aoc.readFile(dataFile)
aoc.part1()
# aoc.part2()