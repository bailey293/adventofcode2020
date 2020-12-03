inputFile = open("input", "r")
answer = 0
firstNumList = []
secondNumList = []
charList = []
passList = []

for x in inputFile:
  y = x.split()
  a = y[0].split("-")
  firstNumList.append(int(a[0]))
  secondNumList.append(int(a[1]))
  charList.append(y[1].strip(":"))
  passList.append(y[2])
  
for password in passList:
  i = passList.index(password)
  char = charList[i]
  
  if password.count(char) == 0:
    continue
  charOne = password[firstNumList[i]-1]
  charTwo = password[secondNumList[i]-1]
  
  if (charOne == char and charTwo != char) or (charOne != char and charTwo == char):
    answer +=1

outputFile = open("output","w")
outputFile.write(str(answer))
outputFile.close()