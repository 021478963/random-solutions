def sub(s, t):
  if len(t) == 0: # the empty set is a subset of all sets
    return True
  if len(s) < len(t): # if t > s then t cannot fit into s
    return False
  
  test = helper(s[:len(t)], t) # test if the next len(t) characters are t

  if test:
    return True
  else:
    return sub(s[1:], t) # check next character

def helper(s, t):
  if len(s) != len(t): # they need to be the same length (this not needed for this implementation)
    return False
  if len(s) == 0: # base case, since s is empty then all other characters were the same
    return True
  elif s[0] != t[0]: # found mismatch, strings are not the same
    return False
  else:
    return helper(s[1:], t[1:]) # call again without first character if first character is the same

#print(helper("this", "this"))
print(sub("hellothere", "."))