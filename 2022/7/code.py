# Advent of code Year 2022 Day 7 solution
# Author = ?
# Date = December 2018

from collections import defaultdict

class Folder:
    def __init__(self, path, dirName):
        self.parentPath = path 
        self.path = path + dirName + "/"
        self.dirName = dirName
        self.files = {} #name=size
        self.fileSizeTotal = 0
        self.childDirs = {}  ## lookup of full path
        self.childDirectorySize = 0 
    
    def addFile(self, name, size):
        if name not in self.files:
            self.files[name] = size
            self.fileSizeTotal += size

    def addDir(self, dirName):
        path = self.path + dirName + '/'

        if path not in self.childDirs:           
            self.childDirs[path] = dirName

    def getChildDirsAndFileSizes(self):
        return self.childDirectorySize + self.fileSizeTotal

    def __repr__(self):
        return "[{} PARENT:{} FILES:{}  CHILD_DIRS:{}]".format(self.path, self.parentPath, self.files, self.childDirs)

    def __str__(self):
        return self.__repr__()

class AOC:
    def __init__(self):
        self.paths = {}

    def navigatedToDirectory(self, path):
        if path not in self.paths:
            # print("ADDING KEY", path, self.paths.keys())
            lastSlash = path[0:-1].rfind("/")
            parentPath = path[0:lastSlash+1]   
            name = path[lastSlash+1:-1]
            dir = Folder(parentPath, name)
            self.paths[dir.path] = dir
            # print("DONE Adding KEY", path, self.paths.keys())


    def readFile(self, file):
        print('----------------------------------------------')
        currentPath = "/"
        self.paths['/'] = Folder('/','')
        self.paths['/'].parentPath=None
        self.paths['/'].path='/'
        

        with open(dataFile) as file:
            while (line := file.readline().rstrip()):
                print(line, "::", currentPath)
                if line == "$ cd ..": ## up one
                    lastSlash = currentPath[0:-1].rfind("/")
                    currentPath = currentPath[0:lastSlash+1]       
                    self.navigatedToDirectory(currentPath) ## don't think this is required.. but if someone were to jump cd /a/b/c and never saw b            
                elif line == "$ cd /": ## root
                    currentPath = "/"
                    # self.navigatedToDirectory(currentPath)
                elif line.startswith("$ cd"): ## Moves down  -> '$ cd brfl'
                    name = line.split(" ")[2]
                    currentPath = currentPath + name + '/'                    
                    self.navigatedToDirectory(currentPath)
                elif line == "$ ls":
                    pass # just listing the current dirs
                elif line.startswith("dir"):## dir btgrv
                    name = line.split(" ")[1]
                    # path = currentPath + name + '/' 
                    self.paths[currentPath].addDir(name)                    
                else: ## should be a file -> 45629 qgj.jjs
                    if len(line.split(" ")) != 2:
                        raise Exception("line not handled", line)
                    size, name = line.split(" ")
                    self.paths[currentPath].addFile(name, int(size))

    def calculateFoldSizes(self):
        groupedByDepth = {}
        deepest=0
        print(self.paths)
        for k in self.paths:
            depth = k.count('/')
            if depth in groupedByDepth:
                groupedByDepth[depth].append(k)
            else:
                groupedByDepth[depth] = [k]
                deepest = max(depth, deepest) ## set the bottom

        for d in range(deepest, 0, -1): # loop backwards.. calculate the deepest folders 1st and work up level by level
            for path in groupedByDepth[d]:
                dir = self.paths[path]                
                for childPath in dir.childDirs.keys():
                    childDir = self.paths[childPath]
                    dir.childDirectorySize += childDir.getChildDirsAndFileSizes()

        top = self.paths['/']
        print(top.getChildDirsAndFileSizes())


    def part1(self): #9 -> 2:24 meetings today :( 5h 24m
        # dirs with less than/ equal 100000
        total = 0
        for folder in self.paths.values():
            size = folder.getChildDirsAndFileSizes()
            if size <= 100000:
                total += size

        print("Part One : ", total)

    # def part2(self, file): # 2:24
    #     self.totalpriority = 0
    #     grouping = []

    #     with open(dataFile) as file:
    #         while (line := file.readline().rstrip()):
    #             lookup = {}
    #             for l in line:
    #                 lookup[l] = True                    
                
    #             grouping.append(lookup)

    #             if len(grouping) == 3:
    #                 for key in grouping[0]:
    #                     if key in grouping[1] and key in grouping[2]:
    #                         self.totalpriority += self.letterValue[key]
    #                         grouping = []
    #                         break
            
    #     print("Part Two : ", self.totalpriority)


aoc = AOC()
dataFile = "input.txt"
# dataFile = 'C:\\Users\\brad\\Documents\\aoc\\aoc_2022\\2022\\7\\test1.txt'
aoc.readFile(dataFile)
aoc.calculateFoldSizes()
aoc.part1()
# aoc.part2()