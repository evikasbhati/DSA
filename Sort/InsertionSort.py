ar=[115,38,8,9,7,4,19,3,78,45];
def InsertionSort(array):

    for i in range(1,len(array)):
        newValue=array[i];

        for j in range(i,-1,-1):
            if newValue<array[j]:
                temp=array[j];
                array[j]=newValue;
                array[j+1]=temp;
        print(ar)

InsertionSort(ar)
print(ar)