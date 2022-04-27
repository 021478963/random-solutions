def cherry_pickup(grid):
  paths = []

  for i in grid:
    paths.append({})

  for i in range(0, len(grid[0])):
    if grid[0][i] == -1:
      break
    else:
      paths[0][i] = [(0, i - 1)]
      if len(grid) > 1:
        if grid[1][i] != -1:
          paths[1][i] = [(0, i)]
        else:
          continue

  for i in range(1, len(grid)):
    for j in range(1, len(paths[i])):
      paths[i][j].append((i, j - 1))
      # print(paths[i][j])
      if len(grid) > i:
        if grid[i + 1][j] != -1:
          paths[i + 1][j].append((i, j))
        else:
          continue
  print(paths)

cherry_pickup([[1, 2, 3], [1, 2, 3], [1, 2, 3]])