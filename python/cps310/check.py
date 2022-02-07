from asm_instruction_decoder import chooser

def check(textFile, binFile):
  textInstructions = getTextFile(textFile)
  binInstructions = getBinFile(binFile)

  smallest = len(textInstructions) if textInstructions < binInstructions else len(binInstructions)

  for i in range(smallest):
    print("file:")
    x = chooser(textInstructions[i])
    print("bin: ")
    y = chooser(binInstructions[i])
    assert x == y
    print("ok\n\n")

def getTextFile(fileName):
  result = []
  with open(fileName, 'r') as file:
    for line in file:
      line = line.replace(' ', '').replace('\n', '')
      if line != "\n" and (len(line) == 32 or len(line) == 8):
        result.append(line)
  return result

def getBinFile(fileName):
  result = []
  with open(fileName, 'r') as file:
    for line in file:
      if '\t' in line:
        result.append(line[9:17])
  return result

textPath = input("text name\n")
binPath = input("bin name\n")
print()
check(textPath, binPath)
input("Press Enter to continue...")