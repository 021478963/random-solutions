def longest_substring(s):
  used_letters = {}
  longest = 0
  for i, letter in enumerate(s):
    if letter in used_letters.keys():
      if i - used_letters[letter] > longest:
        longest = i - used_letters[letter]
      used_letters[letter] = i
    else:
      if i > longest:
        longest = i
      used_letters[letter] = i
    print(longest)

  return longest

print(longest_substring("pwwkew"))