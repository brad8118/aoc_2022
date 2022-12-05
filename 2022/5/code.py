# Advent of code Year 2022 Day 5 solution
# Author = ?
# Date = December 2018

# ['[T]', '', '', '', '', '[D]', '', '', '', '', '', '', '', '', '[L]']
# ['[R]', '', '', '', '', '[S]', '[G]', '', '', '', '', '[P]', '', '', '', '', '', '', '', '', '[H]']
# ['[G]', '', '', '', '', '[H]', '[W]', '', '', '', '', '[R]', '[L]', '', '', '', '', '[P]']
# ['[W]', '', '', '', '', '[G]', '[F]', '[H]', '[S]', '[M]', '', '', '', '', '[L]']
# ['[Q]', '', '', '', '', '[V]', '[B]', '[J]', '[H]', '[N]', '[R]', '[N]']
# ['[M]', '[R]', '[R]', '[P]', '[M]', '[T]', '[H]', '[Q]', '[C]']
# ['[F]', '[F]', '[Z]', '[H]', '[S]', '[Z]', '[T]', '[D]', '[S]']
# ['[P]', '[H]', '[P]', '[Q]', '[P]', '[M]', '[P]', '[F]', '[D]']
# ['', '1', '', '', '2', '', '', '3', '', '', '4', '', '', '5', '', '', '6', '', '', '7', '', '', '8', '', '', '9']

class AOC_day5:
    def __init__(self):
        self.towers={}
    
    def printTowers(self):
        for i in range(1, len(self.towers.keys()) +1):
            print(i, self.towers[i])
        print("--------------------------------------------")

    def readFile(self, file): #8:20
        with open(dataFile) as file:
            lines = []
            while (line := file.readline().rstrip()):
                lines.append(line)

            #create # of towers
            for i in range(1, int(lines.pop()[-1])+1):
                self.towers[i]=[" "] # fill 1st item with blank.. makes easy to print rows if its empty

            # populate each tower    
            while lines:
                l = lines.pop()
                queueIndex = 1
                index = 0
                items = l.split(" ")
                # print("length", len(l))
                while queueIndex <= 9 and index < len(items):  
                    # print(index, items[index])                  
                    if '[' in items[index]: #item in queue
                        self.towers[queueIndex].append(items[index][1:-1]) #append w/out []
                        queueIndex +=1
                        index +=1
                    else: #skip next 3 items
                        queueIndex +=1
                        index +=4

            #got inputs into towers 9:00
            self.printTowers()

            #now the fum, do the moves
            while (line := file.readline().rstrip()):
                # move 3 from 8 to 9
                itemsToMove = int(line.split(" ")[1])
                source = int(line.split(" ")[3])
                destination = int(line.split(" ")[5])

                # print(itemsToMove, source,destination)
                for i in range(itemsToMove):
                    self.towers[destination].append(self.towers[source].pop())

            self.printTowers()
            part1 = ""            
            for i in range(1, len(self.towers.keys()) +1):
                part1 += self.towers[i][-1]

        print("Part one : ", part1) # 8:20 to 9:41 => 1:21m
        # print("Part two : ", anyOverLap)  

aoc = AOC_day5()
dataFile = "input.txt"
# dataFile = "test1.txt"
aoc.readFile(dataFile)
# aoc.part1(dataFile)