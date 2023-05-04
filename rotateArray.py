# Rotation of aaray means shiftig array elements postion to left or right
# by specific place.
ar=[3, 4, 7, 8, 9, 11, 17, 19, 28];

def rotateArray(arr,postion,dir="right"):
    for i in range(len(arr)-1,postion-1,-1):
        (arr[i],arr[i-postion])=(arr[i-postion],arr[i])


rotateArray(ar,3)
print(ar)