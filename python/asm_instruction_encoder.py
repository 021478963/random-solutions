from operations import decimalToBinary
# from operations import binaryToHex

def encoder():
  result = input("op\n").lower().strip()[0]

  if result == "s": # find op
    result = "00 " + "100 "
  elif result == "b":
    result = "00 " + "010 "
  elif result == "c":
    result = "01 "
  elif result == "a":
    result = "10 "
  elif result == "m":
    result = "11 "
  else:
    return "Error"
  
  if result[:2] != '00' and result[:2] != '01': # not SETHI and Branch
    temp = input("Destination Directory (0 - 31)\n")
    result += decimalToBinary(temp, 5)
  elif result[:2] == "01":
    temp = input("disp30\n")
    result += decimalToBinary(temp, 30)
    print(result)
    return result.replace(" ", "")
  elif result[3:6] == '010': # Branch
    temp = input().lower().strip()[1]
    if temp == "e":
      result = insert(result, " 00001", 2)
    elif temp == "c":
      result = insert(result, " 00101", 2)
    elif temp == "n":
      result = insert(result, " 00110", 2)
    elif temp == "v":
      result = insert(result, " 00111", 2)
    elif temp == "a":
      result = insert(result, " 01000", 2)
    else:
      return "Error"
  elif result[3:6] == '100': # SETHI
    temp = input("Destination Directory\n")
    result = insert(result, " " + decimalToBinary(temp, 5), 2)

  if result[9:12] == '100': # SETHI imm22, Branch disp22
    temp = input("SETHI imm22\n")
    result += decimalToBinary(temp, 22)
    print(result)
    return result.replace(" ", "")
  elif result[9:12] == '010':
    temp = input("disp22\n")
    result += decimalToBinary(temp, 22)
    print(result)
    return result.replace(" ", "")

  if result[0:2] == "10": # Arithmetic op3
    temp = input("op3 Arithmetic\n")
    if temp == "addcc":
      result += " 010000"
    elif temp == "andcc":
      result += " 010001"
    elif temp == "orcc":
      result += " 010010"
    elif temp == "orncc":
      result += " 010110"
    elif temp == "srl":
      result += " 100110"
    elif temp == "jmpl":
      result += " 111000"
    elif temp == "subcc":
      result += " 010100"
    else:
      return "Error"
  elif result[0:2] == "11": # Memory op3
    temp = input("op3 Memory\n") 
    if temp == "ld":
      result += "000000"
    elif temp == "st":
      result += "000100"
    else:
      return "Error"
  
  temp = input("rs1\n")
  result += " " + decimalToBinary(temp, 5)
  temp = input("i\n")
  result += " " + temp

  if temp == "0":
    result += "00000000"
    temp = input("rs2\n")
    result += " " + decimalToBinary(temp, 5)
  elif temp == "1":
    temp = input("simm13\n")
    result += decimalToBinary(temp, 13)

  print(result)
  #if mode == 0:
  return result.replace(" ", "")
  #else:
  #  return binaryToHex(result)
    
def insert(originalString, newString, index):
  return originalString[:index] + newString + originalString[index:]

if __name__ == "__main__":
  print(encoder())