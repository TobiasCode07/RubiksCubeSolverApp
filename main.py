# MAKE SURE TO HOLD THE CUBE IN THE SAME ORIENTATION AS SHOWN

from rubik_solver import utils
from tkinter import *

cube = ['y', 'y', 'y', 'y', 'y', 'y', 'y', 'y', 'y', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'r', 'r', 'r', 'r',
        'r', 'r', 'r', 'r', 'r', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o',
        'o', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w']
solved_cube = "yyyyyyyyybbbbbbbbbrrrrrrrrrgggggggggooooooooowwwwwwwww"
current_side = 2
sides = ["b", "y", "g", "w"]  # Left, Up, Right, Down
cube_colors = ["y", "w", "g", "b", "r", "o"]
selected_btn = None

def reset():
    global cube, solved_cube, current_side, sides, cube_colors, selected_btn

    cube = ['y', 'y', 'y', 'y', 'y', 'y', 'y', 'y', 'y', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'r', 'r', 'r', 'r',
            'r', 'r', 'r', 'r', 'r', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o',
            'o', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w']
    solved_cube = "yyyyyyyyybbbbbbbbbrrrrrrrrrgggggggggooooooooowwwwwwwww"
    current_side = 2
    sides = ["b", "y", "g", "w"] # Left, Up, Right, Down
    cube_colors = ["y", "w", "g", "b", "r", "o"]

    select_btn(chng_btns[0])

    count = 0
    for i in range(len(btns)):
        for j in range(len(btns[i])):
            btns[i][j].config(bg=colors[cube[current_side * 9 + count]])
            count += 1

    for a in range(len(side_btns)):
        side_btns[a].config(bg=colors[sides[a]])

    solution_entry.config(state=NORMAL)
    solution_entry.delete(0, END)
    solution_entry.config(state=DISABLED)

other_side = {
    "y":"w",
    "r":"o",
    "g":"b",
    "w":"y",
    "o":"r",
    "b":"g"
}

colors = {
    "y":"yellow",
    "b":"blue",
    "r":"red",
    "g":"green",
    "o":"orange",
    "w":"white"
}

btns = []
btns_pos = []
side_btns = []
chng_btns = []
cube_width = 40
cube_height = 30

def change_color(i, j):
    side = cube[current_side * 9:current_side * 9 + 9]
    side_list = []
    count = 0
    for a in range(3):
        side_list.append([])
        for b in range(3):
            side_list[a].append(side[count])
            count += 1

    side_list[i][j] = cube_colors[chng_btns.index(selected_btn)]
    count2 = 0
    for x in range(3):
        for y in range(3):
            side[count2] = side_list[x][y]
            count2 += 1

    count3 = 0
    for c in range(len(cube)):
        if current_side * 9 <= c < current_side * 9 + 9:
            cube[c] = side[count3]
            count3 += 1

    btns[i][j].config(bg=colors[cube_colors[chng_btns.index(selected_btn)]])

def draw_btns():
    global cube, current_side, btns

    count = 0
    for i in range(len(btns)):
        for j in range(len(btns[i])):
            btns[i][j].grid(row=btns_pos[count][0], column=btns_pos[count][1])
            count += 1

def create_btns():
    count = 0
    for i in range(3):
        btns.append([])
        for j in range(3):
            if i == 1 and j == 1:
                btns[i].append(Button(root, bg=colors[cube[current_side * 9:current_side * 9 + 9][4]], padx=cube_width,
                                      pady=cube_height, state=DISABLED))
            else:
                btns[i].append(Button(root, bg=colors[cube[current_side * 9:current_side * 9 + 9][4]],
                                      padx=cube_width, pady=cube_height, command=lambda i=i, j=j:change_color(i, j)))

            btns_pos.append((i + 1, j + 1))
            count += 1

def change_side(color):
    global current_side

    previous_color = cube[current_side * 9:current_side * 9 + 9][4]

    to_change = None
    for i in range(6):
        chance = cube[i * 9:i * 9 + 9][4]
        if color == chance:
            to_change = i
            break

    current_side = to_change
    side = cube[current_side * 9:current_side * 9 + 9]

    count = 0
    for a in range(len(btns)):
        for b in range(len(btns[a])):
            btns[a][b].config(bg=colors[side[count]])
            count += 1

    side_index = sides.index(color)
    if side_index % 2 == 0:
        other_index = 0 if side_index == 2 else 2
    else:
        other_index = 1 if side_index == 3 else 3

    sides[side_index] = other_side[previous_color]
    sides[other_index] = previous_color

    for x in range(len(side_btns)):
        side_btns[x].config(bg=colors[sides[x]])

def create_side_btns():
    for i in range(4):
        side_btns.append(Button(root, bg=colors[sides[i]], padx=cube_width, pady=cube_height, command=lambda i=i: change_side(sides[i])))

def draw_side_btns():
    pos = [(2, 0), (0, 2), (2, 4), (4, 2)]
    for i in range(len(side_btns)):
        side_btns[i].grid(row=pos[i][0], column=pos[i][1], pady=10 if i == 1 or i == 3 else 0, padx=10 if i == 0 or i == 2 else 0) # Left, Up, Right, Down

def select_btn(new_btn):
    global selected_btn

    if selected_btn:
        selected_btn.config(border=2)

    new_btn.config(border=5)
    selected_btn = new_btn

def create_chng_btns():
    global selected_btn

    for i in range(6):
        chng_btns.append(Button(root, bg=colors[cube_colors[i]], padx=20, pady=15, command=lambda i=i: select_btn(chng_btns[i])))

    select_btn(chng_btns[0])

def draw_chng_btns():
    count = 0
    for i in range(3):
        for j in range(2):
            chng_btns[count].grid(row=i + 1, column=j + 6)
            count += 1

def solve():
    global current_side, sides

    cube_str = ""
    for i in cube:
        cube_str += i

    sides = ["b", "y", "g", "w"]  # Left, Up, Right, Down
    current_side = 2
    count = 0
    for i in range(len(btns)):
        for j in range(len(btns[i])):
            btns[i][j].config(bg=colors[cube[current_side * 9 + count]])
            count += 1

    for a in range(len(side_btns)):
        side_btns[a].config(bg=colors[sides[a]])

    if cube_str == solved_cube:
        solution = "The cube is already solved"
    else:
        try:
            solution = utils.solve(cube_str, "Kociemba")
        except:
            solution = "Invalid cube orientation"

    solution_entry.config(state=NORMAL)
    solution_entry.delete(0, END)
    solution_entry.insert(0, solution)
    solution_entry.config(state=DISABLED)

root = Tk()
root.title("Rubik's Cube Solver")
root.geometry("730x550")
root.iconbitmap("rubik.ico")
root.resizable(False, False)

if not btns:
    create_btns()

if not side_btns:
    create_side_btns()

if not chng_btns:
    create_chng_btns()

draw_side_btns()
draw_btns()
draw_chng_btns()

empty_label = Label(root)
empty_label.grid(row=0, column=5, padx=30)

color_label = Label(root, text="Pick a color:", font=("Arial", 15))
color_label.grid(row=0, column=6, columnspan=2)

solution_label = Label(root, text="Solution:", font=("Arial", 15))
solution_label.grid(row=5, column=0, pady=20)

solution_entry = Entry(root, state=DISABLED, font=("Arial", 15), width=55)
solution_entry.place(x=100, y=482)

reset_btn = Button(root, text="Reset", font=("Arial", 15), padx=20, pady=10, command=reset)
reset_btn.place(x=430, y=385)

solve_btn = Button(root, text="Solve", font=("Arial", 15), padx=20, pady=10, command=solve)
solve_btn.place(x=580, y=385)

root.mainloop()