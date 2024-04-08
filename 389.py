s = "abcd"
t = "abcde"

def findTheDifference(s, t):
    hashmap = {}

    for letter in s:
        hashmap[letter] = 1 + hashmap.get(letter, 0)

    for letter in t:
        if letter not in hashmap or hashmap[letter] == 0:
            return letter
        
        hashmap[letter] -= 1

print(findTheDifference(s, t))