import pytest
import collections

## Sum solution
# since it's non-negative, could sum up, but it might cause issues for large arrays or vales
# Overflow issue

# N + NLogN + N 
# O(NLogN) 
def finder_dict(arr1, arr2):

    count = {}
    for num in arr2:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    
    for num in arr1:
        if num in count:
            count[num] -= 1
        else:
            count[num] = -1

    for num in count:
        if count[num] != 0:
            print(f"{num} is the missing number")
            return num

    return None

# N + NLogN + N 
# O(NLogN) 
def finder_hash(arr1, arr2):
    count = collections.defaultdict(int)

    for num in arr2:
        count[num] += 1

    for num in arr1:
        if count[num] == 0:
            print(f"{num} is the missing number")
            return num
        else:
            count[num] -= 1

    return None

# O(2NLogN) + O(2N)
# O(NLogN) 
def finder_sort(arr1,arr2):
    
    arr1.sort()
    arr2.sort()

    for num1, num2 in zip(arr1,arr2):
        if num1 != num2:
            print(f"{num1} is the missing number")
            return num1

    return None

# if zero is not present
# O(2N)
def finder_xor(arr1,arr2):
    result = 0

    for num in arr1+arr2:
        result^=num

    if result != 0:
        return result

    return None

def test_finder_dict():
    assert(5 == finder_dict([1,2,3,4,5,6,7],[3,7,2,1,4,6]))
    assert(5 == finder_dict([5,5,7,7],[5,7,7]))
    assert(finder_dict([5,5,7,7],[5,5,7,7]) is None)

def test_finder_sort():
    assert(5 == finder_sort([1,2,3,4,5,6,7],[3,7,2,1,4,6]))
    assert(5 == finder_sort([5,5,7,7],[5,7,7]))
    assert(finder_sort([5,5,7,7],[5,5,7,7]) is None)

def test_finder_hash():
    assert(5 == finder_hash([1,2,3,4,5,6,7],[3,7,2,1,4,6]))
    assert(5 == finder_hash([5,5,7,7],[5,7,7]))
    assert(finder_hash([5,5,7,7],[5,5,7,7]) is None)

def test_finder_xor():
    assert(5 == finder_xor([1,2,3,4,5,6,7],[3,7,2,1,4,6]))
    assert(5 == finder_xor([5,5,7,7],[5,7,7]))
    assert(finder_xor([5,5,7,7],[5,5,7,7]) is None)
