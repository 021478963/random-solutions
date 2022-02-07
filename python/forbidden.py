def forbidden_characters(L, forbidden, depth = 0):
  if len(L) == depth:
    return 0
  else:
    if check(L[depth], forbidden):
      L[depth] = ""
      return 1 + forbidden_characters(L, forbidden, depth + 1)
    return forbidden_characters(L, forbidden, depth + 1)

def check(word, forbidden, depth = 0):
  if len(word) == depth:
    return False
  else:
    return checkHorizontal(word[depth], forbidden) or check(word, forbidden, depth + 1)

def checkHorizontal(letter, forbidden, depth = 0):
  if len(forbidden) == depth:
    return False
  else:
    return letter == forbidden[depth] or checkHorizontal(letter, forbidden, depth + 1)

L = ["hater"]
print(forbidden_characters(L, "!@#$!!!"))

L = ["happy", "sad", "simple", ""]
print(forbidden_characters(L, "abc"))
print(L)