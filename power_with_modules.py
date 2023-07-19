def power_modules(A,B,C):
    result=1
    for i in range(B):
        result=(result*A)%C
    return result
A,B,C=map(int,input().split())
result=power_modules(A,B,C)
print(result)
