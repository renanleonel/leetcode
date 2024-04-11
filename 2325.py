key = "the quick brown fox jumps over the lazy dog"
message = "vkbs bs t suepuv"

def decodeMessage(key, message):
    hashmap = {}
    alphabetical = 'abcdefghijklmnopqrstuvwxyz'

    i = 0
    for letter in key:
        if letter not in hashmap and letter != ' ':
            hashmap[letter] = alphabetical[i]
            i+=1

    ans = ''

    for letter in message:
        if letter == ' ':
            ans += letter
        
        elif letter in hashmap:
            ans += hashmap[letter]
    
    return ans

print(decodeMessage(key, message))