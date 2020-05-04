import os
os.system('cls')
os.system('clear')

try:
    from colorama import init, Fore, Back, Style
    init(autoreset=True)
    color = True
except:
    print("Install the color library to better visualization.")
    print("Run the command: pip install -r requirements.txt\n")
    color = False

# Global vars Chess Grid and States, to save previous states to go back.
grid = []
states = []

"""
Test of programming knowledge for BNP. 
Goal: Place N queens in NxN grid.
Commands:
- Goback. Quit the last movement.
- Color. Switch between display types colored or black/white.
- Resolve. Take the actual state of the grid and resolve it with best-first search algorithm.
- Exit. Finish game.
"""

def main():
    global grid
    global color
    print("Choose a grid size (N x N): ")
    while True:
        try:
            size = int(input())
            break
        except ValueError:
            print("Error: The value must be a number. Try again.")

    print("Selected size is: {}".format(size))
    grid = [ [ 0 for i in range(size) ] for j in range(size) ]
    print_grid()

    print("\nCOMMANDS:")
    print("'goback' > Go back movements.")
    print("'resolve' > Take the actual state of the grid and resolve it.")
    print("'color' > Switch between display types colored or black/white.")
    print("'exit' > Finish the game.\n")

    while check_ended():  
        try:
            print("Enter new position for a queen: (LINE [ENTER] COL [ENTER])")
            n = input()   
            if n == 'goback':
                goback_movement()
                print_grid()
            elif n == 'color':
                if color:
                    color = False
                else:
                    color = True
                print_grid()
            elif n == 'resolve':
                resolve()
                break
            elif n == 'exit':
                break
            else:
                n = int(n)
                m = int(input())       

                if check_position(n, m):
                    register_movement(n, m)
                    print_grid()
                else:
                    print("{}x{} Is not a valid position, try again.".format(n,m))
        except ValueError:
            print("Error: The value of postions N and M must be a numbers, 'goback', 'color', 'resolve' or 'exit' command. Try again.")
    
    print("The game is ended! There are no more possible movements ;)")
    print_grid()

# Check user selection type to print the grid
def print_grid():
    if color == True:
        print_grid_color()
    else:
        print_grid_nocolor()

# Print the grid with color
def print_grid_color():
    for i in range(len(grid)):
        if i == 0:
            print("  ".format(i), end = '')
        print(" {} ".format(i), end = '')
    print('')
    for n in range(len(grid)):
        print("{} ".format(n), end = '')
        for m in range(len(grid[n])):
            if grid[n][m] == 0:
                print(Back.WHITE +'   ', end = '')
            elif grid[n][m] == 1:
                print(Back.BLACK + Style.BRIGHT +u' \u2655 ', end = '')
            elif grid[n][m] == 2:
                print(Back.RED +'   ', end = '')
        print('')
    print('')

# Print the grid with no colors
def print_grid_nocolor():
    clossing = '____' * len(grid)
    print(clossing)
    for n in grid:
        print('|', end = '')
        for m in n:
            if m == 0:
                print('   |', end = '')
            elif m == 1:
                print(' Q |', end = '')
            elif m == 2:
                print(' - |', end = '')

        print('\n{}'.format(clossing))
    print('')

# Resolve the grid using best-first search algorithm
def resolve():
    for n in range(len(grid)):
        for m in range(len(grid[n])):
            if check_position(n, m):
                register_movement(n, m)
                print_grid()

# Check if the grid is full
def check_ended():
    for x in grid:
        if 0 in x:
            return True
    return False

# Insert new movement in the grid with val 1
def register_movement(n, m):
    grid[n][m] = 1

# Ondo movement
def goback_movement():
    global grid
    global states
    try:
        prev_state = states.pop()
        grid = prev_state
    except:
        print("There is no movement to go back.")

# Check if the movement is valid and register blocked positions with val 2
def check_position(n, m):
    global grid
    global states
    backup = [ [ i for i in j ] for j in grid ]
    temp_grid = [ [ i for i in j ] for j in grid ]
    maxlen = len(grid)

    if n in range(0, maxlen) and m in range(0, maxlen):
        # Check in line
        if 1 in grid[n]:
            return False
        else:
            temp_grid[n] = [ 2 for i in range(maxlen) ]
        # Check in column
        for pos in range(maxlen):
            if grid[pos][m] == 1:
                return False
                break
            else:
                temp_grid[pos][m] = 2
        # Check in \ /
        for i in range(maxlen):
            if(i != n):
                left = n + m - i
                rigth = m + i - n
                
                if left in range(0, maxlen):                    
                    if grid[i][left] == 1:
                        return False
                    else:
                        temp_grid[i][left] = 2

                if rigth in range(0, maxlen):
                    if grid[i][rigth] == 1:
                        return False
                    else:
                        temp_grid[i][rigth] = 2

        # Save state to return in goback_movement function 
        states.append(backup)

        # If all is correct, then register no valid positions
        grid = temp_grid         
        return True
    else:
        return False

if __name__ == '__main__':
    main()