# In how many assignment pairs does one range fully contain the other?
# use range(starting,ending) if all in next then add to variable? 
input = open("input.txt","r")
input = input.read().split()
counter=0
for i in input:
    r = i.replace(",","-").split("-")
    print(r,r[0],r[1],r[2],r[3])
    if (int(r[0]) >= int(r[2]) and int(r[3]) >= int(r[1])) or (int(r[0]) <= int(r[2]) and int(r[3]) <= int(r[1])):
        print("True")
        counter+=1
print(counter)
