l1=[20,85,1000,50,100]
n=int(input("enter no to be found"))
if n in l1:
    print(l1.index(n))
else:
    print("does not exists")