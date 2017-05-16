# Project Zero - Introduction to Unit Testing
# NAME: George Gu
# DUE DATE: N/A
# OTHER COMMENTS: N/A

def euclid(a,b):
    if a<b:
        a, b = b, a
    while a%b > 0:  
        a, b = b, a%b
    return b    

def coprime(L):
    for i in range(len(L)-1):
        for j in range(i+1,len(L)):
            if euclid(L[i],L[j])>1:
                return False
    return True        

def fibonacci(n):
    v=[0]*n    
    v[0]=1
    if n==1:
        return v
    v[1]=1
    if n==2:
        return v
    for i in range(2,n):
        v[i]=v[i-1]+v[i-2]
    return v
    