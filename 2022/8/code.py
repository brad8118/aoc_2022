# Advent of code Year 2022 Day 8 solution
# Author = ?
# Date = December 2018

class AOC:
    def __init__(self):
        self.grid = []
        self.part1_VisibleTrees = {}

    def readFile(self, file):   
        with open(dataFile) as file:
            while (line := file.readline().rstrip()):
                self.grid.append([int(x) for x in line])

    #true if visible
    def checkVisibility_Left_Right(self, treeLocation):
        # treeLocation = [1,2] # down (y), over(x)
        row = treeLocation[0]
        treeHeight = self.grid[treeLocation[0]][treeLocation[1]]
        tallerFound = False   
        i = 0           
        while i < treeLocation[1]: #left to right            
            t = self.grid[row][i]
            print("[{},{}] -- {}".format(row, i, t))
            i += 1
            if t >= treeHeight:
                tallerFound = True 
                break       

        if tallerFound == False:
            return True 
        
        tallerFound = False   
        i = treeLocation[1] +1 
        while i < len(self.grid[0]): #left to right            
            t = self.grid[row][i]
            print("[{},{}] -- {}".format(row, i, t))
            i += 1
            if t >= treeHeight:
                tallerFound = True 
                break   
     
        return not tallerFound

    #true if visible if 
    def checkVisibility_top_to_bottom(self, treeLocation):
        # treeLocation = [1,2] # down (y), over(x)
        column = treeLocation[1]
        treeHeight = self.grid[treeLocation[0]][treeLocation[1]]
        tallerFound = False   
        i = 0           
        while i < treeLocation[0]: #top to tree          
            t = self.grid[i][column]
            print("[{},{}] -- {}".format(i, column, t))
            i += 1
            if t >= treeHeight:
                tallerFound = True 
                break       

        if tallerFound == False:
            return True 
        
        tallerFound = False   
        i = treeLocation[0] +1 
        while i < len(self.grid): #tree to bottom          
            t = self.grid[i][column]
            print("[{},{}] -- {}".format(i, column, t))
            i += 1
            if t >= treeHeight:
                tallerFound = True 
                break   
     
        return not tallerFound

    def part1(self): #8:50    
        # treeLocation = [2,2] # down, over
        
        for r in range(1, len(self.grid)-1):            
            for c in range(1 ,len(self.grid[0])-1):
                print("Checking Tree", "[{},{}] - {}".format(r,c, self.grid[r][c]))
                visible_row = self.checkVisibility_Left_Right([r,c])
                visible_column = self.checkVisibility_top_to_bottom([r,c])
                if visible_row or visible_column:
                    self.part1_VisibleTrees[(r,c)] = self.grid[r][c]
                    print("visible")

    
        print(self.part1_VisibleTrees)
        insideVisibleTrees = len(self.part1_VisibleTrees)
        total = (len(self.grid) * 2) + (len(self.grid)*2) + insideVisibleTrees - 4
        print("Part One : ",total, "inside", insideVisibleTrees  )

    def part2(self): # 2:24 -> 3:01 => 37m
        totalDiskSpace = 70000000
        requiredSpace = 30000000
        usedSpace = self.paths['/'].getChildDirsAndFileSizes()
        freeDiskSpace = totalDiskSpace - usedSpace
        neededSpace = requiredSpace - freeDiskSpace

        #space dif, path, size of folder
        smallestDrive = (totalDiskSpace, "path", usedSpace)

        for folder in self.paths.values():
            size = folder.getChildDirsAndFileSizes()
            diff = size - neededSpace 
            if diff >= 0 and diff < smallestDrive[0]:
                smallestDrive = (diff, folder.path, size)
                    
        print("Part Two : ", smallestDrive)


aoc = AOC()
dataFile = "input.txt"
# dataFile = 'C:\\Users\\brad\\Documents\\aoc\\aoc_2022\\2022\\8\\test1.txt'
# dataFile = 'test1.txt'
aoc.readFile(dataFile)
aoc.part1()
# aoc.part2()