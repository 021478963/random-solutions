def sort(list, number):
  while True:
    if (number > list[0] and number < list[len(list)//2]):
      if(list[len(list)//2] == number):
        return True
      else:
        list = list[0:len(list)//2]
    else:
      if(list[len(list)//2] == number):
        return True
      else:
        list = list[len(list)//2:-1]

print(sort([1, 2, 3, 4, 5], 5))