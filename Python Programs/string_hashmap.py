def palindrome(s):
    return s == s[::-1]
s1="rotator"
s2="level"

print(palindrome(s1))
print(palindrome(s2))

def anagram(s1,s2):
    return sorted(s1) == sorted(s2)

s1 = "SILENT"
s2 = "LISTEN"

#sort the string in descending order of lentgh of word

s = "Hello world welcome to programming Happy Coding"
A = s.split()
A.sort(key=len,reverse=True)
print(A)



#sort by frequency

s = "programmingknowledge"
from collections import Counter
CT = Counter(s)
print(CT)
print('-----------------')
A = list(CT.items())
print(A)
print('-----------------')

A.sort(key=lambda x:[x[1],x[0]])
print(A)