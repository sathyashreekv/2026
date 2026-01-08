def movezeroes(arr):
    write=0
    for read in range(0,len(arr)):
        if arr[read]!=0:
            arr[read],arr[write]=arr[write],arr[read]
            write+=1
    return arr

arr=[0,1,0,0,122,0,1,-1]
print(movezeroes(arr))