
def initialize_colors():
    yellow = [[3, 6, 5, 0], [2, 1, 0, 5], [1, 0, 2, 4], [0, 3, 4, 6]]
    blue = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    green = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 6]
    orange = [0, 0, 0, "2x", 0, 0, "2x", 0, "2x", 0, "3x"]
    purple = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    return{"yellow": yellow,
           "blue": blue,
           "green": green,
           "orange": orange,
           "purple": purple}


def white_as_color(color, white_instead):
    if white_instead:
        return white
    else:
        return color


def check_yellow(dice_roll, white_as_yellow,
                 yellow_new, execute):
    color = white_as_color("yellow", white_as_yellow)

    yellow_exists = []

    for column in range(0, len(yellow_new)):
        if dice_roll[color] in yellow_new[column]:
            yellow_exists.append(
                [column, yellow_new[column].index[color]])

    y_pos = len(yellow_exists)

    if execute != 0:
        if execute == 1:
            yellow_new[yellow_exists[0][0]][yellow_exists[0][1]] = 0
        if execute == 2:
            yellow_new[yellow_exists[y_pos - 1][0]][yellow_exists[y_pos - 1][1]] = 0
        return yellow_new
    else:
        return True


def check_blue(dice_roll, white_as_blue,
               blue_new, execute):

    color = white_as_color("blue", white_as_blue)

    if blue_new[dice_roll["white"]+dice_roll["blue"]-2] != 0:
        if execute == 1:
            blue_new[dice_roll["white"]+dice_roll["blue"]-2] = 0
            dice_roll[color] = 0
            return blue_new
        else:
            return True


def check_green(dice_roll, white_as_green,
                green_new, execute):
    color = white_as_color("green", white_as_green)

    green_steps = 0
    while green_new[green_steps] == 0:
        green_steps += 1

    if dice_roll[color] >= green_new[green_steps]:
        if execute == 1:
            dice_roll[color] = 0
            return green_new
        else:
            return True


def check_orange(dice_roll, white_as_orange,
                 orange_new, execute):
    color = white_as_color("orange", white_as_orange)

    orange_steps = 0
    while (orange_new[orange_steps] != 0 and
           orange_new[orange_steps] != "2x" and
           orange_new[orange_steps] != "3x"):
        orange_steps += 1

    if execute == 1:
        if orange_new[orange_steps] == "2x":
            orange_new[orange_steps] = dice_roll[color] * 2
        elif orange_new[orange_steps] == "3x":
            orange_new[orange_steps] = dice_roll[color] * 3
        else:
            orange_new[orange_steps] = dice_roll[color]
        return orange_new
    else:
        return True


def check_purple(dice_roll, white_as_purple,
                 purple_new, execute):
    color = white_as_color("purple", white_as_purple)

    purple_steps = 0
    while purple_new[purple_steps] != 0:
        purple_steps += 1

    if dice_roll[color] > purple_new[purple_steps - 1] % 6:
        if execute == 1:
            purple_new[purple_steps] = dice_roll[color]
            return purple_new
        else:
            return True


def rolling_dice(dice_roll_list, roll_no, dice_roll_new):

    dice_list = dice_roll_list[roll_no]

    color_index = 0
    for color in dice_roll.keys():
        if dice_roll_new[color] != -1:
            dice_roll_new[color] = dice_list[color_index]
        color_index += 1

    return dice_roll_new


def eliminating_dice(dice_roll_old, picked_dice, eliminated):
    for color in dice_roll_old.keys():
        if dice_roll_old[color] < dice_roll_old[picked_dice]:
            eliminated[color] = dice_roll_old[color]
            dice_roll_old[color] = -1

    return {"dice_roll_old": dice_roll_old,
            "eliminated": eliminated}


class dice:
    def __init__(self, color, execute):

class yellow_bonus:


