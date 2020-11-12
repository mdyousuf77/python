def mostfrequent(x):
    d={}
    for char in x:
        keys=d.keys()
        if char in keys:
            d[char]+=1
        else:
            d[char]=1
    return d
x=input("enter a string:")
print(mostfrequent(x))
