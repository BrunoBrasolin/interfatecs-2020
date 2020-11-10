import sys

namesArray = sys.stdin.readlines()
newArray = []
for name in namesArray:
    nameToArray = name.split()

    i = 1
    while i < (len(nameToArray) - 1):
        nameToArray[i] = nameToArray[i][0] + '.'
        i+=1
    newArray.append(nameToArray)

for names in sorted(newArray):
    print(*names)