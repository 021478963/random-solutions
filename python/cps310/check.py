'''
  Takes in two filenames to two txt/bin files and compares them.
  Stops at the end of the smaller file
'''

from asm_instruction_decoder import chooser

def check():
  input1 = input("file 1 name:\n")
  if input1[-4:] == ".bin":
    instructions1 = getBinFile(input1)
  else:
    instructions1 = getTextFile(input1)
  input2 = input("file 2 name:\n")
  if input2[-4:] == ".bin":
    instructions2 = getBinFile(input2)
  else:
    instructions2 = getTextFile(input2)

  smallest = len(instructions1) if instructions1 < instructions2 else len(instructions2)

  for i in range(smallest):
    print("file:")
    x = chooser(instructions1[i])
    print("bin: ")
    y = chooser(instructions2[i])
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

if __name__ == "__main__":
  check()