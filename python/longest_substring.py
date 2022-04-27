def longest_substring(s):
  if len(s) == 0:
    return 0
  else:
    used_letters = set()
    for letter in s:
      if letter in used_letters:
        substrings = s.split(letter)
        max = 1
        for i in substrings:
          result = longest_substring(i) + 1
          if result > max:
            max = result
        return max
      used_letters.add(letter)
    return len(s)

print(longest_substring("abcb"))