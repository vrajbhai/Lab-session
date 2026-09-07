# heap sort

do_sort = [55,20,3,66,77,44,22]

def heapify(arr,n,i):
    largest=i
    left = 2 *i + 1
    right = 2 *i + 2
    
    if left < n and arr[left] > arr[largest]:
        largest=left
        
    if right < n and arr[right] > arr[largest]:
        largest=right
        
    if largest != i:
        arr[i],arr[largest]= arr[largest],arr[i]
        heapify(arr,n,largest)
        
        
def buildHeap(arr):
    n = len(arr)
    
    for i in range(n//2-1,-1,-1):
        # i is nothing but parent_index
        heapify(arr,n,i) 
    
    for i in range(n-1,0,-1):
        arr[0],arr[i]=arr[i],arr[0]
        heapify(arr,i,0)
        
        
print(do_sort)

buildHeap(do_sort)

print(do_sort)