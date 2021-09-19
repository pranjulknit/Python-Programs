'''
given two word1,word2, find the minimum 
number of operations required to convert
word1 to word2


1.insert a character
2.Delete a character
3.Replace a character

'''
def editdist(word1,word2):
    r,c = len(word1),len(word2)
    dp =[[0 for j in range(c+1)] for i in range(r+1)]
    for i in range(r+1):
        for j in range(c+1):
            # firststring is empty
            # insert all chars of second string
            if i==0:
                dp[i][j] = j
            #second string is empty
            #remove all chars of first string
            elif j==0:
                dp[i][j] = i
            # uf both char are same ignore
            elif word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            #else look for min(insert,delete,replace)
            else:
                dp[i][j] = 1 +min(dp[i][j-1],dp[i-1][j],dp[i-1][j-1])

    return dp[r][c]            


word1 = "horse"
word2 = "ros"
ans = editdist(word1,word2)
print(ans)