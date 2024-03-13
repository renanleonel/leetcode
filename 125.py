s = "A man, a plan, a canal: Panama"

def validPalindrome(s):
    string = ''

    for char in s:
        if(char.isalnum()):
            string+=char.lower()

    l, r = 0, len(string)-1

    while l < r:
        if string[l] != string[r]:
            return False
        
        l+=1
        r-=1
    
    return True

print(validPalindrome(s))