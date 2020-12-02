inputFile = open("input", "r")
answer = 0
inputList = []
for x in inputFile:
  inputList.append(int(x))
for x in inputList:
  for y in inputList:
    z = x + y
    if z == 2020:
      answer = x*y
      break
  if answer != 0:
    break
outputFile = open("output","w")
outputFile.write(str(answer))
outputFile.close()