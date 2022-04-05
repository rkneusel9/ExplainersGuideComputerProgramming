def unique(A):
    B = []
    for k in A:
        if (k not in B):
            B.append(k)
    return B

A = [1,3,2,1,4]
print(A)
print(unique(A))
Z = ["a",1,"b",0,1,"a","aa"]
print(Z)
print(unique(Z))

