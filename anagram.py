import pytest


def anagram(s1, s2):

    s1 = s1.replace(' ', '')
    s2 = s2.replace(' ', '')

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


def test_anagram():
    assert(anagram('go go go', 'gogogo'))
    assert(anagram('abc', 'cab'))
    assert(anagram('hi     man', 'hi man'))
    assert(anagram('aabbcc', 'aabbc') == False)
    assert(anagram('123', '1 2') == False)
