# #WAP to create TIC-TAC-TOE
import random
# def check():
#     if A1==B1==C1=='X'or A2==B2==C2=='X'or A3==B3==C3=='X'or A1==B2==C3=='X'or C1==B2==A3=='X'or A1==A2==A3=='X' or B1==B2==B3=='X' or C1==C2==C3=='X':
#         if player=='X':
#             print("Player win !")
#         else:
#             print("Computer win !")
#     else:
#         if player=='O':
#             print("Player win !")
#         else:
#             print("Computer win !")


# x=[[' ',' ',' '],
#    [' ',' ',' '],
#    [' ',' ',' ']]
# print("    A | B | C ")
# print()
# print("1  ",x[0][0],"|",x[0][1],"|",x[0][2],
# "\n"  "-   --|---|--")
# print("2  ",x[1][0],"|",x[1][1],"|",x[1][2],"\n"
# "-   --|---|--",)
# print("3  ",x[2][0],"|",x[2][1],"|",x[2][2],"\n")

# player=input("What do you want ('X' or 'O').: ").upper()
# if player !='X' and player != 'O':
#     print("Invalid Input !")
# if player=='X':
#     computer='O'
# else:
#     computer='X'

# A1=x[0][0]
# A2=x[1][0]
# A3=x[2][0]
# B1=x[0][1]
# B2=x[1][1]
# B3=x[2][1]
# C1=x[0][2]
# C2=x[1][2]
# C3=x[2][2]

# print("    A | B | C ")
# print()
# print("1  ",A1,"|",B1,"|",C1,
# "\n"  "-   --|---|--")
# print("2  ",A2,"|",B2,"|",C2,"\n"
# "-   --|---|--",)
# print("3  ",A3,"|",B3,"|",C3,"\n")

# print("Lets Start !")



# check()


def print_board():
    print("    A | B | C ")
    print()
    print(f"1   {x[0][0]} | {x[0][1]} | {x[0][2]}")
    print("   ---|---|---")
    print(f"2   {x[1][0]} | {x[1][1]} | {x[1][2]}")
    print("   ---|---|---")
    print(f"3   {x[2][0]} | {x[2][1]} | {x[2][2]}")
    print()

def check():
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if x[i][0] == x[i][1] == x[i][2] == player or x[0][i] == x[1][i] == x[2][i] == player:
            print(f"{player} wins!")
            return True
    if x[0][0] == x[1][1] == x[2][2] == player or x[0][2] == x[1][1] == x[2][0] == player:
        print(f"{player} wins!")
        return True
    return False
x = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
print_board()
player = input("What do you want ('X' or 'O'): ").upper()
if player != 'X' and player != 'O':
    print("Invalid Input!")
else:
    if player == 'X':
        computer = 'O'
    else:
        computer = 'X'
    print("Let's Start!")
    while True:
        print_board()
        move = input("Enter your move (e.g., A1): ").upper()
        row = int(move[1]) - 1
        col = ord(move[0]) - ord('A')
        if x[row][col] == ' ':
            x[row][col] = player
            if check():
                print_board()
                break
            computer_row, computer_col = 0, 0
            while x[computer_row][computer_col] != ' ':
                computer_row = random.randint(0, 2)
                computer_col = random.randint(0, 2)
            x[computer_row][computer_col] = computer
            if check():
                print_board()
                break
        else:
            print("Cell already taken. Try again.")
check()