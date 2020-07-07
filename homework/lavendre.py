"""
n=int(input("enter a no.:"))
i=1
c=0
while (i<=n):
	k=0
	if (n%i==0):
		j=1
		while(j<=i):
			if (i%j==0):
				k=k+1
			j+=1
		if k==2:
			c+=1
	
	i=i+1
print(c)
"""


n=int(input("enter a no.:"))
i=1
k=0
for i in range (1,n+1):
        if n%i==0:
                c=0
                for j in range (1,i+1):
                        if i%j==0:
                                c+=1
                if c==2:
                        k+=1
print("the no. of factors are:",k)
