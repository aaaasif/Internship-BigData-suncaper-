tryList = ["First", "Second", "Third", "Fourth", "Fifth"]
listLength = len(tryList) - 1

# Method 01
while listLength>=0:
    print(tryList[listLength])
    listLength -= 1

# Method 02
for i in range(listLength, -1, -1):
    print(tryList[i])