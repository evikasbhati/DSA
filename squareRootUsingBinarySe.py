## Find squareRoot of a number Using Binary Search rounding to 3 decimal place.

# Function to find square root integer value
def sqIntValue(num):
    start=0;
    end=num-1
    mid=start+(end-start)//2
    ans=None

    while start<=end:
        if mid*mid>num:
            end=mid-1;
        else:
            ans=mid;
            start=mid+1

        mid=start+(end-start)//2;
    return ans
# Function to find decimal place
def deciValue(value,num,di):
    ans=default=num+0.0
    start=0;
    end=5;
    d=num+5/di

    if d*d<value:
        start=5;
        end=10;

    for i in range(start,end):
        num=default
        if num*num<value:
            num=num+i/di
            if num*num<value:
                ans=num;

    return ans      

def squarRoot(value):
    intValue=sqIntValue(value)
    tenth=deciValue(value,intValue,10)
    hund=deciValue(value, tenth, 100)
    thous=deciValue(value, hund, 1000)
    return round(thous,3)
    
print(squarRoot(38))