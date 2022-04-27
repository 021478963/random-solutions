def checkValidString(s):
  safety = 0
  stack = []

  for c in s:
    if c == '(':
      stack.append(c)
    elif c == ')':
      if len(stack) > 0 and stack[-1] == '(':
        stack.pop()
      elif safety > 0:
        safety -=1
      else:
        return False
    else:
      safety += 1

  return True

print(checkValidString("((((()(()()()*()(((((*)()*(**(())))))(())()())(((())())())))))))(((((())*)))()))(()((*()*(*)))(*)()"))