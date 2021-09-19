def solvedp(A,n):
    if n==1:
        return A[0]
    #if we have only two values to steal
    if n ==2:
        return max(A)
    A[1] = max(A[0],A[1])

    for i in range(2,n):
        A[i] = max(A[i-1],A[i]+A[i-2])
    
    return A[-1]
