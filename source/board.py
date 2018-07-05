class Board:
    def __init__(self):
        levelMap={}
        self.levelMap = levelMap
        levelWidth=[]
        self.levelWidth = levelWidth
        levelHeight=[]
        self.levelHeight =levelHeight
        pointPositions={}
        self.pointPositions = pointPositions
        points =[]
        self.points = points
        playerOnPoint = False
        self.playerOnPoint = playerOnPoint

    def createBoard(self,level): #create the gamefield
        gameFile= open(level, 'r')
        rawGameBoard =gameFile.read(-1)
        xCounter =0
        yCounter =0
        gameWidth=0

        for line in rawGameBoard.split('\n'): #check width        
            if (gameWidth < len(line)):
                gameWidth = len(line)   

        for y in rawGameBoard:
            for x in y:
                if x != " " and x !="\n":
                    self.levelMap[(yCounter,xCounter)]= str(x)
                    if x == ".":
                        self.pointPositions[(yCounter,xCounter)]= str(x)
        
                if x== "\n":
                    yCounter+=1
                    xCounter =0
                else :
                    xCounter+=1
        self.points.append(len(self.pointPositions))
        self.points.append(int(0))
        self.levelWidth.append(gameWidth)
        self.levelHeight.append(yCounter)
   
    def getLevel(self):
        return self.levelMap

    def uppdateLevel(self,move):
        #hämtar x och y för player
        playerPosition = self.getPlayerPosition()
        yPlayerPosition = playerPosition[0]
        xPlayerPosition = playerPosition[1]
    
        if self.IfPlayerCanGo(move):
            self.playerOnPoint
    
            if self.playerOnPoint == True:
                marker = "+"
            if self.playerOnPoint == False:
                marker = "@"

            if move == "r":
                #tar bort sig ifrån positionen man befinner sig på
                del self.levelMap[(yPlayerPosition,xPlayerPosition)]
                #uppdaterar kartan dit man för flyttar sig
                self.levelMap[(yPlayerPosition,xPlayerPosition+1)]= marker


            if move == "l":
                del self.levelMap[(yPlayerPosition,xPlayerPosition)]
                self.levelMap[(yPlayerPosition,xPlayerPosition-1)]= marker


            if move == "u":
                del self.levelMap[(yPlayerPosition,xPlayerPosition)]
                self.levelMap[(yPlayerPosition-1,xPlayerPosition)]= marker

            if move == "d":
                del self.levelMap[(yPlayerPosition,xPlayerPosition)]
                self.levelMap[(yPlayerPosition+1,xPlayerPosition)]= marker

    #hämtar player position
    def getPlayerPosition(self):
        for position, player in self.levelMap.items():
            if player == "@" or player == "+":
                return(position)
   

    #def checkMoveble(r):
    
    def IfPlayerCanGo(self,move):  #check if next is #
        self.playerOnPoint = False
        yPlayerPosition = self.getPlayerPosition()[0]
        xPlayerPosition = self.getPlayerPosition()[1]
        print(self.levelMap[(yPlayerPosition,xPlayerPosition)])

        if move == "r":
            pos1= (yPlayerPosition,xPlayerPosition +1)
            pos2= (yPlayerPosition,xPlayerPosition +2) 

        if move == "l":
            pos1= (yPlayerPosition,xPlayerPosition -1)
            pos2= (yPlayerPosition,xPlayerPosition -2)
 
        if move == "u":
            pos1= (yPlayerPosition-1,xPlayerPosition)
            pos2= (yPlayerPosition-2,xPlayerPosition)

        if move == "d":
            pos1= (yPlayerPosition+1,xPlayerPosition)
            pos2= (yPlayerPosition+2,xPlayerPosition)
 
        if(pos1) in self.levelMap:
            print((pos1))
            if self.levelMap[(pos1)] == "#":
                return(False)
            if self.levelMap[(pos1)] == "o" or self.levelMap[(pos1)] == "*":
                if(pos2) in self.levelMap:
                    if self.levelMap[(pos2)] == "#" or self.levelMap[(pos2)] == "o" :
                        return(False)
                    if self.levelMap[(pos2)] == ".":
                        self.levelMap[(pos2)] = "*"
                        self.points[1]+=1
                        return(True)
                    else:
                        self.levelMap[(pos2)]="o"
                        return(True)
                else:
                    self.levelMap[(pos2)]="o"
                    return(True)
            if self.levelMap[(pos1)] == ".":
                self.playerOnPoint = True
                self.points[1]+=1
                return(True)

            else:
                return(True)
        else:
            return(True)
    

    def checkWinning(self):
        playerPosition= self.getPlayerPosition()
        print(self.points)
        for pp in self.pointPositions:
            if not pp in self.levelMap:
                self.levelMap[pp]="."
                self.points[1]-=1
        if self.points[0] == self.points[1]:
            if not playerPosition in self.pointPositions:
                return(True)
            return(False)
        return(False)
