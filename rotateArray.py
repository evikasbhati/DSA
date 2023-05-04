# Rotation of aaray means shiftig array elements postion to left or right
# by specific place.
ar=[3, 4, 7, 8, 9, 11, 17, 19, 28];
def rotateArray(arr,postion):
    n=len(ar)
    temp=[];
    for i in range(len(arr)):
        temp.insert((i+postion)%n, ar[i])
        print((i+postion)%n)

    return temp
    


print(rotateArray(ar,3))
