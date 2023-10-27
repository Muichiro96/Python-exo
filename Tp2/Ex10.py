L1=[1,3,6,78,35,88,55]
L2=[12,24,35,24,88,120,155]
L3=[]
for i in range(len(L1)):
        if L1[i] in L2:
                L3.append(L1[i])
for element in L3:
        print(element,end=" ")
