import time
import random
import collections

def cyclic_sorted_array(L, number):
  middle = len(L) // 2
  start = 0
  end = len(L) - 1
  while 1:
    if L[middle] == number:
      return True
    elif end == start:
      return False
    elif L[start] < L[middle]:
      if number < L[middle]:
        if L[start] > number:
          start = middle + 1
        else:
          end = middle
      else:
        start = middle + 1
    else:
      if number > L[end]:
        end = middle
      elif number < L[middle]:
        end = middle
      else:
        start = middle + 1
    middle = start + ((end - start) >> 1)

if __name__ == "__main__":
  set1 = []
  n = 200000000
  for i in range(n):
    set1.append(i)
  my_list = collections.deque(set1)
  my_list.rotate(random.randrange(n))
  set1 = list(my_list)
  number = random.randrange(2 * n)
  start_time = time.time()
  # print(set1)
  print(number)
  print(cyclic_sorted_array(set1, number))
  print("time elapsed: " + str(time.time() - start_time))