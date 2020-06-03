import pytest

# Problem
# Given an integer array, output all the unique pairs that sum up to a specific value K
# includes negatives and postive numbers and zeros

# O(N), as set() is O(1)
def pair_sum_set(array,k):

  if len(array)< 2:
    return 0

  seen = set()
  output = set()

  for num in array:

    target = k - num

    if target not in seen:
      seen.add(num)
    else:
      output.add((min(num, target), max(num, target)))

  return len(output)

# 0(N^2)
def pair_sum(array, k):
  
  # edge case
  if len(array) < 2:
    return {}

  pair = {}

  for i in range(len(array)):
    for j in range(len(array)):
      if i == j:
        continue
  
      num1 = array[i]
      num2 = array[j]
      if (num1 + num2) == k:
        id = (min(num1,num2),max(num1,num2))

        if id in pair:
          pair[id] += 1
        else:
          pair[id] = 1
  
  #pytest.set_trace()
  return len(pair)
        
def test_pair_sum():
  assert(pair_sum([1,9,2,8,3,7,4,6,5,5,13,14,11,13,-1], 10) == 6)
  assert(pair_sum([1,2,3,1],3) == 1)
  assert(pair_sum([1,3,2,2],4) == 2)

def test_pair_sum_set():
  assert(pair_sum_set([1,9,2,8,3,7,4,6,5,5,13,14,11,13,-1], 10) == 6)
  assert(pair_sum_set([1,2,3,1],3) == 1)
  assert(pair_sum_set([1,3,2,2],4) == 2)
