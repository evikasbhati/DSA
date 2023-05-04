ar=[2,0,9,3,0,0,5,0]

j=0

for i in range(len(ar)-1):
    if ar[i]!= 0:
        (ar[i],ar[j])=(ar[j],ar[i])
        j+=1

print(ar)