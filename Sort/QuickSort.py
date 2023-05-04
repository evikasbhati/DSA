
def quickSort(array):

    if len(array)<=1:
        return array
    else:
        print(len(array))
        ele=array[0]
        arrL=[i for i in array[1:] if i<ele];
        arrR=[i for i in array[1:] if i>=ele];
        return quickSort(arrL)+[ele]+quickSort(arrR); 

ar=[115,38,8,9,7,4,19,3,78,45];


print(quickSort(ar))