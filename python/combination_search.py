def starter(candidates, target):
    results = []
    for i in range(len(candidates), 0, -1):
        result = search(candidates[:i], target)
        if result is not None and len(result) > 0:
            results += result
    return results

def search(candidates, target):
    # if candidates[-1] == 1:
    #     return [[1] * target]
    if target < candidates[0]:
        return None

    n = 1
    valid_combinations = []
    while n * candidates[-1] <= target:
        if target / (n * candidates[-1]) == 1:
            valid_combinations.append([candidates[-1]] * n)
        else:
            for i in range(len(candidates) - 1, 0, -1):
                temp = search(candidates[:i], target - n * candidates[-1])
                if temp is not None:
                    for i in temp:
                        valid_combinations.append([candidates[-1]] * n + i)
        n += 1
        
    return valid_combinations

candidates = [3, 4, 7, 8]
target = 11
print(starter(candidates, target))