def analyzeStr(s):
  spaceInS = s.count(' ')
  print("contains", len(s) - spaceInS, "characters,", spaceInS, "spaces, and ends with", s[-1])

analyzeStr("hello     !")