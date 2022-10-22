theBoard={8:8,3:3,4:4,1:1,5:5,9:9,6:6,7:7,2:2}
l=[1,2,3,4,5,6,7,8,9]
C=[]
P=[]
turns=['X','O']
board_keys=[]
for key in theBoard:
    board_keys.append(key)
def printBoard(board):
    print(str(board[8])+'|'+str(board[3])+'|'+str(board[4]))
    print('-+-+-')
    print(str(board[1])+'|'+str(board[5])+'|'+str(board[9]))
    print('-+-+-')
    print(str(board[6])+'|'+str(board[7])+'|'+str(board[2]))

def make():
    if theBoard[5] not in turns:
        return 5
    elif theBoard[7] not in turns:
        return 7
    elif theBoard[9] not in turns:
        return 9
    elif theBoard[3] not in turns:
        return 3
    elif theBoard[1] not in turns:
        return 1

def switch_player(count):
    if count%2!=0 :
        current_player='C' 
    else :
        current_player='H'
    return current_player


def go(move):
    theBoard[move]='O'
    C.append(move)

def posswin():
    for i in C:
        for j in C:
            if i!=j:
                x=15-(i+j)
                if x in l and theBoard[x] not in turns:
                    return x
    for i in P:
        for j in P:
            if i!=j:
                x=15-(i+j)
                if x in l and theBoard[x] not in turns:
                    return x
    return 0

       
def checkwin(current_player):
    for i in C:
        for j in C:
            for k in C:
                if i!=j and i!=k and j!=k:
                    if i+j+k==15:
                        printBoard(theBoard)
                        print("Game Over!!!.")
                        print(" *** Computer won. *** ")
                        return 1
   
    for i in P:
        for j in P:
            for k in P:
                if i!=j and i!=k and j!=k:
                    if i+j+k==15:
                        printBoard(theBoard)
                        print("Game Over!!!.")
                        print(" *** Player won. *** ")
                        return 1
    return 0        
             
def game():
    count=0
    current_player="H"
    for i in range(9):
        printBoard(theBoard)
        if current_player=="H":
            print("It's your turn.Move to which place?")
            move=int(input())
            while move not in [1,2,3,4,5,6,7,8,9]:
                    print("Invalid move.\nMove to which place?")
                    move=int(input())
            if theBoard[move] not in turns:
                theBoard[move]='X'
                P.append(move)
                count+=1
            else:
                print("That place is already filled.\nMove to which place?")
                move=int(input())
                while move not in [1,2,3,4,5,6,7,8,9]:
                    print("That place is invalid.\nMove to which place?")
                    move=int(input())
                if theBoard[move] not in turns:
                    theBoard[move]='X'
                    P.append(move)
                count+=1
            current_player=switch_player(count)
        else:
            poss=posswin()
            if poss==0:
                x=make()
                go(x)
            else:
                go(poss)
            print("\nComputer's move\n")
            count+=1
            current_player=switch_player(count)
       
        if count>=5:
            flag=checkwin(current_player)
            if flag:
                break
        if count==9:
            printBoard(theBoard)
            print("Game Over.\n")
            print("it's a tie!!!")
    restart=input("Do you want to play again?(y/n)")
    if restart=="y" or restart=="Y":
        for key in board_keys:
            theBoard[key]=key
            C.clear()
            P.clear()
        game()
if __name__=="__main__":
    game()
