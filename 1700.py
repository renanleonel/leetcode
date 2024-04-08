students = [1,1]
sandwiches = [0,1]

def numberOfStudents(students, sandwiches):
    res = len(students)
    hashmap = {}

    for num in students:
        hashmap[num] = 1 + hashmap.get(num, 0)

    for num in sandwiches:
        if num in hashmap and hashmap[num] > 0:
            res -= 1
            hashmap[num] -= 1
        else: 
            return res

    return res

print(numberOfStudents(students, sandwiches))