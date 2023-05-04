# Condition :Array should be ## Monotonic ## meaning it should be in ascending or descending
# order.
# Time complexity :
# best casr: O(1)
# average and worest case: o(logn)

def BinarySearh(arr,ele):

    start=0;
    end=len(arr)-1;
    middleIndex=start+(end-start)//2;

    while start<=end:
        # print(arr)
        if arr[middleIndex]==ele:
            return middleIndex
        if arr[middleIndex]<ele:
            start=middleIndex+1;
        else:
            end=middleIndex-1;


        middleIndex=start+(end-start)//2;
    return "element not found"
        
ar=[3, 4, 7, 8, 9, 11, 17, 19, 28, 38, 41, 45, 78, 91, 115];

print(BinarySearh(ar, 3))

        
