print('''
============================================================================
                 WELCOME TO TIC TAC PYTHON WORLD CHAMPION
============================================================================
''')

print("Let's start the game!")
print("Watch carefully this table, each number represent a position on the game.")
print(f'''
            ===============
            | 1 || 2 || 3 |
            | 4 || 5 || 6 |
            | 7 || 8 || 9 |
            ===============
            ''')
on_game = True
rounds = 0

table_logic = [[0,0,0], [0,0,0], [0,0,0]]
table_draw = [["[1]", "[2]", "[3]"], ["[4]", "[5]", "[6]"], ["[7]", "[8]", "[9]"]]

# Helper function to check the user answer and avoid error
def check_input(i):
    while not isinstance(i, int):
        try:
            i = int(i)
        except:
            i = input("Input must be a number: ")

    while i < 1 or i > 9:
        i = check_input(input("You have to choose a value between 1 and 9: "))

    return i

# Helper function to calculate the position on the grid
def calculate_pos(p):
    if 1 <= p <= 3: return [0, p-1]
    elif 4 <= p <= 6: return [1, p-4]
    else: return [2, p-7]

# Helper function to write the user input
def write_input(p, n):
    if n == 1: sym = " X "
    elif n == 2: sym = " O "

    v = calculate_pos(p)
    while table_logic[v[0]][v[1]] != 0:
         v = calculate_pos(check_input(input("Position already taken. Choose a position between 1 and 9: ")))

    table_logic[v[0]][v[1]] = n
    table_draw[v[0]][v[1]] = sym

# Helper function to execute victory
def execute_victory(pn):
    print(f"Congratulations to player {pn}! You won :D")
    return False

def check_victory(pn):
    y = 0 # Check horizontal lines

    # Check if game is out of rounds
    if rounds == 9:
        print("No one won, don't worry be happy :)")
        return False

    while y <= 2:
        if table_logic[y][0] == pn and table_logic[y][1] == pn and table_logic[y][2] == pn: return execute_victory(pn)
        y += 1

    x = 0 # Check vertical lines
    while x <= 2:
        if table_logic[0][x] == pn and table_logic[1][x] == pn and table_logic[2][x] == pn: return execute_victory(pn)
        x += 1

    # Check diagonals
    if table_logic[0][0] == pn and table_logic[1][1] == pn and table_logic[2][2] == pn: return execute_victory(pn)
    elif table_logic[0][2] == pn and table_logic[1][1] == pn and table_logic[2][0] == pn: return execute_victory(pn)

    # The game continues
    return True

# Main while that executes while no player have win
while on_game:
    player_num = 1
    while player_num <= 2 and on_game:
        p = check_input(input(f"Player {player_num} place your mark: ") or -1)
        rounds += 1
        write_input(p, player_num)
        print(f'''
            ===============
            |{table_draw[0][0]}||{table_draw[0][1]}||{table_draw[0][2]}|
            |{table_draw[1][0]}||{table_draw[1][1]}||{table_draw[1][2]}|
            |{table_draw[2][0]}||{table_draw[2][1]}||{table_draw[2][2]}|
            ===============
            ''')
        on_game = check_victory(player_num)
        player_num += 1
