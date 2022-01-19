def nameChange(old, newLast):
  return old[0:old.find(' ') + 1] + newLast

print(nameChange("allan was", "here"))