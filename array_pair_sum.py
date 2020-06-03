import pytest

# Problem
# Given an integer array, output all the unique pairs that sum up to a specific value K

def pair_sum(array, k):
  
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
