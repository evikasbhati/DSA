
def getElement(arr,ele):
    first=None;
    last=None;

    for i in range(len(arr)):
        if arr[i]==ele:
            if first ==None:
                first=i
            else:
                last=i
    if first: 
        if last is None:
            return first,first
        else:
            return first,last
    else:
        return -1;

ar=[42,1,5,77,88,9,5,99,5,51]
print(getElement(ar, 5))