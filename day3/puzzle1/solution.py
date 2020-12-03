def positionCheck(positionToCheck, lineLen):
  returnNum = positionToCheck
  if positionToCheck >= lineLen:
    returnNum = positionToCheck - lineLen
  return returnNum
    
inputFile = open("input", "r")
answer = 0
currentPos = 0
inputList = []

for x in inputFile:
  inputList.append(x)
inputFile.close()

lineLen = len(inputList[0])-1
for x in inputList:
  if x[currentPos] == '#':
    answer+=1
  currentPos = positionCheck(currentPos + 3, lineLen)
  
outputFile = open("output","w")
outputFile.write(str(answer))
outputFile.close()