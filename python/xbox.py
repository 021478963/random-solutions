def xbox(n):
  printline(n + 2)
  myPrint(n, 0, 0)
  printline(n + 2)
  return None

def printline(n):
  if n == 0:
    print()
    return None
  else:
    print("#", end = "")
    printline(n - 1)

def myPrint(n, currentY, currentX):
  if currentY == n:
    return False
  if currentX == 0:
    print("#", end = "")

  if currentY == currentX or n - currentY - 1 == currentX:
    print('x', end = "")
  else:
    print(" ", end ="")
    
  if currentX == n - 1:
    print("#")
    myPrint(n, currentY + 1, 0)
  elif currentX < n:
    myPrint(n, currentY, currentX + 1)

xbox(5)
xbox(10)