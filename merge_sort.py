def ms(arr,low,high):
    if low==high:
        return
    mid=(low+high)//2
    ms(arr,low,mid)
    ms(arr,mid+1,high)
    merge(arr,low,mid,high)
    

def merge_sort(arr,n):
    ms(arr,0,n-1)
    return arr

def merge(arr,low,mid,high):
    start=low
    right=mid+1
    temp=[]
    while low<=mid and right<=high:
        if arr[low]<=arr[right]:
            temp.append(arr[low])
            low+=1
        else:
            temp.append(arr[right])
            right+=1
    while low<=mid:
        temp.append(arr[low])
        low+=1
    while right<=high:
        temp.append(arr[right])
        right+=1
    for i in range(len(temp)):
        arr[start+i]=temp[i]
   

a=merge_sort([38,27,43,3,9,82,10],7)
print(a)
