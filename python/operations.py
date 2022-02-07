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

if __name__ == "__main__":
  temp = input("select\n")
  temp = temp.strip().lower()
  myInput = input("input\n")
  if temp == "dtb":
    while 1:
      print(decimalToBinary(myInput, 32))
      myInput = input("input\n")
  elif temp == "btd":
    while 1:
      print(binaryToDecimal(myInput))
      myInput = input("input\n")
  elif temp == "htb":
    while 1:
      print(hexToBinary(myInput))
      myInput = input("input\n")