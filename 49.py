strs = ["eat","tea","tan","ate","nat","bat"]

def groupAnagrams(strs):
    hashmap = {}
    for str in strs:
        count = [0] * 26

        for letter in str:
            count[ord(letter) - ord('a')] = letter

        if tuple(count) not in hashmap:
            hashmap[tuple(count)] = []

        hashmap[tuple(count)].append(str)

    return hashmap.values()

print(groupAnagrams(strs))