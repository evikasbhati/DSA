ar=[115,38,8,9,7,4,19,3,78,45];

def min(index,arr=[]):
    minValue=arr[index];
    sIndex=index
    for i in range(index+1,len(arr)):
        if minValue>arr[i]:
            minValue=arr[i]
            sIndex=i
    return sIndex
    
def selectionSort(array):
    for i in range(len(array)):
        k=min(i,array);
        temp=array[k];
        array[k]=array[i];
        array[i]=temp;

selectionSort(ar)

print(ar)