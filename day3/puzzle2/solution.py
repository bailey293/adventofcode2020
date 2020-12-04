inputFile = open("input", "r")
inputList = []

for x in inputFile:
  inputList.append(x)
inputFile.close()

lineLen = len(inputList[0])-1
counters = []

currentPos = 0
counter = 0
for x in inputList:
  if x[currentPos] == '#':
    counter+=1
  currentPos = (currentPos + 1)%lineLen
counters.append(counter)

counter = 0
currentPos = 0
for x in inputList:
  if x[currentPos] == '#':
    counter+=1
  currentPos = (currentPos + 3)%lineLen
counters.append(counter)

counter = 0
currentPos = 0
for x in inputList:
  if x[currentPos] == '#':
    counter+=1
  currentPos = (currentPos + 5)%lineLen
counters.append(counter)

counter = 0
currentPos = 0
for x in inputList:
  if x[currentPos] == '#':
    counter+=1
  currentPos = (currentPos + 7)%lineLen
counters.append(counter)

counter = 0
currentPos = 0
lineCount = 0
for x in inputList:
  if (lineCount % 2) == 0:
    if x[currentPos] == '#':
      counter+=1
    currentPos = (currentPos + 1)%lineLen
  lineCount+=1
counters.append(counter)

answer = counters[0]*counters[1]*counters[2]*counters[3]*counters[4]

outputFile = open("output","w")
outputFile.write(str(answer))
outputFile.close()