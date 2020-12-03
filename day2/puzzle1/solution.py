inputFile = open("input", "r")
answer = 0
leastNumList = []
mostNumList = []
charList = []
passList = []

for x in inputFile:
  y = x.split()
  a = y[0].split("-")
  leastNumList.append(int(a[0]))
  mostNumList.append(int(a[1]))
  charList.append(y[1].strip(":"))
  passList.append(y[2])
  
for password in passList:
  i = passList.index(password)
  leastNum = leastNumList[i]
  mostNum = mostNumList[i]
  char = charList[i]
  
  charCount = password.count(char)
  
  if leastNum <= charCount and charCount <= mostNum:
    answer +=1

outputFile = open("output","w")
outputFile.write(str(answer))
outputFile.close()