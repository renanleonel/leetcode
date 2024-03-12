s = "anagram"
t = "nagaram"

def validAnagram(s, t):
    if len(s) != len(t):
        return False 
    
    hashS, hashT = {}, {}

    for i in range(len(s)):
        hashS[s[i]] = 1 + hashS.get(s[i], 0)
        hashT[t[i]] = 1 + hashT.get(t[i], 0)

    return True if hashS == hashT else False
        

print(validAnagram(s, t))