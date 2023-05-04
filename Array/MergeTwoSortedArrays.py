# Merge two sorted arrays

ar1=[5,7,9,71]
ar2=[3,5,12,17,19,43]

ar=[i for i in range(len(ar1)+len(ar2))]
i=j=k=0;

while i<len(ar1) and j<len(ar2):
    if ar1[i]>ar2[j]:
        ar[k]=ar2[j]
        j+=1
    else:
        ar[k]=ar1[i]
        i+=1
    k+=1


while i<len(ar1):
    ar[k]=ar1[i]
    i+=1
    j+=1

while j<len(ar2):
    ar[k]=ar2[j]
    j+=1
    k+=1


print(ar)
