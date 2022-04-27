def longest_substring(s):
  used_letters = set()
  start = 0
  longest = 0
  for i, letter in enumerate(s):
    if letter in used_letters:
      if i - start > longest:
        longest = i - start
      used_letters = set()
      start = i
    used_letters.add(letter)

  last = len(s) - start
  if last > longest:
    return last
  return longest

print(longest_substring("dvdf"))