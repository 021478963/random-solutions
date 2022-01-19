from typing import final


def userid(first, middle, last):
  final = first[0]
  if len(middle) > 0:
    final += middle[0]
  final += last[0:8 - len(final)]
  return final

print(userid("allan", "", "3456789"))