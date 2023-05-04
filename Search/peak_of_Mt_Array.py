# Find peak of mountain Array?
#-> Mounatin  Array structure is firsr value is ascending order till higest value then
# descending order.
# We have to find the highest value in the array.

# Array examples:
# ar=[3, 4, 7, 8, 9, 11, 17, 19, 28, 25, 18, 15, 12, 7, 5];
# ar=[3, 4, 7, 8, 9, 11, 17, 19,  5];
# ar=[ 17,19, 28, 25, 18, 15, 12, 7, 5];

def peak(arr):
    start=0;
    end=len(arr)-1;
    mid=start+(end-start)//2

    while start<end:
        print("exe")
        if arr[mid]<arr[mid+1]:
            start=mid+1
        else:
            end=mid
            
        mid=start+(end-start)//2
    return mid
            

ar=[3, 4, 7, 8, 9, 11, 17, 19, 28, 25, 18, 15, 12, 7, 5];
print(peak(ar))

