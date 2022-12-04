# Advent of code Year 2022 Day 4 solution
# Author = ?
# Date = December 2018

class AOC:
    def __init__(self):
        pass

    def part1(self, file): 
        total_included=0
        anyOverLap=0

        with open(dataFile) as file:
            while (line := file.readline().rstrip()):
                elf1, elf2 = line.split(',')               
                elf1 = elf1.split('-')   
                elf2 = elf2.split('-')   

                #one is overlaped by the other
                if ((int(elf1[0]) <= int(elf2[0]) and int(elf1[1]) >= int(elf2[1])) or # elf2 inside elf1
                    (int(elf2[0]) <= int(elf1[0]) and int(elf2[1]) >= int(elf1[1]))):
                    total_included +=1
                    # print(elf1, elf2)

                # either overlap the other
                if ((int(elf1[0]) <= int(elf2[0]) <= int(elf1[1])) or #elf2 starting is between start/end elf1
                    (int(elf1[0]) <= int(elf2[1]) <= int(elf1[1])) or #elf2 end is between start/end elf1
                    (int(elf2[0]) <= int(elf1[1]) <= int(elf2[1])) or #elf1 starting is between start/end elf2
                    (int(elf2[0]) <= int(elf1[1]) <= int(elf2[1])) ): #elf1 end is between start/end elf2
                    anyOverLap +=1

        print("Part one : ", total_included) # 11:03 :11:30 27m
        print("Part two : ", anyOverLap)  #11:30 to 11:40 10m

aoc = AOC()
dataFile = "input.txt"
# dataFile = "test1.txt"
# aoc.readFile(dataFile)
aoc.part1(dataFile)