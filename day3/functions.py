"""
def fact(n):
    if n==0 or n==1:
        return 1
    ans=1
    for i in range (2,n+1):
        ans*=i
    return ans

n=int(input("Enter a no.:"))
print(fact(n))

"""
"""
def sum(n):
    ans=0
    for i in range (1,n+1):
        ans+=i
    return ans

n=int(input("Enter a no.:"))
print(sum(n))
"""

marks=[23,45,56,78,34]
"""
sum=0
for i in marks:
    sum+=1
print(sum)   
"""
ans = sum(marks)
