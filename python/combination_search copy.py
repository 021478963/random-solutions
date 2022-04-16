def starter(candidates, target):
  results = []
  for i in range(len(candidates), 0, -1):
    # print(candidates[:i])
    result = search(candidates[:i], target)
    if len(result) > 0:
      results += result
    print(results)
  return results

def search(candidates, target):
  if target < candidates[0]:
    return None

  n = 1
  valid_combinations = []
  while n * candidates[-1] <= target:
    if target % (n * candidates[-1]) ==  0:
      valid_combinations.append([candidates[-1]] * n)
    else:
      temp = search(candidates, target - n * candidates[-1])
      if temp is not None:
        for i in temp:
          valid_combinations.append([candidates[-1]] * n + i)
    n += 1
    
  return valid_combinations

# print(starter([3, 2, 1], 3))
starter([1, 2, 3], 3)