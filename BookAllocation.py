
def BookAllocation(arr,sNum):
    dArr=arr;
    divNum=round(len(arr)/sNum);
    asum=0;
    maxValue=0;
   
    for i in range(0,len(arr),divNum+1):
        dArr.insert(i+divNum,None)
    
    start=0;
    end=len(dArr)-1;

    if dArr[len(dArr)-1] is not None:
        dArr.append(None)
    print(dArr)

    while start<=end:
        print(start,arr[start])
        if arr[start] is None:
            if asum>maxValue:
                maxValue=asum
                print(asum,"max",maxValue)
            asum =0;

        if arr[start] is not None:
            asum=asum+arr[start]
            print("sum",asum)

        start+=1
        

    return maxValue

ar=[5,1,15,120,11,8,0,177,53]
print(BookAllocation(ar, 6))
# print(round(9/6),len(ar))

