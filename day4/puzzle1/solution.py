inputFile = open("input", "r")
answer=0
y=[]

for x in inputFile:
  splitX = x.split()
  for z in splitX:
    splitZ = z.split(':')
    y.append(splitZ[0])
  if x == '\n':
    if (len(y) == 7 and y.count('cid') == 0) or len(y) == 8:
      answer+=1
    y = []
if (len(y) == 7 and y.count('cid') == 0) or len(y) == 8:
  answer+=1
  
inputFile.close()
outputFile = open("output","w")
outputFile.write(str(answer))
outputFile.close()