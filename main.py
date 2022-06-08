# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True

s1 = "adobe"
s2 = "abode"
def find_anagram(s1, s2):
    # [assignment] Add your code here
    if(sorted(s1) == sorted(s2)):
        return True
    else:
        return False

print(find_anagram(s1,s2))

