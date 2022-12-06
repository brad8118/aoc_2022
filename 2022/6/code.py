# Advent of code Year 2022 Day 8 solution
# Author = ?
# Date = December 2018

from collections import OrderedDict

class AOC:
    def __init__(self):
        self.dataStream = ""
        self.key = ""
        self.part1_index = 0

    def readFile(self, file):
        with open(dataFile) as file:
            while (line := file.readline().rstrip()):
                self.dataStream = line
                
    def part1(self): #7:35 -> 8:47 => 1h 12m
        lookup = self.dataStream[0:4]
        # print(self.dataStream)
        for i in range(4, len(self.dataStream)):
            # print(lookup, i, self.dataStream[i])
            if len(set(lookup)) == len(lookup):
                self.key = lookup
                self.part1_index = i
                break
            
            lookup = lookup[1:4] + self.dataStream[i]
        print("Part One : ", self.key, self.part1_index)

    def part2(self): #8:47 =>  8:54 => 8m
        lookup = self.dataStream[0:14]
        # print(self.dataStream)
        for i in range(14, len(self.dataStream)):
            # print(lookup, i, self.dataStream[i])
            if len(set(lookup)) == len(lookup):
                self.key = lookup
                self.part1_index = i
                break
            
            lookup = lookup[1:14] + self.dataStream[i]
        print("Part One : ", self.key, self.part1_index)

    # def part1(self): #7:35 ->
    #     lookup = OrderedDict()
    #     lookup[self.dataStream[0]] = 0
    #     lookup[self.dataStream[1]] = 1
    #     lookup[self.dataStream[2]] = 2

    #     if len(list(lookup.keys())) < 3:
    #         self.key = self.dataStream[0:4]
    #         self.part1_index = 5 # last index(+1 to convert to #) and the next index (+1)
    #         return

    #     for i in range(3, len(self.dataStream)):
    #         c = self.dataStream[i]
    #         print(i, c, lookup)
    #         if c not in lookup:
    #             print(c, lookup)
    #             for k,v in lookup.items():
    #                 self.key += k 
    #             self.key += c
    #             self.part1_index = i + 2 # last index(+1 to convert to #) and the next index (+1)
    #             break
    #         else:
    #             del lookup[list(lookup.keys())[0]]
    #             lookup[c] = i



aoc = AOC()
dataFile = "input.txt"
# dataFile = "test1.txt"
aoc.readFile(dataFile)
# aoc.dataStream = "nppdvjthqldpwncqszvftbrmjlhg"
aoc.part1()
aoc.part2()