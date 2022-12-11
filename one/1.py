input = open('input.txt', 'r')
highest_number = 0
number = 0
for i in input:
    if i == "\n":
        if number > highest_number:
            highest_number = number
            number = 0
        else:
            number = 0
    else:
        number += int(i)

print(highest_number)
