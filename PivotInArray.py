# Pivot is highest or lowest value in a  monotonic array which is rotated;
# Example: ar=[17, 19, 28, 3, 4, 7, 8, 9, 11];
# We will find lowest 

def Pivot(arr):
    start=0;
    end=len(arr)-1;
    mid=start+(end-start)//2

    while start<end:
        if arr[mid]>=arr[0]:
            start=mid+1
        else:
            end=mid

        mid=start+(end-start)//2
    return mid

ar=[17, 19, 28, 3, 4, 7, 8, 9, 11];
print(Pivot(ar))