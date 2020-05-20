def heapify(arr,n,i):
    largest = i
    l = 2*i+1
    r = 2*i+2
    if l<n and arr[i]<arr[l]:
        largest= l
    if r<n and arr[largest]<arr[r]:
        largest = r
    if largest!=i:
        arr[i],arr[largest]=arr[largest],arr[i]
        heapify(arr,n,largest)

def insert(array,num):
    size = len(array)
    array.append(num)
    for i in range((size//2)-1,-1,-1):#this is actually going from size//2 -1 to 0
        heapify(array,size,i)

def deleteNode(array,num):
    size = len(array)
    i = 0
    for i in range(0,size):
        if num == array[i]:
            break
    arr[i],array[size-1]=array[size-1],arr[i]
    array.remove(size-1)
    for i in range((len(array)//2)-1,-1,-1):
        heapify(array,len(array),i)


arr = []
insert(arr,1)
insert(arr,2)
insert(arr,3)
insert(arr,4)
insert(arr,5)

print("Max-Heap array: "+ str(arr))

# if size is 10 then size//2 is 5,then 5-1 will be 4 then
#by using range(4,-1)

deleteNode(arr,4)
print("After deleting an element: "+str(arr))
