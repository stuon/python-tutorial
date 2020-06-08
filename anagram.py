import pytest
import pdb

# Problem
# determine if two strings are an anagram. Ignore spaces and case in-sensitive
def anagram_native(s1, s2):

    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()

    return sorted(s1) == sorted(s2)

# O(1) + O(NLogN) + O(NLogN) + O(NLogN)
# O(1) + O(4NLogN)
# O(NLogN)
def anagram_count(s1, s2):

    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()

    # Edge case
    if (len(s1) != len(s2)):
        return False

    count = {}
    for i in s1:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1

    for i in s2:
        if i in count:
            count[i] -= 1
        else:           
            count[i] = -1

    for i in count:
        if count[i] != 0:
            return False

    return True

# 2N + 1 + N^2 + N
# N + N^2
# N^2
def anagram(s1, s2):

    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()

    # Edge case
    if (len(s1) != len(s2)):
        return False

    match = [0]*len(s2)

    for i in range(len(s1)):

        found = False

        for j in range(len(s2)):

            # match already found
            if match[j] == 1:
                continue

            if s1[i] == s2[j]:
                found = True
                break

        if found:
            match[j] = 1

    for i in match:
        if i == 0: # at least one match not found
            return False

    return True

def test_anagram_native():

    assert(anagram_native('go go go', 'gogogo'))
    assert(anagram_native('abc', 'cab'))
    assert(anagram_native('hi     man', 'hi man'))
    assert(anagram_native('aabbcc', 'aabbc') == False)
    assert(anagram_native('123', '1 2') == False)
    assert(anagram_native('123', '1 23aa') == False)

def test_anagram_count():

    assert(anagram_count('go go go', 'gogogo'))
    assert(anagram_count('abc', 'cab'))
    assert(anagram_count('hi     man', 'hi man'))
    assert(anagram_count('aabbcc', 'aabbc') == False)
    assert(anagram_count('123', '1 2') == False)
    assert(anagram_count('123', '1 23aa') == False)

def test_anagram():
    assert(anagram('go go go', 'gogogo'))
    assert(anagram('abc', 'cab'))
    assert(anagram('hi     man', 'hi man'))
    assert(anagram('aabbcc', 'aabbc') == False)
    assert(anagram('123', '1 2') == False)
    assert(anagram('123', '1 23aa') == False)
    