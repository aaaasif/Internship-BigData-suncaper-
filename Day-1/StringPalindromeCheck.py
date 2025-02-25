myString = "fisalahalludba"
newString = ""

strLength = len(myString)
while strLength > 0:
    newString += myString[strLength-1]
    strLength -= 1

if myString == newString:
    print("Palindrom")
else: print("Not Palindrom")

print(myString)
print(newString)