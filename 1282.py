groupSizes = [3,1,3,3,3,3,3]

def group(groupSizes):
    hashmap = {}
    ans = []

    for i, size in enumerate(groupSizes):
        if size not in hashmap:
            hashmap[size] = []
        hashmap[size].append(i)

        if len(hashmap[size]) == size:
            ans.append(hashmap[size])
            hashmap[size] = []

    return ans



print(group(groupSizes))