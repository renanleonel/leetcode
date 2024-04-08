ransomNote = "bg"
magazine = "efjbdfbdgfjhhaiigfhbaejahgfbbgbjagbddfgdiaigdadhcfcj"


def canConstruct(ransomNote, magazine):
    hashmapR = {}
    hashmapM = {}
    
    for letter in ransomNote:
        hashmapR[letter] = 1 + hashmapR.get(letter, 0)
    
    for letter in magazine:
        hashmapM[letter] = 1 + hashmapM.get(letter, 0)

    for letter in ransomNote:
        if letter not in hashmapM:
            return False
        if hashmapR[letter] > hashmapM[letter]:
            return False

    return True 

print(canConstruct(ransomNote, magazine))