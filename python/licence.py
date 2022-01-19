def ask(n):
  if n == 5:
    return None
  else:
    n += 1
    plate = input("please enter a valid Ontario licence plate:\n")
    if not test(plate, 0):
      print("Invalid licence plate.")
      plate = ask(n)
    return plate

def test(plate, digit):
  if len(plate) != 8:
    return False
  if digit == 8:
    return True

  if digit < 4:
    if not ('A' <= plate[digit] <= 'Z'):
      return False
  elif digit == 4:
    if plate[digit] != '*':
      return False
  else:
    if not ('0' <= plate[digit] <= '9'):
      return False
  return test(plate, digit + 1)

def licence_plate():
  plate = ask(0)
  result = (ord(plate[0]) - 64) * 1000 ** 4 + (ord(plate[1]) - 64) * 1000 ** 3 + (ord(plate[2]) - 64) * 1000 ** 2 + (ord(plate[3]) - 64) * 1000 + int(plate[5:8]) 
  return result

print(licence_plate())
#for i in range(8):
  #print(test("ABCD*123", i))
#print(test("ABCD*10", 0))