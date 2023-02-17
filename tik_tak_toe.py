# tik-tak-toe
import random

class tik:
    def __init__(self):
        pass
    checklist = [0,1,2,3,4,5,6,7,8]
    l1 = [' '] * 3
    l2 = [' '] * 3
    l3 = [' '] * 3

    def print_game(self) -> None:
        print(*tik.l1, sep = ' | ')
        print(*tik.l2, sep = ' | ')
        print(*tik.l3, sep = ' | ')

    def insert(self, pos: int, letter: str) -> None:
        if(pos >= 0 and pos <= 2):
            tik.l1[pos] = letter
        elif(pos >= 3 and pos <= 5):
            tik.l2[pos - 3] = letter
        else:
            tik.l3[pos - 6] = letter

    def check(self, letter: str) -> bool:
        # horizontal check
        if(tik.l1.count(tik.l1[0]) == 3 and tik.l1[0] != ' '):
            print("\nWinner: ", letter)
            return True
        if(tik.l2.count(tik.l2[0]) == 3 and tik.l2[0] != ' '):
            print("\nWinner: ", letter)
            return True
        if(tik.l3.count(tik.l3[0]) == 3 and tik.l3[0] != ' '):
            print("\nWinner: ", letter)
            return True
        
        # vertical check
        if(tik.l1[0] == tik.l2[0] == tik.l3[0] and tik.l1[0] != ' '):
            print("\nWinner: ", letter)
            return True
        if(tik.l1[1] == tik.l2[1] == tik.l3[1] and tik.l1[1] != ' '):
            print("\nWinner: ", letter)
            return True
        if(tik.l1[2] == tik.l2[2] == tik.l3[2] and tik.l1[2] != ' '):
            print("\nWinner: ", letter)
            return True
        
        # diagonal check
        if(tik.l1[0] == tik.l2[1] == tik.l3[2] and tik.l1[0] != ' '):
            print("\nWinner: ", letter)
            return True
        if(tik.l1[2] == tik.l2[1] == tik.l3[0] and tik.l1[2] != ' '):
            print("\nWinner: ", letter)
            return True
        
        # full check
        if(' ' not in tik.l1 and ' ' not in tik.l2 and ' ' not in tik.l3):
            print("\nDraw")
            return True
        
        return False

obj = tik()
obj.print_game()

while(True):

    print("\nValid Positions: ", tik.checklist)
    x = int(input("You're turn(X): "))
    if(x > 8):
        print("\nNot a position, choose again")
        continue
    if(x in obj.checklist):
        obj.checklist.remove(x)
        obj.insert(x, 'X')
    else:
        print("\nPosition already aquired, choose again")
        continue
    obj.print_game()
    
    if(obj.check('x')):
        break

    print("\nComputer's turn: ")
    o = random.choices(obj.checklist, k = 1)
    int_o = o[0]
    obj.checklist.remove(int_o)
    obj.insert(int_o, 'O')
    obj.print_game()

    if(obj.check('O')):
        break
