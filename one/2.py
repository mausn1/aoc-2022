input = open('input.txt', 'r')
highest_number = 0
highest_number2 = 0
highest_number3 = 0
number = 0
for i in input:
    if i in ['\n', '\r\n']:
        if number > highest_number:
            highest_number2 = highest_number
            highest_number = number
            number = 0
        if number > highest_number2:
            highest_number3 = highest_number2
            highest_number2 = number
            number = 0
        if number > highest_number3:
            highest_number3 = number
            number = 0
        else:
            number = 0
    else:
        number += int(i)

print(highest_number)
print(highest_number2)
print(highest_number3)
print(highest_number+highest_number2+highest_number3)
