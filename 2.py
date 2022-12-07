l1=[x for x in range(1,69)]
print(l1)
l2=[]
n=int(input("enter a numbe tio be deleted "))
if n in l1:
    l2.append(n)
    l1.remove(n)
else:
    print("roll no does not exists in the list")
print(l1)
