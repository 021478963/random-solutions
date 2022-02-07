def equivalence_classes(L):
  result = []
  format(iterable(L, result))
  result.sort()
  return result

def iterable(L, result, depth = 0):
  if len(L) == depth:
    return result
  else:
    sort(result, L[depth], letterCount(L[depth]))
    return iterable(L, result, depth + 1)

def sort(result, word, length, depth = 0):
  if len(result) == depth:
    result.append([length, word])
    return True
  elif result[depth][0] == length:
    result[depth].append(word)
    return True
  else:
    return sort(result, word, length, depth + 1)

def letterCount(word, depth = 0):
  if len(word) == depth:
    return 0
  else:
    if word[depth] == 'a' or word[depth] == 'e' or word[depth] == 'i' or word[depth] == 'o' or word[depth] == 'u':
      return 1 + letterCount(word, depth + 1)
    return letterCount(word, depth + 1)

def format(result, depth = 0):
  if len(result) == depth:
    return True
  else:
    result[depth].pop(0)
    result[depth].sort()
    return format(result, depth + 1)

L = ["coop", "meats", "slant", "a", "ab", "baa"]
print(equivalence_classes(L))

L = ["craft"]
print(equivalence_classes(L))