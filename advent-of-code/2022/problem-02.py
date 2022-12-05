from helpers import get_lines
import math

def score_move(move):
    if move == "X":
        return 1
    if move == "Y":
        return 2
    if move == "Z":
        return 3
    raise f"Invalid input to score_move of ::{move}::"

def score_game(opponent_move, my_move):
    ''' 0 for lose, 3 for tie, 6 for win
    '''
    convert_table = {"X":"A", "Y":"B", "Z":"C"}
    if opponent_move == convert_table[my_move]:
        return 3
    if opponent_move == "A": # rock, then I win only if I did paper
        return 6 if my_move == "Y" else 0
    if opponent_move == "B": # paper, then I win only if I did scissors
        return 6 if my_move == "Z" else 0
    if opponent_move == "C": # scissors, then I win only if I did rock
        return 6 if my_move == "X" else 0

def solve1(data):
    total_count = 0
    for line in data:
        opponent_move, my_move = line.split(" ")
        win_lose_points = score_game(opponent_move, my_move)
        my_move_points = score_move(my_move)
        total_count += win_lose_points + my_move_points
        print(f"{win_lose_points} + {my_move_points} = {win_lose_points + my_move_points}")
    print(f"total: {total_count}")

def score_outcome(my_outcome):
    if my_outcome == "X": 
        return 0
    if my_outcome == "Y":
        return 3
    if my_outcome == "Z":
        return 6
    raise "Invalid input to score_outcome ::{my_outcome}::"

def get_move(opponent_move, my_outcome):
    if my_outcome == "Y":
        convert_table = {"A":"X", "B": "Y", "C":"Z"}
    elif my_outcome == "X": # I need to lose. rock goes to scissors, paper goes to rock, scissors goes to paper
        convert_table = {"A": "Z", "B":"X", "C":"Y"}
    elif my_outcome == "Z": # I need to win. rock goes to paper, paper goes to scissors, scissors goes to rock
        convert_table = {"A":"Y","B":"Z","C":"X"}
    else:
        raise "Invalid input to get_move ::{my_outcome}::"
    return convert_table[opponent_move]


def solve2(data):
    total_count = 0
    for line in data:
        opponent_move, my_outcome = line.split(" ")
        my_move = get_move(opponent_move, my_outcome)
        my_move_points = score_move(my_move)
        outcome_points = score_outcome(my_outcome)
        print(f"{my_move_points} + {outcome_points} = {outcome_points + my_move_points}")
        total_count += outcome_points + my_move_points

    print(f"total: {total_count}")

test_data = '''
A Y
B X
C Z
'''

# data = test_data.strip().split("\n")
data = get_lines("input-02.txt")

solve2(data)