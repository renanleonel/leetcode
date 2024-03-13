jewels = "aA"
stones = "aAAbbbb"

def jewelsAndStones(jewels, stones):
    hashmap = {}
    result = 0
    
    for i in range(len(stones)):
        hashmap[stones[i]] = 1 + hashmap.get(stones[i], 0)

    for jewel in jewels:
        if jewel in hashmap:
            result+=hashmap[jewel]

    return result

print(jewelsAndStones(jewels, stones))