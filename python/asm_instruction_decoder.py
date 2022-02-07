from operations import binaryToDecimal
from operations import fixWidth
from operations import hexToBinary

def chooser(binaryInput):
  if len(binaryInput) == 8:
    binaryInput = hexToBinary(binaryInput)
  if len(binaryInput) != 32:
    return False
  op = binaryInput[0:2]
  if op == "00": # SETHI or Branch
    result = type1(binaryInput)
  elif op == "01": # CALL
    result = type2(binaryInput)
  elif op == "10": # Arithmetic
    result = type3(binaryInput)
  elif op == "11": # Memory
    result = type3(binaryInput)
  else:
    return False
  return result

def type1(myInput): # SETHI or Branch
  resultCode = "             00 "
  resultWords = "Branch or SETHI "
  if myInput[7:10] == "010": # branch
    resultCode += "0 " + myInput[3:7] + "    010 " + myInput[10:]
    resultWords += "  " + cond(myInput[3:7]) + "Branch disp22 value:" + fixWidth(str(binaryToDecimal(myInput[10:], 0)), 9)
  elif myInput[7:10] == "100": # sethi
    resultCode += myInput[2:7] + fixWidth("100", 6) + " " + myInput[10:]
    resultWords += fixWidth("r: " + str(binaryToDecimal(myInput[2:7], 1)), 5) + " SETHI imm22 value:" + fixWidth(str(binaryToDecimal(myInput[10:], 1)), 10)
  else:
    return False
  print(resultCode)
  print(resultWords)
  return resultCode

def cond(code):
  if code == "0001":
    return "  be "
  elif code == "0101":
    return " bcs "
  elif code == "0110":
    return "bneg "
  elif code == "0111":
    return " bvs "
  elif code == "1000":
    return "  ba "

def type2(myInput): # CALL
  resultCode = "  01 " + myInput[3:]
  resultWords = "CALL disp30 value:" + fixWidth(str(binaryToDecimal(myInput[3:], 1)), 16)
  print(resultCode)
  print(resultWords)
  return resultCode

def type3(myInput): 
  if myInput[0:2] == "10": # Arithmetic
    resultCode = "             10 "
    resultWords = "     Arithmetic "
  else: # Memory
    resultCode = "             11 "
    resultWords = "         Memory "

  resultCode += myInput[2:7] + " " + myInput[7:13] + " " + myInput[13:18]
  resultWords += fixWidth("r: " + str(binaryToDecimal(myInput[2:7], 1)), 5) + op3(myInput[7:13]) +  fixWidth("r: " + str(binaryToDecimal(myInput[13:18], 1)), 6)
  i = myInput[18]
  if i == "0":
    resultCode += " 0 00000000 " + myInput[27:]
    resultWords += " i          " + fixWidth("r: " + str(binaryToDecimal(myInput[27:], 3)), 5)
  elif i == "1":
    resultCode += " 1 " + myInput[19:]
    resultWords += " i simm13: " + fixWidth(str(binaryToDecimal(myInput[19:], 1)), 5)
  else:
    return False
  print(resultCode)
  print(resultWords)
  return resultCode

def op3(code):
  if code == "010000":
    return "  addcc"
  if code == "010001":
    return "  andcc"
  if code == "010010":
    return "   orcc"
  if code == "010110":
    return "  orncc"
  if code == "100110":
    return "    srl"
  if code == "111000":
    return "   jmpl"
  if code == "000000":
    return "     ld"
  if code == "000100":
    return "     st"
  if code == "010100":
    return "  subcc"

if __name__ == "__main__":
  myInput = ""
  while 1:
    myInput = input("Enter Binary Code:\n").lower().replace(" ", "")
    if myInput == "stop":
      break
    if not chooser(myInput):
      print("Length error, please try again.")