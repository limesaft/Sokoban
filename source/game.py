from board import * 

def main():
    flag = True
    theBoard = Board()
    printStart(theBoard)
    while flag:
        printLevel(theBoard)
        move = input("Make your move (l)eft, (r)ight, (u)p, (d)own:?"+'\n')
        if move == "l" or move == "r" or move == "u" or move == "d":
            theBoard.uppdateLevel(move)
            if theBoard.checkWinning():
                print('\n'*30)
                print("youwan!")
                break


def printStart(theBoard):
    print('\n'*30)
    print ("Welcome to Sokoban, please choose a level:")                                 
    print("1. first_level")
    print("2. second_level")
    print("3. my_level")
    flag = True
    while (flag == True):
        level = input("Choose: ")
        
        if (level == "1"):
            flag = False
            theBoard.createBoard("firstlevel.txt")
            
        elif(level == "2"):
            flag = False
            theBoard.createBoard("secondlevel.txt")
            
        elif(level == "3"):
            flag = False
            theBoard.createBoard("mylevel.txt")
  
        else:
            print("Level doesnt exist, choose new!" + '\n')


def printLevel(theBoard):
    print("\n"*20)
    level = theBoard.getLevel()
    height = theBoard.levelHeight[0]
    width = theBoard.levelWidth[0]
    y = 0
    x = 0
    for y in range(height):
        for x in range(width):
            if (y,x) in level:
                print(level[(y,x)], end="")
            else:
                print(" ",end="")
        print()
            
main()
