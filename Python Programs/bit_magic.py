def evenodd(n):
    if n&1:
        print("odd")
    else:
        print("Even")

t = int(input())
while t:
    n = int(input())
    evenodd(n)
    t = t-1
    
