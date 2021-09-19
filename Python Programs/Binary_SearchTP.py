'''1. find a pair whose sum is equal to target K
**unsorted array
2. Implement binary search in a sorted array
'''
# A = List
#Key = Target Value
#Sorted Array
#Time CMP = LOGN
#SPACE CMP = LOGN(Recursive)
#SPACE CMP = O(1)(Itervative)

'''
def binsearch(a,left,right,key):
    while left <= right:
        mid = (left + right) // 2
        if a[mid] == key:
            return mid
        elif a[mid] <key:
            left = mid +1
        else:
            right = mid -1
    return -1    

A=[25,35,45,80,96,200]
key = 200
#print(binsearch(A,0,len(A)-1,key))
#Bisect ac as a binary search
import bisect
print(bisect.bisect_left(A,key,0,len(A)))
'''

A=[10,35,80,96,200,500,850,7]
k = 17
def findTargetPair(A,k):
    st = set()
    for i in range(len(A)):
        complement = k -A[i]
        if complement in st:
            return[complement,A[i]]
        else:
            st.add(A[i])
print(findTargetPair(A,k))
