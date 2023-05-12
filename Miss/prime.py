primeN=[];

for i in range(2,101):
    prime=False;
    for j in range(2,i):
        if i%j==0:
            prime=True;
            break
    if prime is False:
        primeN.append(i)

print(primeN)
print("No of elements",len(primeN))