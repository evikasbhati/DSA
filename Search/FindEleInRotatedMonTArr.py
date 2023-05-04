def Pivot(arr):
    start=0;
    end=len(arr)-1;
    mid=start+(end-start)//2;

    while start<end:
        if arr[mid]>=arr[0]:
            start=mid+1
        else:
            end=mid

        mid=start+(end-start)//2;
    return mid

def Find(arr,ele):
    pivot=Pivot(arr)
    start=0;
    end=len(arr)-1;
    if arr[pivot]==ele:
        return pivot;

    if arr[0]<= ele and ele  <=arr[pivot-1]:
        end=pivot-1
    else:
        start=pivot+1;

    mid=start+(end-start)//2;

    while start<=end:
        if ele==arr[mid]:
            return mid
        if arr[mid]>ele:
            end=mid-1
        else:
            start=mid+1
        mid=start+(end-start)//2;
        
    return -1

ar=[17, 19,25, 28,  4,5, 7, 8, 9, 11,13]
print(Find(ar,5))