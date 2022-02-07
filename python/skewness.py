from math import sqrt

# skewness
def skewness(l):
  myL = l[:]
  m = mean(myL)
  myL = l[:]
  myL.sort()
  med = median(myL)
  myL = l[:]
  sD = standardDeviation(myL, m)
  return 3 * (m - med) / sqrt(sD / len(l))

# mean
def mean(l, sum = 0, depth = 0):
  if len(l) == 0 and depth == 0:
    return 0
  elif len(l) == 0:
    return sum / depth
  else:
    sum += l.pop()
    return mean(l, sum, depth + 1)

# median
def median(l):
  if len(l) >= 3:
    l.pop(0)
    l.pop()
    return median(l)
  elif len(l) == 2:
    return (l[0] + l[1]) / 2
  elif len(l) == 1:
    return l[0]
  else:
    return 0

# standard deviation
def standardDeviation(l, mean, depth = 0):
  if len(l) == depth:
    return 0
  else:
    return (l[depth] - mean) ** 2 + standardDeviation(l, mean, depth + 1)

l = [5, 4, 3, 4, 5]
print(skewness(l))
l = [-94226, 94226]
print(skewness(l))