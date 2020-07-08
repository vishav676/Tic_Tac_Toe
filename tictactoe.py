grid = "_________"


def show_grid(string_grid):
    print('---------')
    for i in range(0, len(string_grid), 3):
        print("| " + string_grid[i] + " " + string_grid[i + 1] + " " + string_grid[i + 2] + " |")
    print('---------')


def list_to_grid(current_grid):
    s = ''
    for i in range(3):
        for j in range(3):
            s += current_grid[i][j]
    return s


def grid_list(grid_new):
    lis = []
    for s in range(0, len(grid_new), 3):
        sub_list = [grid_new[s], grid_new[s + 1], grid_new[s + 2]]
        lis.append(sub_list)
        print(sub_list)
    return lis


def horizontal_win(grid_new_list, turn):
    check_list = []
    for i in range(3):
        for j in range(3):
            if grid_new_list[i][j] != turn:
                check_list.append(False)
            else:
                check_list.append(True)
        if all(check_list):
            return True
        else:
            check_list = []
    return False


def diagonal_win(grid_new_list, turn):
    check_list = []
    check_list_second = []
    for i in range(3):
        for j in range(3):
            if i == j:
                if grid_new_list[i][j] == turn:
                    check_list.append(True)
                else:
                    check_list.append(False)

    if not all(check_list):
        print('i AM INSIDE' + turn)
        if grid_new_list[0][2] == turn and grid_new_list[1][1] == turn and grid_new_list[2][0] == turn:
            return True

    else:
        return all(check_list)
    return False


def vertical_win(grid_new_list, turn):
    check_list = []
    for i in range(3):
        for j in range(3):
            if grid_new_list[j][i] != turn:
                check_list.append(False)
            else:
                check_list.append(True)
        if not all(check_list):
            check_list = []
        else:
            return True
    return False


def check_win(current_grid, checkFor):
    if horizontal_win(current_grid, checkFor):
        return True
    elif vertical_win(current_grid, checkFor):
        return True
    elif diagonal_win(current_grid, checkFor):
        return True


def count_(current_grid, checkFor):
    count = 0
    for i in range(3):
        for j in range(3):
            if current_grid[i][j] == checkFor:
                count += 1
    return count


def analyze_input(current_grid, x, y):
    if 1 <= x <= 3 and 1 <= y <= 3:
        if current_grid[3 - y][x - 1] != "_":
            print("This cell is occupied by " + current_grid[3 - y][x - 1])
            return False
    else:
        print("Coordinates should be from 1 to 3")
        return False
    return True


show_grid(grid)
current_grid = grid_list(grid)
coord_x = 0
coord_y = 0

while True:
    your_move = input()
    try:
        coord_x = int(your_move.split(" ")[0])
        coord_y = int(your_move.split(" ")[1])
        if analyze_input(current_grid, coord_x, coord_y):
            no_of_x = count_(current_grid, "X")
            no_of_o = count_(current_grid, "O")
            if no_of_x <= no_of_o:
                current_grid[3 - coord_y][coord_x - 1] = "X"
            else:
                current_grid[3 - coord_y][coord_x - 1] = "O"
            grid = list_to_grid(current_grid)
            show_grid(list_to_grid(current_grid))
            x_win_factor = check_win(current_grid, 'X')
            o_win_factor = check_win(current_grid, 'O')
            if x_win_factor and not o_win_factor:
                print("X wins")
                break
            elif not x_win_factor and o_win_factor:
                print("O wins")
                break
            elif not x_win_factor and not o_win_factor and "_" not in grid:
                print("Draw")
                break
    except ValueError:
        print("You should enter numbers!")
