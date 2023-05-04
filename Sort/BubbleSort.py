ar=[115,38,8,9,7,4,19,3,78,45,1];

def BubbleSort(array1):

    for j in range(len(array1)):
        swapped=False
        print(ar)
        for i in range(len(array1)-1-j):
            if ar[i]>ar[i+1]:
                temp=ar[i];
                ar[i]=ar[i+1];
                ar[i+1]=temp;
                swapped=True;
        if swapped==False:
            return ;   

BubbleSort(ar)
# print(ar)