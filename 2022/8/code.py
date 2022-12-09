# Advent of code Year 2022 Day 8 solution
# Author = ?
# Date = December 2018

class AOC:
    def __init__(self):
        self.grid = []
        self.part1_VisibleTrees = {}
        self.part2_viewingDistance = 0
    
    def gridWith(self):
        return len(self.grid[0])

    def gridDepth(self):
        return len(self.grid)

    def readFile(self, file):   
        with open(dataFile) as file:
            while (line := file.readline().rstrip()):
                self.grid.append([int(x) for x in line])

    #true if visible
    def checkVisibility_Left_Right(self, treeLocation):
        # treeLocation = [3,2] # down (y), over(x)
        row = treeLocation[0]
        treeHeight = self.grid[treeLocation[0]][treeLocation[1]]
        tallerFound_left = False   
        i = treeLocation[1] -1  
        left_view = 0        
        while i >= 0: #left to right            
            t = self.grid[row][i]
            # print("[{},{}] -- {}".format(row, i, t))
            i -= 1 
            left_view +=1  
            if t >= treeHeight:
                tallerFound_left = True 
                break 
   
        # if tallerFound_left == False:
        #     return True 
        
        tallerFound_right = False   
        i = treeLocation[1] +1 
        right_view =0 
        while i < self.gridWith(): #left to right            
            t = self.grid[row][i]
            # print("[{},{}] -- {}".format(row, i, t))
            i += 1
            right_view +=1  
            if t >= treeHeight:
                tallerFound_right = True 
                break 
     
        return (not (tallerFound_left and tallerFound_right),left_view , right_view)

    #true if visible if 
    def checkVisibility_top_to_bottom(self, treeLocation):
        # treeLocation = [3,2] # down (y), over(x)
        column = treeLocation[1]
        treeHeight = self.grid[treeLocation[0]][treeLocation[1]]
        tallerFound_up = False   
        up_view = 0
        i = treeLocation[0] -1          
        while i >= 0 : #top to tree          
            t = self.grid[i][column]
            # print("[{},{}] -- {}".format(i, column, t))
            i -= 1
            up_view += 1
            if t >= treeHeight:
                tallerFound_up = True 
                break       
        
        tallerFound_down= False
        down_view =0   
        i = treeLocation[0] +1 
        while i < self.gridDepth(): #tree to bottom          
            t = self.grid[i][column]
            # print("[{},{}] -- {}".format(i, column, t))
            down_view += 1
            i += 1
            if t >= treeHeight:
                tallerFound_down = True 
                break   
     
        return (not (tallerFound_up and tallerFound_down),up_view , down_view)

    def search(self): #8:50am -> 6:05 pm     part2 7pm to 
         
        for r in range(1, self.gridDepth()-1):            
            for c in range(1 ,self.gridWith()-1):
                # r,c = 3,2 
                # print("Checking Tree", "[{},{}] - {}".format(r,c, self.grid[r][c]))
                visible_row = self.checkVisibility_Left_Right([r,c])
                visible_column = self.checkVisibility_top_to_bottom([r,c])
                if visible_row[0] or visible_column[0]:
                    distance = visible_row[1] * visible_row[2] * visible_column[1] * visible_column[2]
                    self.part1_VisibleTrees[(r,c)] = "{} -- {}".format(self.grid[r][c], distance)
                    self.part2_viewingDistance = max (self.part2_viewingDistance, distance)
                    # print("visible", self.part2_viewingDistance)

    
        # print(self.part1_VisibleTrees)
        insideVisibleTrees = len(self.part1_VisibleTrees)
        total = (len(self.grid) * 2) + (len(self.grid)*2) + insideVisibleTrees - 4
        print("Part One : ", total, "inside", insideVisibleTrees)
        print("Part Two : ", self.part2_viewingDistance)

aoc = AOC()
dataFile = "input.txt"
# dataFile = 'C:\\Users\\brad\\Documents\\aoc\\aoc_2022\\2022\\8\\test1.txt'
# dataFile = 'test1.txt'
aoc.readFile(dataFile)
aoc.search()
# aoc.part2()