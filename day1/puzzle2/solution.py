inputFile = open("input", "r")
answer = 0
inputList = []
for x in inputFile:
  inputList.append(int(x))
for a in inputList:
  for b in inputList:
    for c in inputList:
      z = a + b + c
      if z == 2020:
        answer = a*b*c
        break
    if answer != 0:
      break
  if answer != 0:
    break
outputFile = open("output","w")
outputFile.write(str(answer))
outputFile.close()