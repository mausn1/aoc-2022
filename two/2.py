moves = {"A": "rock", "B": "paper", "C": "scissors",
         "X": "rock", "Y": "paper", "Z": "scissors"}
winning_moves = {"rock": ["scissors"],
                 "paper": ["rock"], "scissors": ["paper"]}


def points(moves1, moves2):
    if moves[moves1] == moves[moves2]:
        return 3+list(winning_moves.keys()).index(moves[moves1])+1
    if winning_moves[moves[moves1]][0] == moves[moves2]:
        return 6+list(winning_moves.keys()).index(moves[moves1])+1
    return 0+list(winning_moves.keys()).index(moves[moves1])+1


input = open("input.txt", "r")
total = 0

for i in input.readlines():
    a = i[2]
    b = i[0]
    total += points(a, b)

print(total)
