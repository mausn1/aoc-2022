# imports
import string
input = open("input.txt", "r")

# list
alphabeth = list(string.ascii_lowercase)+list(string.ascii_uppercase)

# test 1
# print(alphabeth.index('F')+1) # 16
# print(alphabeth.index('L')+1) # 38
# print(alphabeth.index('P')+1) # 42
# print(alphabeth.index('v')+1) # 22
# print(alphabeth.index('t')+1) # 20
# print(alphabeth.index('s')+1) # 19

# returns the amount of points of the letter


def points(letter):
    return alphabeth.index(letter)+1


def detect(row):
    compartment_one, compartment_two = row[:len(row)//2], row[len(row)//2:]
    for i in compartment_one:
        if i in compartment_two:
            return points(i)

# test 2
# print(detect("jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL"))


score = 0
for i in input.readlines():
    # Pyright Error? for whaterver reason idk
    score += detect(i)
print(score)
