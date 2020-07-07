ar=[]
for i in range (0,len(ar)):
	x=int(input("Enter a no.:"))
	ar.append(x)
s=0
for i in range (0,len(ar)):
	s=s+ar[i]
print ("sum is :",s)