# Advent of code Year 2022 Day 2 solution
# Author = ?
# Date = December 2018

class ElfCalories:
    def __init__(self):
        self.totalCalories = 0
        self.items = []

    def add(self, calorie):
        self.totalCalories += calorie
        self.items.append(calorie)

class AOC:
    def __init__(self):
        self.elfs = []
        self.max = 0

    def readFile(self, file):
        currentElf = ElfCalories()
        with open(file) as file:
            for line in file:
                calories = line.strip()
                if calories != '':
                    currentElf.add(int(calories))
                else:
                    if currentElf.totalCalories > self.max:
                        self.max = currentElf.totalCalories
                    self.elfs.append(currentElf.totalCalories) #changed for part2- only cares about total
                    currentElf = ElfCalories()
           
                # print("line : ",  calories)

    def part1(self):
        print("Part One : ", self.max)

    def part2(self):
        #sloppy when reading the file I could only keep track of the top 3
        top3 = sorted(self.elfs)[-3:]
        print("Part Two : ", sum(top3))


aoc = AOC()
dataFile = "input.txt"
aoc.readFile(dataFile)
aoc.part1()
aoc.part2()
