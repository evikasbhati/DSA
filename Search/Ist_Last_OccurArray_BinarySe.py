# Find the first, last occurrance and occurrance count of a number in array
# using Binary Search
 
def postion(arr,ele):
    start=0;
    end=len(arr)-1;
    middleIndex=start+(end-start)//2;

    while start<=end:
        if ele==arr[middleIndex]:
            return start,middleIndex,end

        if ele>arr[middleIndex]:
            start=middleIndex+1
        else:
            end=middleIndex-1

        middleIndex=middleIndex=start+(end-start)//2;

    return  start,None,end

def getElement(arr,ele):
   
    first=None;
    last=None;

    start,middle,end= postion(arr,ele)
    mid=middle

    if middle is not None:
        while start<=middle:
            if arr[middle]==ele:
                first=middle
                middle-=1
            else:
                break;

        while mid<=end:
            if arr[mid]==ele:
                last=mid
                mid+=1
            else:
                break;
    
        if first is not None: 
            print("occurrence: ",last-first+1)
            if last is None:
                return first,first
            else:
                return first,last
    else:
        return -1;

ar=[3, 4, 7, 8,8,8,8,8, 9, 11, 17, 19, 28, 38, 40, 41,43,43,44,45,45,45,45,45,45,45, 78, 91, 115,115,115,115];
print(getElement(ar, 115))