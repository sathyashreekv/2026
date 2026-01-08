def removeduplicates(arr):
    write=0
   
    for read in range(1,len(arr)):
        if arr[write]!=arr[read]:
            write+=1
            arr[write]=arr[read]
           
            
    return 


arr=[1,1,2]
print(removeduplicates(arr))
    
