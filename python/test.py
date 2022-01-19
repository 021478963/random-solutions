def swap(s, one, two):
  return s[0:one] + s[two] + s[one + 1:two] + s[one] + s[two + 1:]

if __name__ == "__main__":
  print(swap("ab", 0, 1))
  print(swap("banana", 2, 5))