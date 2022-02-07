def decimalToBinary(decimalInput, length = 32):
  value = int(decimalInput)
  result = ""
  while value != 0:
    remainder = value % 2
    value = value // 2
    result = str(remainder) + result

  if len(result) < length:
    result = "0" * (length - len(result)) + result
  elif len(result) > length:
    result = result[len(result) - length:]
  return result

def twosComp(binary):
  result = ""
  for i in binary:
    if i == '0':
      result += '1'
    elif i == '1':
      result += '0'
    else:
      return "error"
  return result

def twosCompHelper(binary, result, depth):
  if depth == -1:
    return result
  elif binary[depth] == '0':
    result += '1'
    result

def binaryToDecimal(binaryInput, mode = 0, length = 32):
  total = 0
  if mode == 1:
    binaryInput = "0" + binaryInput
  if len(binaryInput) < length + mode:
    if binaryInput[0] == '0':
      binaryInput = "0" * (length + mode - len(binaryInput)) + binaryInput
    else:
      binaryInput = "1" * (length + mode - len(binaryInput)) + binaryInput
      total = - (2 ** (length + mode - 1))

  for i in range(length + mode - 1, 0, -1):
    total += int(binaryInput[i]) * 2 ** (length + mode - i - 1)
  return total

def fixWidth(result, length = 10):
  if len(result) < length:
    return " " * (length - len(result)) + result
  else:
    return result

def hexToBinary(hexInput):
  hexInput = hexInput.lower()
  result = ""
  for i in hexInput:
    if "0" <= i <= "9":
      result += decimalToBinary(i, 4)
    elif "a" <= i <= "f":
      i = str(ord(i) - ord("a") + 10)
      result += decimalToBinary(i, 4)
  return result

def hexToDecimal(hexInput):
  return binaryToDecimal(hexToBinary(hexInput))
if __name__ == "__main__":
  #print(twosComp("101010"))
  
  temp = input("select\n")
  temp = temp.strip().lower()
  myInput = input("input\n")
  if temp == "dtb":
    while 1:
      temp1 = input("bits\n")
      print(decimalToBinary(myInput, int(temp1)))
      myInput = input("input\n")
  elif temp == "btd":
    while 1:
      print(binaryToDecimal(myInput))
      myInput = input("input\n")
  elif temp == "htb":
    while 1:
      print(hexToBinary(myInput))
      myInput = input("input\n")
  elif temp == "htd":
    while 1:
      print(hexToDecimal(myInput))
      myInput = input("input\n")