#program to display fibonacci series upto nth term
n=int(input('enter the limit:')) #accepting the limit from user
n1,n2=0,1 #first two terms
i=0
if n<=0:  #checking if the number is valid
    print("enter a positive integer")
elif n==1:
    print("fibonacci series:",n1)
else:
 print("fibonacci series:")
while i<n:
    print(n1)
    n3=n1+n2
    n1=n2 #updating the values
    n2=n3
    i+=1
